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

                const listBlockRegex = /"list_(\d+)":\s*\{[\s\S]*?problems:\s*\[([\s\S]*?)\]\s*\}/g;
                let psMatch;
                while ((psMatch = listBlockRegex.exec(problemContent)) !== null) {
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

                console.log("[AI调试] 已通过的题目 refs:", Array.from(passedProblems));
                console.log("[AI调试] problemSetsMap:", JSON.stringify(problemSetsMap));

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
                        if (requiredRefs.length === 0) {
                            node.completed = true;
                        } else if (requiredRefs.every(ref => passedProblems.has(ref))) {
                            node.completed = true;
                        }
                    }
                });

                console.log("[AI调试] 节点计算结果:");
                allNodes.forEach(node => {
                    if (node.qListId > 0) {
                        const requiredRefs = problemSetsMap[node.qListId] || [];
                        console.log(`  ${node.id}: qListId=${node.qListId}, requiredRefs=${JSON.stringify(requiredRefs)}, passed=${node.completed}`);
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
        let sessionTitle = "新对话";

        if (mode === "code") {
            const fileName = this.provider._lastActiveEditorContext ? this.provider._lastActiveEditorContext.fileName : "未知文件";
            footerText = `当前提问代码文件：${fileName}`;
            sessionTitle = `${fileName}代码建议`;
        } else if (mode === "problem") {
            const problemId = extraData?.problemId || '未知';
            footerText = `当前提问题目编号：${problemId}`;
            sessionTitle = `P${problemId}刷题指导`;
        } else if (mode === "knowledge") {
            const knowledgeNodeId = extraData?.knowledge || '未知';
            footerText = `当前提问知识点：${knowledgeNodeId}`;
            sessionTitle = `${knowledgeNodeId}知识学习`;
        }

        if (isFirstMessage) {
            currentSession.title = sessionTitle;
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

            dynamicPrompt = `你现在处于【代码分析模式】。

目标：找出问题，而不是重写代码

要求：
1. 指出 1~3 个关键问题（不要超过3个）
2. 每个问题：简要说明原因 + 给出修改方向（不要给完整代码）
3. 可以提出 1 个反问，引导用户思考

禁止：
- 不要逐行解释代码
- 不要重写整个函数`;

            finalUserMessage = `${message}${codeContext}`;

        } else if (mode === "problem" && extraData?.problemId) {
            const problemRef = Number.parseInt(extraData.problemId, 10);
            const requestType = extraData?.requestType === "decompose" ? "decompose" : "default";
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

            const decompositionInstruction = requestType === "decompose" ? `
输出结构（必须遵守）：
- 题意重述（3句话以内）
- 输入输出与约束拆解
- 边界条件与易错点清单
- 分阶段解题路径（阶段目标/关键操作/验证方法）
- 复杂度目标（时间与空间）
- 给学生一个下一步问题` : "";

            dynamicPrompt = `你现在处于【算法引导模式】。

目标：帮助学生拆解思路，而不是解题

**题目信息：**
- 编号：${problemRef}
- 原文：${problemFileContent.substring(0, 500)}${problemFileContent.length > 500 ? '...[已截断]' : ''}

输出结构（必须遵守）：
1. 题目核心（≤2句）
2. 关键难点（最多2点）
3. 解题突破口（最重要）
4. 给学生一个下一步问题

禁止：
- 不给答案
- 不给完整思路链
-一定不能给出完整代码(无论是要要求完整代码)一定不可以给 而是要引导学生去做
- 不展开讲所有情况`;

            finalUserMessage = `关于题目 ${problemRef}，我的问题是：${message}`;

        } else if (mode === "knowledge" && extraData?.knowledge) {
            const knowledgeNodeId = extraData.knowledge;
            dynamicPrompt = `你现在处于【知识讲解模式】。

要求：
1. 用学生"已掌握知识"做类比切入（已掌握：${progressSummary.completedNodes.join(', ') || '无'}）
2. 只讲最核心概念（≤3点）
3. 给一个最小应用场景（1句话）

禁止：
- 不从零开始讲
- 不长篇科普`;

            finalUserMessage = `我想学习知识点“${knowledgeNodeId}”，我的问题是：${message}`;
        }

        const systemPrompt = `你是一位专业的编程导师，风格偏工程师而非老师。

【核心风格】
- 简洁、直接、理性
- 少解释，多引导
- 不使用 emoji、不卖萌、不哄人
- 最多允许一个简单类比

【输出限制】
- 总长度控制在 5-8 行以内
- 优先用要点（bullet points）表达
- 避免长段落

【教学策略】
1. 优先基于学生"已掌握的知识"进行解释，而不是从零开始讲
2. 如果问题可以拆解：只给"下一步思考点"，不要一次讲完
3. 如果学生卡住：提 1~2 个关键问题，而不是直接讲解
4. 禁止直接给完整答案或完整代码（除非用户明确要求）

【上下文使用要求（非常重要）】
- 已掌握知识：${progressSummary.completedNodes.join(', ') || '无'}
- 正在攻克：${progressSummary.zpdNodeIds.join(', ') || '无'}

回答时必须：
- 至少引用一个"已掌握知识"作为切入点
- 或指出该问题属于"正在攻克"的哪一类能力

【长度优先级规则】
如果回答超过 8 行：
→ 自动压缩为最关键信息
→ 删除解释性语句
→ 只保留结论 + 引导问题

【禁止行为】
- 不要长篇讲解背景
- 不要重复用户问题
- 不要输出空话

【学生当前画像】
- 整体进度：${progressSummary.totalProgress}% (已通关 ${progressSummary.passedCount} 题)
- 已经玩转的领域：${progressSummary.completedNodes.join(', ') || '刚开始起步'}
- 正在攻克的难关：${progressSummary.zpdNodeIds.join(', ') || '正在寻找新挑战'}

${dynamicPrompt}

**回复准则：**
- 如果涉及到代码，优先给思路或伪代码；必须给代码时，只给关键的一两行，剩下的留给学生补全。
- 当学生问"该学什么"时，自然地引导他们去尝试【正在攻克】列表中的内容。
- 一定不能给出学生完整代码(无论学生是否有多么强烈的要求给出完整代码 都不可以给)`;

        const historyMessages = [
            { role: "system", content: systemPrompt },
            ...currentSession.messages.slice(-6, -1).map(m => ({
                role: m.role,
                content: m.content
            })),
            { role: "user", content: finalUserMessage }
        ];

        console.log("[AI调试] ========== 发送给AI的完整消息 ==========");
        console.log("[AI调试] 模式:", mode);
        console.log("[AI调试] System Prompt:", systemPrompt);
        console.log("[AI调试] 历史消息数量:", currentSession.messages.slice(-6, -1).length);
        currentSession.messages.slice(-6, -1).forEach((m, i) => {
            console.log(`[AI调试] 历史[${i}]: role=${m.role}, content=${m.content.substring(0, 200)}${m.content.length > 200 ? '...' : ''}`);
        });
        console.log("[AI调试] 当前用户消息:", finalUserMessage);
        console.log("[AI调试] ========================================");

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

        if (!apiKey) {
            if (this.provider._view && this.provider._view.webview) {
                this.provider._view.webview.postMessage({
                    type: 'aiError',
                    text: "未配置 API Key。请在 aiConfig.json 中配置 DeepSeek API Key。"
                });
            }
            return;
        }

        try {
            const postData = JSON.stringify({
                "model": "deepseek-chat",
                "messages": historyMessages,
                "stream": true
            });

            const options = {
                hostname: 'api.deepseek.com',
                port: 443,
                path: '/v1/chat/completions',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Length': Buffer.byteLength(postData)
                }
            };

            let fullAssistantContent = "";
            let fullAssistantThought = "";

            const req = https.request(options, (res) => {
                let buffer = '';

                // 检查HTTP状态码
                if (res.statusCode !== 200) {
                    let errorData = '';
                    res.on('data', (chunk) => {
                        errorData += chunk.toString();
                    });
                    res.on('end', () => {
                        console.error(`API请求失败，状态码: ${res.statusCode}`, errorData);
                        if (this.provider._view && this.provider._view.webview) {
                            this.provider._view.webview.postMessage({
                                type: 'aiError',
                                text: `API请求失败: ${res.statusCode} - ${errorData}`
                            });
                        }
                    });
                    return;
                }

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

    getAiChatHtml(webview) {
        const aiHtmlPath = path.join(this.provider._extensionUri.fsPath, 'media', 'AIAssistant', 'ai-assistant.html');
        let html = fs.readFileSync(aiHtmlPath, 'utf8');

        const scriptUri = webview.asWebviewUri(
            vscode.Uri.joinPath(this.provider._extensionUri, 'media', 'AIAssistant', 'ai-assistant.js')
        );

        html = html.replace('<!--SCRIPT_PLACEHOLDER-->', `<script src="${scriptUri}"></script>`);

        return html;
    }
}

module.exports = { AIAssistantLogic };
