"use strict";
// Object.defineProperty(exports, "__esModule", { value: true });
exports.activateModify = activateModify;
exports.deactivateModify = deactivateModify;
const Main_1 = require("./Main");
function activateModify(context) {
    context.subscriptions.push(Main_1.Main.watch());
}
function deactivateModify() { }
