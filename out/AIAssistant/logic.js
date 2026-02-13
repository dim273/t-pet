const vscode = require("vscode");
const fs = require('fs');
const path = require('path');
const https = require('https');

class AIAssistantLogic {
    constructor(provider) {
        this.provider = provider;
    }

    // 更新最后活动的编辑器上下文
    updateLastActiveContext(editor) {
        if (editor && editor.document && editor.document.uri.scheme === 'file') {
            const document = editor.document;
            const selection = editor.selection;
            const code = selection.isEmpty ? document.getText() : document.getText(selection);
            
            this.provider._lastActiveEditorContext = {
                fileName: path.basename(document.fileName),
                code: code,
                languageId: document.languageId,
                timestamp: Date.now()
            };
        }
    }

    /**
     * 根据 ref 获取题目信息
     */
    getProblemByRef(ref) {
        try {
            const problemDataPath = path.join(this.provider._extensionUri.fsPath, 'media', 'ProblemList', 'data.js');
            if (fs.existsSync(problemDataPath)) {
                const content = fs.readFileSync(problemDataPath, 'utf8');
                const refInt = parseInt(ref);
                const problemRegex = new RegExp(`\\{[^\\{]*?ref:\\s*${refInt}[^\\}]*?\\}`, 'gs');
                const match = problemRegex.exec(content);
                if (match) {
                    const objStr = match[0];
                    const title = /title:\s*"(.*?)"/.exec(objStr)?.[1] || "未知题目";
                    const difficulty = /difficulty:\s*"(.*?)"/.exec(objStr)?.[1] || "未知难度";
                    const tagsMatch = /tags:\s*\[(.*?)\]/.exec(objStr);
                    const tags = tagsMatch ? tagsMatch[1].split(',').map(s => s.trim().replace(/"/g, '')) : [];
                    return { title, difficulty, tags, ref: refInt };
                }
            }
        } catch (e) {
            console.error("读取题目信息失败:", e);
        }
        return null;
    }

    /**
     * 获取学习进度摘要，包括知识树完成情况和最近发展区 (ZPD)
     */
    getLearningProgressSummary() {
        const passedProblems = new Set(this.provider.saveData.progress?.passedProblems || []);
        const summary = {
            passedCount: passedProblems.size,
            totalNodes: 0,
            completedCount: 0,
            completedNodes: [],
            zpdNodes: [], // 最近发展区：已解锁但未完成
            lockedNodes: [],
            totalProgress: 0
        };

        try {
            const treeDataPath = path.join(this.provider._extensionUri.fsPath, 'media', 'TreeNode', 'data.js');
            const problemDataPath = path.join(this.provider._extensionUri.fsPath, 'media', 'ProblemList', 'data.js');
            
            if (fs.existsSync(treeDataPath) && fs.existsSync(problemDataPath)) {
                const treeContent = fs.readFileSync(treeDataPath, 'utf8');
                const problemContent = fs.readFileSync(problemDataPath, 'utf8');

                // 1. 提取题单对应的题目 ref 列表
                const problemSetsMap = {};
                const problemSetRegex = /"list_(\d+)":\s*\{.*?problems:\s*\[([\s\S]*?)\s*\]\s*\}/g;
                let psMatch;
                while ((psMatch = problemSetRegex.exec(problemContent)) !== null) {
                    const listId = psMatch[1];
                    const problemsText = psMatch[2];
                    const refs = [];
                    const refRegex = /ref:\s*(\d+)/g;
                    let refMatch;
                    while ((refMatch = refRegex.exec(problemsText)) !== null) {
                        refs.push(parseInt(refMatch[1]));
                    }
                    problemSetsMap[listId] = refs;
                }

                // 2. 提取所有知识点节点信息
                const allNodes = [];
                const nodeMap = new Map();
                
                const nodeObjRegex = /\{([\s\S]*?)\}/g;
                let objMatch;
                
                const extractProp = (str, key) => {
                    const regex = new RegExp(`${key}:\\s*(?:"(.*?)"|(\\d+)|(\\[.*?\\]))`);
                    const match = regex.exec(str);
                    if (!match) return null;
                    return match[1] || match[2] || match[3];
                };

                while ((objMatch = nodeObjRegex.exec(treeContent)) !== null) {
                    const content = objMatch[1];
                    // 必须包含 id 或 title
                    const idVal = extractProp(content, 'id');
                    const titleVal = extractProp(content, 'title');
                    const id = idVal || titleVal;
                    
                    if (!id) continue;

                    const qListIdStr = extractProp(content, 'questionList');
                    const parentStr = extractProp(content, 'parent');
                    
                    if (id) {
                        const qListId = qListIdStr ? parseInt(qListIdStr) : 0;
                        let parents = [];
                        if (parentStr) {
                            parents = parentStr.replace(/[\[\]"]/g, '').split(',').map(s => s.trim()).filter(s => s);
                        }

                        const node = {
                            id: id,
                            qListId: qListId,
                            parents: parents,
                            completed: false,
                            unlocked: false
                        };
                        allNodes.push(node);
                        nodeMap.set(id, node);
                    }
                }

                // 3. 计算节点状态
                allNodes.forEach(node => {
                    if (node.qListId > 0) {
                        const requiredRefs = problemSetsMap[node.qListId] || [];
                        if (requiredRefs.length > 0 && requiredRefs.every(ref => passedProblems.has(ref))) {
                            node.completed = true;
                        }
                    }
                });

                for (let i = 0; i < 5; i++) {
                    let changed = false;
                    allNodes.forEach(node => {
                        if (node.qListId === 0 && !node.completed) {
                            // 找到所有以当前节点为父节点的子节点
                            const children = allNodes.filter(n => n.parents.includes(node.id));
                            
                            const leafChildren = children.filter(n => n.qListId > 0);
                            const categoryChildren = children.filter(n => n.qListId === 0);

                            if (leafChildren.length > 0) {
                                if (leafChildren.every(c => c.completed)) {
                                    node.completed = true;
                                    changed = true;
                                }
                            } else if (categoryChildren.length > 0) {
                                if (categoryChildren.every(c => c.completed)) {
                                    node.completed = true;
                                    changed = true;
                                }
                            } else {
                                if (node.id === "编程学习之旅") { // Root
                                    node.completed = true;
                                    changed = true;
                                }
                            }
                        }
                    });
                    if (!changed) break;
                }
                
                // 特殊处理：根节点总是完成和解锁的
                const rootNode = nodeMap.get("编程学习之旅");
                if (rootNode) {
                    rootNode.completed = true;
                    rootNode.unlocked = true;
                }

                for (let i = 0; i < 5; i++) {
                    allNodes.forEach(node => {
                        if (!node.unlocked) {
                            if (node.parents.length === 0) {
                                // 没有父节点（可能是 treeNode_X 里的副本 Root），默认解锁
                                node.unlocked = true;
                            } else {
                                // 检查父节点
                                const parent = nodeMap.get(node.parents[0]); // 假设单父节点
                                if (parent) {
                                    if (node.qListId > 0) {
                                        // Leaf Node: 只要父节点 Unlocked 即可 (进入章节即解锁所有题目)
                                        if (parent.unlocked) node.unlocked = true;
                                    } else {
                                        // Category Node: 需要父节点 Completed (章节之间的序列依赖)
                                        // 特例：如果父节点是 Root，则只要 Root Unlocked (总是 true)
                                        if (parent.id === "编程学习之旅") {
                                            node.unlocked = true;
                                        } else if (parent.completed) {
                                            node.unlocked = true;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }

                // 收集统计数据
                allNodes.forEach(node => {
                    if (node.completed) {
                        summary.completedCount++;
                        summary.completedNodes.push(node.id);
                    }
                    summary.totalNodes++;
                });

                // 收集 ZPD (已解锁但未完成的 Leaf Node)
                allNodes.forEach(node => {
                    if (node.qListId > 0 && node.unlocked && !node.completed) {
                        let label = node.id;
                        if (node.parents && node.parents.length > 0) {
                            // 尝试找到一个非 Root 的 Parent 作为一级分类
                            const parentId = node.parents.find(p => !p.endsWith('*') && p !== "编程学习之旅");
                            if (parentId) {
                                label = `${parentId} > ${node.id}`;
                            }
                        }
                        
                        summary.zpdNodes.push({ id: node.id, label: label });
                    } else if (!node.unlocked) {
                        summary.lockedNodes.push(node.id);
                    }
                });
                
                // 转换 completedNodes 为 ID 列表
                summary.zpdNodeIds = summary.zpdNodes.map(n => n.id);
                
                if (summary.totalNodes > 0) {
                    summary.totalProgress = Math.round((summary.completedCount / summary.totalNodes) * 100);
                }
            }
        } catch (e) {
            console.error("获取进度摘要失败:", e);
        }

        return summary;
    }

    async handleAiRequest(payload) {
        const { mode, message, extraData, workspaceCode } = payload;

        if (!this.provider.saveData.aiHistory) {
            this.provider.saveData.aiHistory = { sessions: [], currentSessionId: "" };
        }

        if (!this.provider.saveData.aiHistory.currentSessionId) {
            const newSession = {
                id: Date.now().toString(),
                title: "新对话",
                timestamp: Date.now(),
                messages: []
            };
            this.provider.saveData.aiHistory.sessions.push(newSession);
            this.provider.saveData.aiHistory.currentSessionId = newSession.id;
        }

        const currentSession = this.provider.saveData.aiHistory.sessions.find(s => s.id === this.provider.saveData.aiHistory.currentSessionId);
        const isFirstMessage = currentSession && currentSession.messages.length === 0;

        let footerText = "";
        if (mode === "code") {
            const fileName = this.provider._lastActiveEditorContext ? this.provider._lastActiveEditorContext.fileName : "未知文件";
            footerText = `当前提问代码文件：${fileName}`;
        } else if (mode === "problem") {
            footerText = `当前提问题目编号：${extraData?.problemId || '未知'}`;
        } else if (mode === "knowledge") {
            footerText = `当前提问知识点：${extraData?.knowledge || '未知'}`;
        }

        const userMsg = { 
            role: "user", 
            content: message, 
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            footer: footerText 
        };
        currentSession.messages.push(userMsg);

        const progressSummary = this.getLearningProgressSummary();
        
        let dynamicPrompt = "";
        let finalUserMessage = message;

        if (mode === "code") {
            let codeContext = "";
            if (workspaceCode || extraData?.workspaceCode) {
                const activeEditor = vscode.window.activeTextEditor;
                if (activeEditor) {
                    this.updateLastActiveContext(activeEditor);
                }

                if (this.provider._lastActiveEditorContext) {
                    const { fileName, code } = this.provider._lastActiveEditorContext;
                    codeContext = `\n\n【当前工作区代码 (${fileName})】:\n\`\`\`\n${code}\n\`\`\``;
                }
            }
            
            dynamicPrompt = `你现在处于【代码建议】模式。
你的任务是分析学生提供的代码，给出改进建议。
**模式指令：**
1. 重点关注代码的可读性、逻辑正确性和效率。
2. 采用引导式提问，例如“你觉得这里如果输入负数会发生什么？”。
3. 给出优化方向，而不是直接重写整个函数。`;
            
            finalUserMessage = `${message}${codeContext}`;

        } else if (mode === "problem" && extraData?.problemId) {
            const problemRef = extraData.problemId;
            let problemFileContent = "";
            try {
                const problemFilePath = path.join(this.provider._extensionUri.fsPath, "res", "Problem", `${problemRef}.md`);
                if (fs.existsSync(problemFilePath)) {
                    problemFileContent = fs.readFileSync(problemFilePath, 'utf8');
                }
            } catch (err) {
                console.error("读取题目文件失败:", err);
            }

            if (!problemFileContent) {
                if (this.provider._view && this.provider._view.webview) {
                    this.provider._view.webview.postMessage({
                        type: 'aiError',
                        text: `抱歉，找不到编号为 ${problemRef} 的题目源文件。`
                    });
                }
                return;
            }
            
            dynamicPrompt = `你现在处于【题目解析】模式。
当前学生正在询问题目编号为 ${problemRef} 的问题。
**题目原文内容：**
${problemFileContent}

**模式指令：**
1. **绝对禁止直接给出答案 or 完整代码**。
2. 你的任务是引导学生分析题目的输入输出要求，拆解核心逻辑。
3. 结合题目原文，解释其中的难点或容易误解的地方。
4. 鼓励学生先用自然语言描述思路。`;
            
            finalUserMessage = `关于题目 ${problemRef}，我的问题是：${message}`;

        } else if (mode === "knowledge" && extraData?.knowledge) {
            const knowledgeNodeId = extraData.knowledge;
            dynamicPrompt = `你现在处于【知识深度学习】模式。
学生选择了知识点：${knowledgeNodeId}。

**模式指令：**
1. **关联旧知**：重点引导学生根据他们【已经玩转的领域】(${progressSummary.completedNodes.join(', ') || '编程基础'})来理解这个新知识点。
2. **循序渐进**：如果这是一个复杂的概念，先解释最基础的部分，通过类比来降低认知负荷。
3. **学以致用**：尝试给出一个微型场景或代码片段，让学生思考这个知识点如何解决问题。`;
            
            finalUserMessage = `我想学习知识点“${knowledgeNodeId}”，我的问题是：${message}`;
        }

        const systemPrompt = `你是一位亲切且专业的编程导师。你的目标是作为伙伴引导学生思考，而不是作为老师说教。

**核心指令：**
1. **隐藏术语**：严禁在回复中提及“最近发展区”、“ZPD”、“脚手架”、“认知负荷”等任何教育学或心理学专业术语。
2. **顺滑引导**：根据学生【已完全掌握】的知识，自然地类比或推导出【正在学习】中的新概念。
3. **阶梯式沟通：**
   - 如果学生卡住了，先问一个引导性的小问题。
   - 严禁提及学生【尚未解锁】的深奥概念。
4. **语气定位**：幽默、鼓励、平等。

**学生当前画像：**
- 整体进度：${progressSummary.totalProgress}% (已通关 ${progressSummary.passedCount} 题)
- 已经玩转的领域：${progressSummary.completedNodes.join(', ') || '刚开始起步'}
- 正在攻克的难关：${progressSummary.zpdNodeIds.join(', ') || '正在寻找新挑战'}
- 暂时未触及的迷雾：${progressSummary.lockedNodes.slice(0, 10).join(', ') + (progressSummary.lockedNodes.length > 10 ? '...' : '') || '无'}

${dynamicPrompt}

**回复准则：**
- 如果涉及到代码，优先给思路或伪代码；必须给代码时，只给关键的一两行，剩下的留给学生补全。
- 当学生问“该学什么”时，自然地引导他们去尝试【正在攻克】列表中的内容。`;

        const historyMessages = [
            { role: "system", content: systemPrompt },
            ...currentSession.messages.slice(-11, -1).map(m => ({
                role: m.role,
                content: m.content
            })),
            { role: "user", content: finalUserMessage }
        ];

        let apiKey = "";
        let model = "";
        try {
            const configPath = path.join(this.provider._extensionUri.fsPath, 'aiConfig.json');
            if (fs.existsSync(configPath)) {
                const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
                apiKey = config.openrouter?.apiKey || "";
                model = config.openrouter?.model || model;
            }
        } catch (error) {
            console.error("读取 aiConfig.json 失败:", error);
        }

        if (!apiKey) {
            apiKey = vscode.workspace.getConfiguration('t-pet').get('openrouterApiKey') || process.env.OPENROUTER_API_KEY;
        }

        if (!apiKey || apiKey === "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" || apiKey === "<OPENROUTER_API_KEY>") {
            if (this.provider._view && this.provider._view.webview) {
                this.provider._view.webview.postMessage({
                    type: 'aiError',
                    text: "无效或未配置 API Key。请在插件设置中配置 't-pet.openrouterApiKey'。您可以从 openrouter.ai 获取免费 Key。"
                });
            }
            return;
        }

        try {
            const postData = JSON.stringify({
                "model": model,
                "messages": historyMessages,
                "stream": true
            });

            const options = {
                hostname: 'openrouter.ai',
                port: 443,
                path: '/api/v1/chat/completions',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`,
                    'HTTP-Referer': 'https://github.com/t-pet',
                    'X-Title': 'T-Pet VSCode Extension',
                    'Content-Length': Buffer.byteLength(postData)
                }
            };

            let fullAssistantContent = "";
            let fullAssistantThought = "";

            const req = https.request(options, (res) => {
                let buffer = '';

                res.on('data', (chunk) => {
                    buffer += chunk.toString();
                    const lines = buffer.split('\n');
                    buffer = lines.pop();

                    for (const line of lines) {
                        if (line.trim() === '') continue;
                        if (line.startsWith('data: ')) {
                            const data = line.slice(6);
                            if (data === '[DONE]') {
                                this.saveAssistantMessageToHistory(fullAssistantContent, fullAssistantThought);
                                if (isFirstMessage) {
                                    this.generateSessionTitle(currentSession.id, message, fullAssistantContent, apiKey, model);
                                }
                                if (this.provider._view && this.provider._view.webview) {
                                    this.provider._view.webview.postMessage({ type: 'aiStreamDone' });
                                }
                                continue;
                            }

                            try {
                                const parsed = JSON.parse(data);
                                const delta = parsed.choices[0]?.delta || {};
                                const content = delta.content || "";
                                const reasoning = delta.reasoning_content || delta.reasoning || "";
                                
                                if (content) fullAssistantContent += content;
                                if (reasoning) fullAssistantThought += reasoning;

                                if (content || reasoning) {
                                    if (this.provider._view && this.provider._view.webview) {
                                        this.provider._view.webview.postMessage({
                                            type: 'aiStreamChunk',
                                            content: content,
                                            reasoning: reasoning
                                        });
                                    }
                                }
                            } catch (e) {
                                console.error("解析流数据失败:", e, data);
                            }
                        }
                    }
                });

                res.on('end', () => {
                    if (this.provider._view && this.provider._view.webview) {
                        this.provider._view.webview.postMessage({ type: 'aiStreamDone' });
                    }
                });
            });

            req.on('error', (e) => {
                if (this.provider._view && this.provider._view.webview) {
                    this.provider._view.webview.postMessage({
                        type: 'aiError',
                        text: `网络请求失败: ${e.message}`
                    });
                }
            });

            req.write(postData);
            req.end();

        } catch (error) {
            if (this.provider._view && this.provider._view.webview) {
                this.provider._view.webview.postMessage({
                    type: 'aiError',
                    text: error.message
                });
            }
        }
    }

    async generateSessionTitle(sessionId, userMessage, aiResponse, apiKey, model) {
        try {
            const prompt = `请根据以下对话内容，生成一个简短的标题（不超过10个字）。直接返回标题文字，不要包含引号或任何解释。
用户：${userMessage}
助手：${aiResponse.slice(0, 100)}...`;

            const postData = JSON.stringify({
                "model": model,
                "messages": [{ role: "user", content: prompt }],
                "stream": false
            });

            const options = {
                hostname: 'openrouter.ai',
                port: 443,
                path: '/api/v1/chat/completions',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Length': Buffer.byteLength(postData)
                }
            };

            const req = https.request(options, (res) => {
                let data = '';
                res.on('data', (chunk) => data += chunk);
                res.on('end', () => {
                    try {
                        const parsed = JSON.parse(data);
                        let title = parsed.choices[0]?.message?.content?.trim() || "";
                        
                        if (!title) {
                            title = userMessage.slice(0, 10) + (userMessage.length > 10 ? "..." : "");
                        }

                        title = title.replace(/["'。]/g, '');
                        
                        const session = this.provider.saveData.aiHistory?.sessions.find(s => s.id === sessionId);
                        if (session) {
                            session.title = title;
                            this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
                            this.handleLoadAiHistory();
                        }
                    } catch (e) {
                        console.error("解析标题生成结果失败，使用兜底逻辑:", e);
                        const title = userMessage.slice(0, 10) + (userMessage.length > 10 ? "..." : "");
                        const session = this.provider.saveData.aiHistory?.sessions.find(s => s.id === sessionId);
                        if (session) {
                            session.title = title;
                            this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
                            this.handleLoadAiHistory();
                        }
                    }
                });
            });
            req.write(postData);
            req.end();
        } catch (error) {
            console.error("生成标题请求失败:", error);
        }
    }

    saveAssistantMessageToHistory(content, thought) {
        if (!content && !thought) return;
        
        const currentSession = this.provider.saveData.aiHistory?.sessions.find(s => s.id === this.provider.saveData.aiHistory.currentSessionId);
        if (currentSession) {
            currentSession.messages.push({
                role: "assistant",
                content: content,
                thought: thought,
                time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            });
            this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
            this.handleLoadAiHistory();
        }
    }

    handleLoadAiHistory() {
        if (!this.provider.saveData.aiHistory) {
            this.provider.saveData.aiHistory = { sessions: [], currentSessionId: "" };
        }
        
        const progressSummary = this.getLearningProgressSummary();

        if (this.provider._view && this.provider._view.webview) {
            this.provider._view.webview.postMessage({
                type: 'aiHistoryLoaded',
                history: {
                    ...this.provider.saveData.aiHistory,
                    zpdNodes: progressSummary.zpdNodes
                }
            });
        }
    }

    handleSwitchAiSession(sessionId) {
        if (this.provider.saveData.aiHistory) {
            this.provider.saveData.aiHistory.sessions = this.provider.saveData.aiHistory.sessions.filter(s => 
                s.messages.length > 0 || s.id === sessionId
            );
            
            this.provider.saveData.aiHistory.currentSessionId = sessionId;
            this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
            this.handleLoadAiHistory();
        }
    }

    handleCreateNewAiSession() {
        if (!this.provider.saveData.aiHistory) {
            this.provider.saveData.aiHistory = { sessions: [], currentSessionId: "" };
        }
        
        this.provider.saveData.aiHistory.sessions = this.provider.saveData.aiHistory.sessions.filter(s => s.messages.length > 0);
        
        const newSession = {
            id: Date.now().toString(),
            title: "新对话",
            timestamp: Date.now(),
            messages: []
        };
        
        this.provider.saveData.aiHistory.sessions.unshift(newSession);
        this.provider.saveData.aiHistory.currentSessionId = newSession.id;
        this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
        this.handleLoadAiHistory();
    }

    handleDeleteAiSession(sessionId) {
        if (this.provider.saveData.aiHistory) {
            this.provider.saveData.aiHistory.sessions = this.provider.saveData.aiHistory.sessions.filter(s => s.id !== sessionId);
            if (this.provider.saveData.aiHistory.currentSessionId === sessionId) {
                this.provider.saveData.aiHistory.currentSessionId = this.provider.saveData.aiHistory.sessions[0]?.id || "";
            }
            this.provider.storage.updateAccountByIndex(this.provider._currentAccountId, this.provider.saveData);
            this.handleLoadAiHistory();
        }
    }

    getLearningProgressSummary() {
        const passedProblems = new Set(this.provider.saveData.progress?.passedProblems || []);
        const summary = {
            passedCount: passedProblems.size,
            totalNodes: 0,
            completedCount: 0,
            completedNodes: [],
            zpdNodes: [],
            lockedNodes: [],
            totalProgress: 0
        };

        try {
            const treeDataPath = path.join(this.provider._extensionUri.fsPath, 'media', 'TreeNode', 'data.js');
            const problemDataPath = path.join(this.provider._extensionUri.fsPath, 'media', 'ProblemList', 'data.js');
            
            if (fs.existsSync(treeDataPath) && fs.existsSync(problemDataPath)) {
                const treeContent = fs.readFileSync(treeDataPath, 'utf8');
                const problemContent = fs.readFileSync(problemDataPath, 'utf8');

                const problemSetsMap = {};
                const problemSetRegex = /"list_(\d+)":\s*\{.*?problems:\s*\[([\s\S]*?)\s*\]\s*\}/g;
                let psMatch;
                while ((psMatch = problemSetRegex.exec(problemContent)) !== null) {
                    const listId = psMatch[1];
                    const problemsText = psMatch[2];
                    const refs = [];
                    const refRegex = /ref:\s*(\d+)/g;
                    let refMatch;
                    while ((refMatch = refRegex.exec(problemsText)) !== null) {
                        refs.push(parseInt(refMatch[1]));
                    }
                    problemSetsMap[listId] = refs;
                }

                const allNodes = [];
                const nodeMap = new Map();
                
                const nodeObjRegex = /\{([\s\S]*?)\}/g;
                let objMatch;
                
                const extractProp = (str, key) => {
                    const regex = new RegExp(`${key}:\\s*(?:"(.*?)"|(\\d+)|(\\[.*?\\]))`);
                    const match = regex.exec(str);
                    if (!match) return null;
                    return match[1] || match[2] || match[3];
                };

                while ((objMatch = nodeObjRegex.exec(treeContent)) !== null) {
                    const content = objMatch[1];
                    const idVal = extractProp(content, 'id');
                    const titleVal = extractProp(content, 'title');
                    const id = idVal || titleVal;
                    
                    if (!id) continue;

                    const qListIdStr = extractProp(content, 'questionList');
                    const parentStr = extractProp(content, 'parent');
                    
                    if (id) {
                        const qListId = qListIdStr ? parseInt(qListIdStr) : 0;
                        let parents = [];
                        if (parentStr) {
                            parents = parentStr.replace(/[\[\]"]/g, '').split(',').map(s => s.trim()).filter(s => s);
                        }

                        const node = {
                            id: id,
                            qListId: qListId,
                            parents: parents,
                            completed: false,
                            unlocked: false
                        };
                        allNodes.push(node);
                        nodeMap.set(id, node);
                    }
                }

                allNodes.forEach(node => {
                    if (node.qListId > 0) {
                        const requiredRefs = problemSetsMap[node.qListId] || [];
                        if (requiredRefs.length > 0 && requiredRefs.every(ref => passedProblems.has(ref))) {
                            node.completed = true;
                        }
                    }
                });

                for (let i = 0; i < 5; i++) {
                    let changed = false;
                    allNodes.forEach(node => {
                        if (node.qListId === 0 && !node.completed) {
                            const children = allNodes.filter(n => n.parents.includes(node.id));
                            const leafChildren = children.filter(n => n.qListId > 0);
                            const categoryChildren = children.filter(n => n.qListId === 0);

                            if (leafChildren.length > 0) {
                                if (leafChildren.every(c => c.completed)) {
                                    node.completed = true;
                                    changed = true;
                                }
                            } else if (categoryChildren.length > 0) {
                                if (categoryChildren.every(c => c.completed)) {
                                    node.completed = true;
                                    changed = true;
                                }
                            } else {
                                if (node.id === "编程学习之旅") {
                                    node.completed = true;
                                    changed = true;
                                }
                            }
                        }
                    });
                    if (!changed) break;
                }
                
                const rootNode = nodeMap.get("编程学习之旅");
                if (rootNode) {
                    rootNode.completed = true;
                    rootNode.unlocked = true;
                }

                for (let i = 0; i < 5; i++) {
                    allNodes.forEach(node => {
                        if (!node.unlocked) {
                            if (node.parents.length === 0) {
                                node.unlocked = true;
                            } else {
                                const parent = nodeMap.get(node.parents[0]);
                                if (parent) {
                                    if (node.qListId > 0) {
                                        if (parent.unlocked) node.unlocked = true;
                                    } else {
                                        if (parent.id === "编程学习之旅") {
                                            node.unlocked = true;
                                        } else if (parent.completed) {
                                            node.unlocked = true;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }

                allNodes.forEach(node => {
                    if (node.completed) {
                        summary.completedCount++;
                        summary.completedNodes.push(node.id);
                    }
                    summary.totalNodes++;
                });

                allNodes.forEach(node => {
                    if (node.qListId > 0 && node.unlocked && !node.completed) {
                        let label = node.id;
                        if (node.parents && node.parents.length > 0) {
                            const parentId = node.parents.find(p => !p.endsWith('*') && p !== "编程学习之旅");
                            if (parentId) {
                                label = `${parentId} > ${node.id}`;
                            }
                        }
                        summary.zpdNodes.push({ id: node.id, label: label });
                    } else if (!node.unlocked) {
                        summary.lockedNodes.push(node.id);
                    }
                });
                
                summary.zpdNodeIds = summary.zpdNodes.map(n => n.id);
                
                if (summary.totalNodes > 0) {
                    summary.totalProgress = Math.round((summary.completedCount / summary.totalNodes) * 100);
                }
            }
        } catch (e) {
            console.error("获取进度摘要失败:", e);
        }

        return summary;
    }

    getAiChatHtml(webview) {
        const aiHtmlPath = path.join(this.provider._extensionUri.fsPath, 'media', 'AIAssistant', 'ai-assistant.html');
        let html = fs.readFileSync(aiHtmlPath, 'utf8');

        const scriptUri = webview.asWebviewUri(
            vscode.Uri.joinPath(this.provider._extensionUri, 'media', 'AIAssistant', 'ai-assistant.js')
        );

        html = html.replace('<!--SCRIPT_PLACEHOLDER-->', `<script type="module" src="${scriptUri}"></script>`);

        return html;
    }
}

module.exports = { AIAssistantLogic };
