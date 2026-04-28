const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";

function sendCommand(type, data) {
    window.top.postMessage({ type, data }, MainOrigin);
}

function openAutoLodash() {
    sendCommand('live2d-openAutoLodash');
}
function closeAutoLodash() {
    sendCommand('live2d-closeAutoLodash');
}


// 生成依赖
function generateResources() {
    vscode.postMessage({ type: 'generateResources' });
}

// 移除依赖
function removeResources() {
    vscode.postMessage({ type: 'removeResources' });
}

// 返回
function switchPageToMain() {
    vscode.postMessage({ type: 'switchPageToMain' });
}

// 退出登陆
function logout() {
    vscode.postMessage({ type: 'switchPageToLogin' });
}

// 开启live2d
function lodashLive2d() {
    sendCommand('live2d-lodash');
}

// 关闭live2d
function closeLive2d() {
    sendCommand('live2d-close');
}

// 保存配置
function saveCurrentConfig() {
    sendCommand('live2d-saveCurrentConfig');
}

// 复原配置
function resetPosition() {
    sendCommand('live2d-resetPosition');
}

// 自启动开
function openAutoLodash() {
    sendCommand('live2d-openAutoLodash');
}

// 自启动关
function closeAutoLodash() {
    sendCommand('live2d-closeAutoLodash');
}

function saveDeepseekConfig() {
    const apiKey = document.getElementById('deepseekApiKey')?.value || "";
    const model = document.getElementById('deepseekModel')?.value || "deepseek-v4-pro";
    vscode.postMessage({
        type: 'saveDeepseekConfig',
        data: { apiKey, model }
    });
}

function testDeepseekConnection() {
    const apiKey = document.getElementById('deepseekApiKey')?.value || "";
    if (!apiKey) {
        alert("请先输入 API Key");
        return;
    }
    vscode.postMessage({
        type: 'testDeepseekConnection',
        data: { apiKey }
    });
}

window.addEventListener('DOMContentLoaded', () => {
    vscode.postMessage({ type: 'getDeepseekConfig' });
});

window.addEventListener('message', event => {
    const msg = event.data;
    if (msg.type === 'saveSuccess') {
        alert("保存成功！");
    } else if (msg.type === 'testSuccess') {
        alert("连接成功！");
    } else if (msg.type === 'testError') {
        alert("连接失败：" + msg.error);
    } else if (msg.type === 'loadDeepseekConfig') {
        const { apiKey, model } = msg.data || {};
        const apiKeyInput = document.getElementById('deepseekApiKey');
        const modelSelect = document.getElementById('deepseekModel');
        if (apiKeyInput) apiKeyInput.value = apiKey || "";
        if (modelSelect) modelSelect.value = model || "deepseek-v4-pro";
    }
});
