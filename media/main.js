const vscode = acquireVsCodeApi();

function generateResources() {
    vscode.postMessage({ type: 'generateResources' });
}

function removeResources() {
    vscode.postMessage({ type: 'removeResources' });
}

function switchPageToMain() {
    vscode.postMessage({ type: 'switchPageToMain' });
}

function logout() {
    vscode.postMessage({ type: 'switchPageToLogin' });
}

function lodashLive2d() {
    vscode.postMessage({ type: 'live2d-lodash' });
}

function closeLive2d() {
    vscode.postMessage({ type: 'live2d-close' });
}

function saveCurrentConfig() {
    vscode.postMessage({ type: 'live2d-saveCurrentConfig' });
}

function resetPosition() {
    vscode.postMessage({ type: 'live2d-resetPosition' });
}

function openAutoLodash() {
    vscode.postMessage({ type: 'live2d-openAutoLodash' });
}

function closeAutoLodash() {
    vscode.postMessage({ type: 'live2d-closeAutoLodash' });
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
