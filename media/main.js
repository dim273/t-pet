const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";
function generateResources() {
    vscode.postMessage({ type: 'generateResources' });
}

function removeResources() {
    vscode.postMessage({ type: 'removeResources' });
}

function switchPageToMain() {
    vscode.postMessage({ type: 'switchPageToMain' });
}

function sendCommand(type, data) {
    window.top.postMessage({ type, data }, MainOrigin);
}

function openAutoLodash() {
    sendCommand('live2d-openAutoLodash');
}
function closeAutoLodash() {
    sendCommand('live2d-closeAutoLodash');
}
function lodashLive2d() {
    sendCommand('live2d-lodash');
}
function closeLive2d() {
    sendCommand('live2d-close');
}
function saveCurrentConfig() {
    sendCommand('live2d-saveCurrentConfig');
}
function resetPosition() {
    sendCommand('live2d-resetPosition');
}



