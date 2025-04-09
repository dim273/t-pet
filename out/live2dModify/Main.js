"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Main = void 0;
const vscode = require("vscode");
const path = require("path");
const version_1 = require("./version");
const Dom_1 = require("./Dom");
const vscode_1 = require("vscode");
class Main {
    static watch() {
        const base = vscode_1.env.appRoot;
        const filePath = path.join(base, 'out', 'vs', 'code', 'electron-sandbox', 'workbench', 'workbench.js');
        const configName = 'vscode-live2d-asoul';
        const extName = "TheSecondAkari-vscode-live2d";
        let DomApi = new Dom_1.Dom(configName, filePath, version_1.default, extName);
        Main.Instance = DomApi;
        return vscode.workspace.onDidChangeConfiguration(() => DomApi.install());
    }
}
exports.Main = Main;
