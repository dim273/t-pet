"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const live2dView_1 = require("./live2dView");
const live2dModify_1 = require("./live2dModify");

function activate(context) {
	// 注册live2d窗口
	(0, live2dView_1.activateLive2d)(context);
	// 注册live2d修改器
	(0, live2dModify_1.activateModify)(context);
}

function deactivate() { }

