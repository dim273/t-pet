const vscode = acquireVsCodeApi();

function goBack() {
    vscode.postMessage({ type: 'goBack' });
}

document.addEventListener('DOMContentLoaded', function () {
    // DOM元素
    const chatContainer = document.getElementById('chat-container');
    const chatContent = document.getElementById('chat-content');
    const initState = document.getElementById('init-state');
    const modeBtns = document.querySelectorAll('.mode-btn');
    const modeIndicator = document.getElementById('mode-indicator');
    const inputGroups = document.querySelectorAll('.input-group');
    const backBtn = document.getElementById('back-btn');

    // 发送按钮
    const sendCodeBtn = document.getElementById('send-code');
    const sendProblemBtn = document.getElementById('send-problem');
    const sendKnowledgeBtn = document.getElementById('send-knowledge');

    // 输入框
    const codeInput = document.getElementById('code-input');
    const problemIdInput = document.getElementById('problem-id');
    const problemInput = document.getElementById('problem-input');
    const knowledgeSelect = document.getElementById('knowledge-select');
    const knowledgeInput = document.getElementById('knowledge-input');

    // 侧边栏元素
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    const menuToggle = document.getElementById('menu-toggle');
    const sidebarClose = document.getElementById('sidebar-close');
    const newChatBtn = document.getElementById('new-chat-btn');
    const historyList = document.getElementById('history-list');

    // 初始设置指示器位置
    updateModeIndicator(document.querySelector('.mode-btn.active'));

    // 侧边栏控制
    menuToggle.addEventListener('click', () => {
        sidebar.classList.add('active');
        sidebarOverlay.style.display = 'block';
        // 打开侧边栏时加载历史
        vscode.postMessage({ type: 'loadAiHistory' });
    });

    const closeSidebar = () => {
        sidebar.classList.remove('active');
        sidebarOverlay.style.display = 'none';
    };

    sidebarClose.addEventListener('click', closeSidebar);
    sidebarOverlay.addEventListener('click', closeSidebar);

    newChatBtn.addEventListener('click', () => {
        vscode.postMessage({ type: 'createNewAiSession' });
        closeSidebar();
    });

    // 模式切换
    modeBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            // 更新按钮状态
            modeBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // 更新指示器位置
            updateModeIndicator(this);

            // 显示对应的输入区域
            const mode = this.dataset.mode;
            inputGroups.forEach(group => {
                group.classList.toggle('active', group.dataset.mode === mode);
            });
        });
    });

    function updateModeIndicator(btn) {
        const btnRect = btn.getBoundingClientRect();
        const containerRect = btn.parentElement.getBoundingClientRect();

        modeIndicator.style.width = `${btnRect.width}px`;
        modeIndicator.style.left = `${btnRect.left - containerRect.left}px`;
    }

    // 当前流式传输的状态
    let currentAssistantMessageEl = null;
    let currentThoughtText = "";
    let currentContentText = "";
    let lastRenderTime = 0;
    const RENDER_INTERVAL = 50; // 毫秒，控制渲染频率以提升性能

    // 处理来自扩展的消息
    window.addEventListener('message', event => {
        const message = event.data;
        switch (message.type) {
            case 'aiStreamChunk':
                if (!currentAssistantMessageEl) {
                    removeLoading();
                    currentAssistantMessageEl = createAssistantMessageElement();
                    chatContent.appendChild(currentAssistantMessageEl);
                    currentThoughtText = "";
                    currentContentText = "";
                }
                
                if (message.reasoning) {
                    currentThoughtText += message.reasoning;
                }
                if (message.content) {
                    currentContentText += message.content;
                }
                
                // 节流渲染
                const now = Date.now();
                if (now - lastRenderTime > RENDER_INTERVAL) {
                    updateAssistantDisplay(currentAssistantMessageEl, currentThoughtText, currentContentText);
                    lastRenderTime = now;
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }
                break;
                
            case 'aiStreamDone':
                // 最后强制渲染一次确保内容完整
                if (currentAssistantMessageEl) {
                    updateAssistantDisplay(currentAssistantMessageEl, currentThoughtText, currentContentText);
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }
                currentAssistantMessageEl = null;
                currentThoughtText = "";
                currentContentText = "";
                lastRenderTime = 0;
                
                // AI 完成输出后，检查并同步最后一条用户消息的脚注（如果是“正在读取...”状态）
                const messages = document.querySelectorAll('.message.user');
                if (messages.length > 0) {
                    const lastUserMsg = messages[messages.length - 1];
                    const footer = lastUserMsg.querySelector('.message-footer');
                    if (footer && footer.textContent.includes('正在读取...')) {
                        // 触发一次历史记录刷新，获取最终保存的文件名
                        setTimeout(() => {
                            vscode.postMessage({ type: 'loadAiHistory' });
                        }, 500);
                    }
                }
                break;

            case 'aiResponse':
                removeLoading();
                addMessage('assistant', message.text);
                break;
            case 'aiError':
                removeLoading();
                addMessage('assistant', `错误: ${message.text}`);
                break;
            case 'aiHistoryLoaded':
                renderHistoryList(message.history);
                renderCurrentSession(message.history);
                // 更新知识学习下拉框
                if (message.history && message.history.zpdNodes) {
                    updateKnowledgeSelect(message.history.zpdNodes);
                }
                break;
        }
    });

    function updateKnowledgeSelect(nodes) {
        if (!knowledgeSelect) return;
        
        // 保留第一个默认选项
        const firstOption = knowledgeSelect.options[0];
        knowledgeSelect.innerHTML = '';
        knowledgeSelect.appendChild(firstOption);
        
        if (nodes && nodes.length > 0) {
            nodes.forEach(node => {
                const option = document.createElement('option');
                option.value = node.id;
                option.textContent = node.label;
                knowledgeSelect.appendChild(option);
            });
        }
    }

    function renderHistoryList(history) {
        historyList.innerHTML = '';
        
        // 过滤掉没有消息的会话（除非是当前选中的空会话，但通常我们只想在记录里看到有内容的）
        const displaySessions = (history.sessions || []).filter(session => session.messages.length > 0);
        
        if (displaySessions.length === 0) {
            historyList.innerHTML = '<div style="padding: 20px; text-align: center; opacity: 0.5;">暂无历史记录</div>';
            return;
        }

        displaySessions.forEach(session => {
            const item = document.createElement('div');
            item.className = `history-item ${session.id === history.currentSessionId ? 'active' : ''}`;
            
            const title = document.createElement('div');
            title.className = 'history-title';
            title.textContent = session.title || '新对话';
            title.onclick = () => {
                vscode.postMessage({ type: 'switchAiSession', sessionId: session.id });
                closeSidebar();
            };

            const deleteBtn = document.createElement('div');
            deleteBtn.className = 'delete-session';
            deleteBtn.innerHTML = '&times;';
            deleteBtn.onclick = (e) => {
                e.stopPropagation();
                vscode.postMessage({ type: 'deleteAiSession', sessionId: session.id });
            };

            item.appendChild(title);
            item.appendChild(deleteBtn);
            historyList.appendChild(item);
        });
    }

    function renderCurrentSession(history) {
        const currentSession = history.sessions.find(s => s.id === history.currentSessionId);
        
        // 清空当前聊天
        chatContent.innerHTML = '';
        
        if (!currentSession || currentSession.messages.length === 0) {
            initState.classList.remove('hidden');
            chatContent.style.display = 'none';
            return;
        }

        initState.classList.add('hidden');
        chatContent.style.display = 'block';

        currentSession.messages.forEach(msg => {
            if (msg.role === 'user') {
                addMessage('user', msg.content, msg.time, null, msg.footer);
            } else {
                addMessage('assistant', msg.content, msg.time, msg.thought);
            }
        });
        
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function createAssistantMessageElement() {
        const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const messageEl = document.createElement('div');
        messageEl.className = 'message assistant';
        messageEl.innerHTML = `
            <div class="avatar">AI</div>
            <div class="message-content">
                <div class="name">编程助手</div>
                <div class="message-body"></div>
                <div class="timestamp">${timestamp}</div>
            </div>
        `;
        return messageEl;
    }

    function updateAssistantDisplay(el, thought, content) {
        const bodyEl = el.querySelector('.message-body');
        let html = "";
        
        if (thought) {
            const isStreaming = !content && currentAssistantMessageEl !== null;
            html += `
                <div class="thought-container ${isStreaming ? 'streaming' : 'expanded'}">
                    <div class="thought-header" onclick="this.parentElement.classList.toggle('expanded')">正在思考中...</div>
                    <div class="thought-content">${thought.trim().replace(/\n/g, '<br>')}</div>
                </div>`;
        }
        
        if (content) {
            // 清理内容中的多余首尾换行，防止 marked 产生空段落
            const cleanedContent = content.trimStart();
            if (window.marked && typeof window.marked.parse === 'function') {
                // 配置 marked 选项以减少不必要的换行
                html += window.marked.parse(cleanedContent, {
                    breaks: true,
                    gfm: true
                });
            } else {
                html += cleanedContent.replace(/\n/g, '<br>');
            }
        }
        
        bodyEl.innerHTML = html;
    }

    // 发送消息函数
    function sendMessage(type, message, extraData = {}) {
        // 隐藏初始状态
        if (!initState.classList.contains('hidden')) {
            initState.classList.add('hidden');
            chatContent.style.display = 'block';
        }

        // 构建脚注内容
        let footerText = "";
        if (type === 'code') {
            // 获取文件名（从 index.js 缓存中读取，这里前端暂时显示为“当前工作区”）
            footerText = "当前提问代码文件：正在读取...";
        } else if (type === 'problem') {
            footerText = `当前提问题目编号：${extraData.problemId || '未知'}`;
        } else if (type === 'knowledge') {
            footerText = `当前提问知识点：${extraData.knowledge || '未知'}`;
        }

        // 添加用户消息
        addMessage('user', message, null, null, footerText);

        // 添加加载状态
        addLoading();

        // 向扩展发送请求
        vscode.postMessage({
            type: 'aiRequest',
            payload: {
                mode: type,
                message: message,
                extraData: extraData,
                workspaceCode: type === 'code' ? document.getElementById('workspace-code').checked : false
            }
        });
    }

    function addMessage(sender, text, time = null, thought = null, footer = null) {
        const timestamp = time || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const name = sender === 'user' ? '您' : '编程助手';

        const messageEl = document.createElement('div');
        messageEl.className = `message ${sender}`;
        
        let formattedText = text;
        if (sender === 'assistant') {
            // 统一使用流式显示的更新逻辑来处理非流式消息
            const tempDiv = document.createElement('div');
            updateAssistantDisplay({ querySelector: () => tempDiv }, thought || "", text);
            formattedText = tempDiv.innerHTML;
        }

        let footerHtml = footer ? `<div class="message-footer">${footer}</div>` : "";

        messageEl.innerHTML = `
            <div class="avatar">${sender === 'user' ? 'U' : 'AI'}</div>
            <div class="message-content">
                <div class="name">${name}</div>
                <div class="message-body">${formattedText}</div>
                ${footerHtml}
                <div class="timestamp">${timestamp}</div>
            </div>
        `;

        chatContent.appendChild(messageEl);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function addLoading() {
        const loadingEl = document.createElement('div');
        loadingEl.id = 'ai-loading';
        loadingEl.className = 'message assistant';
        loadingEl.innerHTML = `
            <div class="avatar">AI</div>
            <div class="message-content">
                <div class="name">编程助手</div>
                <div class="message-body">正在思考中...</div>
            </div>
        `;
        chatContent.appendChild(loadingEl);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function removeLoading() {
        const loadingEl = document.getElementById('ai-loading');
        if (loadingEl) {
            loadingEl.remove();
        }
    }

    // 事件监听器
    sendCodeBtn.addEventListener('click', function () {
        const message = codeInput.value.trim();
        if (!message) return;

        sendMessage('code', message);
        codeInput.value = '';
    });

    sendProblemBtn.addEventListener('click', function () {
        const problemId = problemIdInput.value.trim();
        const message = problemInput.value.trim();
        if (!message) return;

        sendMessage('problem', message, { problemId });
        problemIdInput.value = '';
        problemInput.value = '';
    });

    sendKnowledgeBtn.addEventListener('click', function () {
        const knowledge = knowledgeSelect.value;
        const message = knowledgeInput.value.trim();
        if (!message && !knowledge) return;

        sendMessage('knowledge', message, { knowledge });
        knowledgeInput.value = '';
    });

    // 输入框回车支持
    const setupEnterKey = (input, btn) => {
        input.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                btn.click();
            }
        });
    };

    setupEnterKey(codeInput, sendCodeBtn);
    setupEnterKey(problemInput, sendProblemBtn);
    setupEnterKey(knowledgeInput, sendKnowledgeBtn);

    // 暴露 goBack 供全局调用
    window.goBack = goBack;

    // 初始化
    window.addEventListener('resize', () => {
        updateModeIndicator(document.querySelector('.mode-btn.active'));
    });

    // 初始加载历史记录
    vscode.postMessage({ type: 'loadAiHistory' });
});
