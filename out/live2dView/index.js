"use strict";
// 设置模块导出标记
Object.defineProperty(exports, "__esModule", { value: true });
exports.activateLive2d = activateLive2d;

// 导入 VSCode API和自定义模块
const vscode = require("vscode");
const Main_1 = require("../live2dModify/Main");
const fs = require('fs');
const path = require('path');
const https = require('https');
const { FileStorage } = require('../../manager/fileStorage');
const { AIAssistantLogic } = require('../AIAssistant/logic');
const { console } = require("inspector");

// 扩展激活入口函数
function activateLive2d(context) {
	// 创建 Webview 视图提供者
	const provider = new Live2dViewProvider(context.extensionUri);
	// 注册 Webview 视图
	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(Live2dViewProvider.viewType, provider)
	);
}

// Webview视图提供者类
class Live2dViewProvider {
	constructor(_extensionUri) {
		this._extensionUri = _extensionUri;  // 扩展安装目录URI
		this._page = 'login';                // 当前页面状态，初始化为登陆界面

		// 初始化文件存储管理器和账号信息
		this.storage = new FileStorage(_extensionUri);
		this._currentAccountId = 0;
		this.saveData = {
			id: 1,
			name: "错误警告账号",
			platforms: {
				leetcode: true,
				luogu: true,
				github: true
			},
			lastLogin: "2025-02-05",
			checkInDays: {}
		};

		// --- 代码建议上下文追踪 ---
		this._lastActiveEditorContext = null;
		this.aiLogic = new AIAssistantLogic(this);

		// 初始化当前活动的编辑器
		this.aiLogic.updateLastActiveContext(vscode.window.activeTextEditor);
		// 监听编辑器切换
		vscode.window.onDidChangeActiveTextEditor(editor => {
			this.aiLogic.updateLastActiveContext(editor);
		});
		// 监听选区变化
		vscode.window.onDidChangeTextEditorSelection(event => {
			this.aiLogic.updateLastActiveContext(event.textEditor);
		});
	}

	// 解析 Webview 视图
	resolveWebviewView(webviewView, context, _token) {
		// 保存 Webview 实例引用
		this._view = webviewView;
		this._history = []; // 初始化
		this._page = 'login'; // 默认起始页
		// 配置 Webview 选项
		webviewView.webview.options = {
			enableScripts: true,  // 允许执行脚本
			localResourceRoots: [this._extensionUri],  // 允许加载的资源路径
		};

		// 设置 HTML 内容
		webviewView.webview.html = this.updateWebviewContent(webviewView.webview);

		// 处理来自 Webview 的消息
		webviewView.webview.onDidReceiveMessage(async (data) => {
			switch (data.type) {
				case "judge":
					console.log("收到评测请求, ref=", data.ref);

					try {
						const results = await this._judgeProblem(data.ref);
						webviewView.webview.postMessage({
							type: "judgeResult",
							results: results
						});

					} catch (err) {
						console.error("评测异常:", err);
						webviewView.webview.postMessage({
							type: "judgeResult",
							results: [{ id: "0", status: "RE", got: String(err) }]
						});
					}
					break;
				// 切换页面
				case "switchPageToMain":
					this._history.push(this._page); // <-- 保存当前页
					this._page = 'main';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToProblemList":
					this._history.push(this._page);
					this._page = 'list';
					this._currentProblemListId = data.listId || 1;
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToProblem":
					const problemFilePath = path.join(this._extensionUri.fsPath, "res", "Problem", `${data.ref}.md`);
					if (fs.existsSync(problemFilePath)) {
						this._history.push(this._page);
						this._page = 'problem';
						this._currentProblemRef = data.ref;
						this._currentProblemTitle = data.title;
						webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					} else {
						vscode.window.showErrorMessage(`无法打开题目：找不到文件 ${data.ref}.md`);
					}
					break;
				case "switchPageToReProblemList":
					this._history.push(this._page);
					this._page = 'Reproblem';
					this._currentProblemListId = data.listId || 1;
					this._view.webview.html = this._getRecommendProblemListHtml(this._view.webview);
					break;
				case "switchPageToLogin":
					this._history.push(this._page);
					this._page = 'login';

					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageTotree":
					this._history.push(this._page);
					this._page = 'tree';
					this._currentSubTree = null; // 重置当前子树
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchToSubTree":
					// 切换到指定的子树
					this._currentSubTree = data.subTreeId;
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToCalender":
					this._history.push(this._page);
					this._page = 'calender';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);

					// 加载日历数据并在DOMContentLoaded后发送
					const calenderData = this.saveData.checkInDays;
					if (this._view && this._view.webview) {
						this._view.webview.postMessage({
							type: 'loadCalenderData',
							data: calenderData
						});
					}
					break;
				case "switchPageToSetting":
					this._history.push(this._page);
					this._page = 'setting';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToAbilityMap":
					this._history.push(this._page);
					this._page = 'abilityMap';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToAiChat":
					this._history.push(this._page);
					this._page = 'aiChat';
					if (data.bootstrap) {
						if (Number.isInteger(Number.parseInt(data.bootstrap.problemId, 10))) {
							const safeProblemId = Number.parseInt(data.bootstrap.problemId, 10);
							this._aiBootstrap = {
								mode: "problem",
								requestType: data.bootstrap.requestType === "decompose" ? "decompose" : "default",
								problemId: safeProblemId
							};
						} else if (data.bootstrap.mode === "knowledge" && data.bootstrap.knowledgeName) {
							this._aiBootstrap = {
								mode: "knowledge",
								knowledgeName: data.bootstrap.knowledgeName
							};
						} else {
							this._aiBootstrap = null;
						}
					} else {
						this._aiBootstrap = null;
					}
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					if (!this.saveData.aiHistory || !this.saveData.aiHistory.currentSessionId ||
						(this.saveData.aiHistory.sessions.find(s => s.id === this.saveData.aiHistory.currentSessionId)?.messages.length > 0)) {
						this.aiLogic.handleCreateNewAiSession();
					} else {
						this.aiLogic.handleLoadAiHistory();
					}
					break;
				case "goBack":
					if (this._history.length > 0) {
						this._page = this._history.pop();
						webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					}
					break;

				/*----------------------- 资源管理----------------------------- */
				case "generateResources":
					// 生成资源文件
					Main_1.Main.Instance && Main_1.Main.Instance.generateResources();
					break;
				case "removeResources":
					// 移除资源文件
					Main_1.Main.Instance && Main_1.Main.Instance.removeResources(true);
					break;
				case "selectAccount":
					// 处理选择账号
					this._currentAccountId = data.accountId;
					this.saveData = this.storage.getAccountByIndex(data.accountId) || this.saveData;
					if (!this.saveData.progress) {
						this.saveData.progress = { passedProblems: [] };
					}
					this.saveData.lastLogin = new Date().toLocaleDateString('zh-CN');
					this.storage.updateAccountByIndex(data.accountId, this.saveData);
					break;
				case "problemPassed":
					// 处理题目完成
					if (!this.saveData.progress) {
						this.saveData.progress = { passedProblems: [] };
					}
					const problemRef = data.ref;
					if (!this.saveData.progress.passedProblems.includes(problemRef)) {
						this.saveData.progress.passedProblems.push(problemRef);
						this.storage.updateAccountByIndex(this._currentAccountId, this.saveData);
						vscode.window.showInformationMessage(`恭喜！你已完成题目 #${problemRef}`);
					}
					break;
				case "deleteAccount":
					// 处理删除账号
					this.storage.deleteAccountByIndex(data.accountId);
					break;
				case "addAccount":
					// 处理添加账号
					this.storage.addAccount(data.account);
					break;
				case "saveCalenderData":
					// 处理日历打卡数据
					this.saveData.checkInDays = data.data;
					this.storage.updateAccountByIndex(this._currentAccountId, this.saveData);
					break;
				case "openDataFolder":
					// 打开数据文件夹
					this.openDataFolder();
					break;
				case "aiRequest":
					this.aiLogic.handleAiRequest(data.payload);
					break;
				case "loadAiHistory":
					this.aiLogic.handleLoadAiHistory();
					break;
				case "switchAiSession":
					this.aiLogic.handleSwitchAiSession(data.sessionId);
					break;
				case "createNewAiSession":
					this.aiLogic.handleCreateNewAiSession();
					break;
				case "deleteAiSession":
					this.aiLogic.handleDeleteAiSession(data.sessionId);
					break;
				case "saveDeepseekConfig":
					this._saveDeepseekConfig(data.data);
					break;
				case "testDeepseekConnection":
					this._testDeepseekConnection(data.data.apiKey);
					break;
				case "getDeepseekConfig":
					this._getDeepseekConfig();
					break;

			}
		});
	}

	/**
	 * 获取 DeepSeek 配置并发送到 Webview
	 */
	_getDeepseekConfig() {
		const config = vscode.workspace.getConfiguration('t-pet');
		const apiKey = config.get('deepseekApiKey') || "";
		const model = config.get('deepseekModel') || "deepseek-v4-pro";
		this._view.webview.postMessage({
			type: 'loadDeepseekConfig',
			data: { apiKey, model }
		});
	}

	/**
	 * 保存 DeepSeek 配置到 VSCode 全局配置
	 */
	async _saveDeepseekConfig(data) {
		try {
			const config = vscode.workspace.getConfiguration('t-pet');
			await config.update('deepseekApiKey', data.apiKey, vscode.ConfigurationTarget.Global);
			await config.update('deepseekModel', data.model, vscode.ConfigurationTarget.Global);
			this._view.webview.postMessage({ type: 'saveSuccess' });
		} catch (error) {
			vscode.window.showErrorMessage('保存配置失败: ' + error.message);
		}
	}

	/**
	 * 测试 DeepSeek API 连接
	 */
	async _testDeepseekConnection(apiKey) {
		if (!apiKey) {
			this._view.webview.postMessage({ type: 'testError', error: '请先输入 API Key' });
			return;
		}

		try {
			const https = require('https');
			const postData = JSON.stringify({
				"model": "deepseek-v4-flash",
				"messages": [{ role: "user", content: "Hi" }],
				"thinking": {"type": "disabled"},
				"stream": false
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

			const req = https.request(options, (res) => {
				let data = '';
				res.on('data', (chunk) => data += chunk);
				res.on('end', () => {
					if (res.statusCode === 200) {
						this._view.webview.postMessage({ type: 'testSuccess' });
					} else {
						this._view.webview.postMessage({ type: 'testError', error: `状态码 ${res.statusCode}` });
					}
				});
			});

			req.on('error', (e) => {
				this._view.webview.postMessage({ type: 'testError', error: e.message });
			});

			req.write(postData);
			req.end();
		} catch (error) {
			this._view.webview.postMessage({ type: 'testError', error: error.message });
		}
	}

	/**
	 * 异步生成会话标题
	 */
	async _generateSessionTitle(sessionId, userMessage, aiResponse) {
		return this.aiLogic.generateSessionTitle(sessionId, userMessage, aiResponse);
	}

	_saveAssistantMessageToHistory(content, thought) {
		return this.aiLogic.saveAssistantMessageToHistory(content, thought);
	}

	_handleLoadAiHistory() {
		return this.aiLogic.handleLoadAiHistory();
	}

	_handleSwitchAiSession(sessionId) {
		return this.aiLogic.handleSwitchAiSession(sessionId);
	}

	_handleCreateNewAiSession() {
		return this.aiLogic.handleCreateNewAiSession();
	}

	_handleDeleteAiSession(sessionId) {
		return this.aiLogic.handleDeleteAiSession(sessionId);
	}

	/**
	 * 获取学习进度摘要，包括知识树完成情况和最近发展区 (ZPD)
	 */
	_getLearningProgressSummary() {
		return this.aiLogic.getLearningProgressSummary();
	}

	updateWebviewContent(webview) {
		switch (this._page) {
			case 'main':
				return this._getMainHtml(webview);
			case 'list':
				return this._getProblemListHtml(webview);
			case 'problem':
				return this._getProblemHtml(webview);
			case 'login':
				return this._getLoginHtml(webview);
			case 'calender':
				return this._getCalenderHtml(webview);
			case 'tree':
				return this._getTreeHtml(webview);
			case 'aiChat':
				return this._getAiChatHtml(webview);
			case 'Reproblem':
				return this._getRecommendProblemListHtml(webview);
			case 'abilityMap':
				return this._getAbilityMapHtml(webview);
			default:
				return this._getSettingHtml(webview);
		}
	}

	// 生成能力图谱界面
	_getAbilityMapHtml(webview) {
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const abilityCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "AbilityMap", "ability.css"));
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "data.js"));
		const problemListDataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "data.js"));
		const abilityCalculatorUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "AbilityMap", "ability.js"));
		const abilityHtmlPath = path.join(this._extensionUri.fsPath, "media", "AbilityMap", "ability.html");
		const htmlContent = fs.readFileSync(abilityHtmlPath, 'utf8');

		const logoUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "logo.png"));
		let result = htmlContent.replace(/{{logo}}/g, logoUri.toString());
		result = result.replace('</head>', `<link rel="stylesheet" href="${variablesCssUri}">\n<link rel="stylesheet" href="${baseCssUri}">\n<link rel="stylesheet" href="${abilityCssUri}">\n</head>`);

		const passedProblems = this.saveData.progress ? this.saveData.progress.passedProblems : [];

		return `<!DOCTYPE html>
		<html lang="zh-CN">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<link rel="stylesheet" href="${variablesCssUri}">
			<link rel="stylesheet" href="${baseCssUri}">
			<link rel="stylesheet" href="${abilityCssUri}">
			<link rel="stylesheet" href="${vscodeCssUri}">
			<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
			<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
		</head>
		<body>
			<div class="header">
        <button class="tp-back-btn" id="backButton"><i class="fa fa-arrow-left"></i></button>
        <h3 class="tp-page-title">能力图谱</h3>
    	</div>
			${result}
			<script src="${dataUri}"></script>
			<script src="${problemListDataUri}"></script>
			<script src="${abilityCalculatorUri}"></script>
			<script>
				window.passedProblems = ${JSON.stringify(passedProblems)};
				window.problemSets = problemSets;
				window.treeData = treeData;
				window.onload = function () {
					if (window.abilityMap && window.abilityMap.init) {
						window.abilityMap.init();
					}
				};
			</script>
		</body>
		</html>`;
	}
	//评测逻辑
	async _judgeProblem(ref) {
		console.log(`[judgeProblem] ref=${ref}`);

		const editor = vscode.window.activeTextEditor;
		if (!editor) {
			vscode.window.showErrorMessage("没有打开任何代码文件");
			return "RE";
		}

		const userFile = editor.document.fileName;
		const ext = path.extname(userFile).toLowerCase();

		const judgePath = path.join(this._extensionUri.fsPath, "res", "JudgeData", `P${ref}`, "tests");
		if (!fs.existsSync(judgePath)) {
			console.log("找不到评测数据目录:", judgePath);
			return "RE";
		}

		const inFiles = fs.readdirSync(judgePath).filter(f => f.endsWith(".in"));
		if (inFiles.length === 0) {
			console.log("没有找到输入文件");
			return "RE";
		}

		for (const inFile of inFiles) {
			const base = inFile.replace(".in", "");
			const inputPath = path.join(judgePath, inFile);
			const outputPath = path.join(judgePath, `${base}.out`);

			if (!fs.existsSync(outputPath)) continue;

			const input = fs.readFileSync(inputPath, "utf8");
			const expected = fs.readFileSync(outputPath, "utf8").trim();

			try {
				let userOutput = "";

				if (ext === ".py") {
					userOutput = await this._runCommand(`python "${userFile}"`, input, 3000);
				} else if (ext === ".js") {
					userOutput = await this._runCommand(`node "${userFile}"`, input, 3000);
				} else if (ext === ".c" || ext === ".cpp") {
					const exeName = path.join(path.dirname(userFile), `${path.basename(userFile, ext)}.exe`);
					const compiler = ext === ".c" ? "gcc" : "g++";

					// 编译
					await this._runCommand(`${compiler} "${userFile}" -o "${exeName}"`, "", 5000);

					// 执行
					userOutput = await this._runCommand(`"${exeName}"`, input, 3000);
				} else {
					return "Unsupported";
				}

				userOutput = userOutput.trim();

				if (userOutput !== expected) {
					console.log(`[judgeProblem] 用例 ${base} WA`);
					console.log("userOutput:", userOutput);
					return "WA";  // 遇到 WA 立即返回
				}

			} catch (err) {
				console.log(`[judgeProblem] 用例 ${base} 异常:`, err);
				if (err === "Timeout") return "Timeout"; // 超时立即返回
				return "RE";  // 运行错误
			}
		}

		// 全部 AC
		return "AC";
	}

	// 执行命令函数，支持超时短路
	_runCommand(cmd, input, timeoutMs) {
		return new Promise((resolve, reject) => {
			const { spawn } = require("child_process");
			const child = spawn(cmd, [], { shell: true });

			let output = "";
			let finished = false;

			// 超时处理
			const timer = setTimeout(() => {
				if (!finished) {
					finished = true;
					try { child.kill("SIGKILL"); } catch { }
					reject("Timeout");  // <-- 注意这里改成 Timeout
				}
			}, timeoutMs);

			child.stdin.write(input);
			child.stdin.end();

			child.stdout.on("data", data => output += data.toString());
			child.stderr.on("data", data => console.error("[stderr]", data.toString()));

			child.on("close", code => {
				if (!finished) {
					finished = true;
					clearTimeout(timer);
					resolve(output);  // 即使 code !== 0 也先返回输出，由上层 judge 判定
				}
			});

			child.on("error", err => {
				if (!finished) {
					finished = true;
					clearTimeout(timer);
					reject(err.message);
				}
			});
		});
	}
	// 生成设置
	_getSettingHtml(webview) {
		const scriptUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "main.js"));
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const mainCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "main.css"));
		const buttonCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "button.css"));

		const nonce = getNonce();

		return `<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<link href="${variablesCssUri}" rel="stylesheet">
				<link href="${baseCssUri}" rel="stylesheet">
				<link href="${buttonCssUri}" rel="stylesheet">
				<link href="${mainCssUri}" rel="stylesheet">
				<link href="${vscodeCssUri}" rel="stylesheet">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
				<title>Live 2d</title>
			</head>
			<body>
				<div class="header">
        	<button class="tp-back-btn" onclick="switchPageToMain()"><i class="fa fa-arrow-left"></i></button>
        	<h3 class="tp-page-title">设置</h3>
    		</div>
				<div class="tp-settings-container">
					<div class="common-title">萌宠设置</div>
					<div class="common-subtitle">基本操作:</div>
					<div class="common-bar">
						<button class="common-button" onclick="lodashLive2d()">启动live2d</button>
						<button class="common-button" onclick="closeLive2d()">关闭live2d</button>
					</div>
					<div class="common-bar">
						<button
							title="将定位依赖,大小，位置等信息存储，下次启动自动生效"
							class="common-button"
							onclick="saveCurrentConfig()">
							保存当前配置
						</button>
						<button class="common-button" onclick="resetPosition()">重置默认位置</button>
					</div>
					<div class="common-bar">
						<button class="common-button common-button-danger" onclick="logout()">退出登录</button>
					</div>

					<div class="common-subtitle">配置信息:</div>
					<div class="common-subtitle">自启动:</div>
					<div class="common-bar" >
						<button class="common-button" onclick="openAutoLodash()">开启</button>
						<button class="common-button" onclick="closeAutoLodash()">关闭</button>
					</div>

					<div class="common-subtitle">插件依赖文件:</div>
					<div class="common-bar">
						<button
							title="插件依赖文件会在初次安装插件并启动时自动生成，点击该按钮可强制生成覆盖"
							class="common-button"
							onclick="generateResources()">
							生成
						</button>
						<button
							title="卸载该插件前，请先执行该操作。去除该插件造成的影响"
							class="common-button"
							onclick="removeResources()">
							移除
						</button>
					</div>
					<div class="common-subtitle">定时切换(分钟):</div>
					<div class="common-bar">
						<input class="tp-input" style="width: 30%" placeholder="默认30" type="number" onchange="handleChangeTime(event)" />
						<button class="common-button" style="width: 30%" onclick="openBackgroundSetTime()">开启</button>
						<button class="common-button" style="width: 30%" onclick="closeBackgroundSetTime()">关闭</button>
					</div>

					<div class="common-title" style="margin-top: var(--space-5);">AI助手配置</div>
					<div class="common-subtitle">API Key:</div>
					<div class="common-bar" style="flex-direction: column; align-items: stretch;">
						<input id="deepseekApiKey" class="tp-input" style="width: 100%; margin-bottom: var(--space-2);" type="password" placeholder="输入 DeepSeek API Key" />
						<div style="display: flex; gap: var(--space-2);">
							<button class="common-button" onclick="saveDeepseekConfig()">保存配置</button>
							<button class="common-button" onclick="testDeepseekConnection()">测试连接</button>
						</div>
					</div>
					<div class="common-subtitle">模型:</div>
					<div class="common-bar">
						<select id="deepseekModel" class="tp-input" style="width: 100%;">
							<option value="deepseek-v4-pro">deepseek-v4-pro</option>
							<option value="deepseek-v4-flash">deepseek-v4-flash</option>
						</select>
					</div>
					<div id="aiConfigStatus" class="common-subtitle" style="margin-top: var(--space-2); font-size: var(--text-xs);"></div>
				</div>

				<script nonce="${nonce}" src="${scriptUri}"></script>
			</body>
			</html>`;
	};

	// 生成Ai助手
	_getAiChatHtml(webview) {
		const aiHtmlPath = path.join(this._extensionUri.fsPath, 'media', 'AIAssistant', 'ai-assistant.html');
		let html = fs.readFileSync(aiHtmlPath, 'utf8');

		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const buttonCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "button.css"));
		const aiCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "AIAssistant", "ai-assistant.css"));

		html = html.replace('../styles/variables.css', variablesCssUri.toString());
		html = html.replace('../styles/base.css', baseCssUri.toString());
		html = html.replace('../styles/button.css', buttonCssUri.toString());
		html = html.replace('ai-assistant.css', aiCssUri.toString());

		const bootstrap = this._aiBootstrap ? {
			mode: this._aiBootstrap.mode,
			requestType: this._aiBootstrap.requestType,
			problemId: this._aiBootstrap.problemId,
			knowledgeName: this._aiBootstrap.knowledgeName
		} : null;

		const scriptUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, 'media', 'AIAssistant', 'ai-assistant.js')
		);

		html = html.replace(
			'<!--SCRIPT_PLACEHOLDER-->',
			`<script>window.__AI_BOOTSTRAP__ = ${JSON.stringify(bootstrap)};</script><script type="module" src="${scriptUri}"></script>`
		);

		return html;
	}

	// 生成主菜单
	_getMainHtml(webview) {
		const htmlPath = path.join(__dirname, '../../media/menu.html');
		let htmlContent = fs.readFileSync(htmlPath, 'utf8');

		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const buttonCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "button.css"));
		const menuCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "menu.css"));

		htmlContent = htmlContent.replace('styles/variables.css', variablesCssUri.toString());
		htmlContent = htmlContent.replace('styles/base.css', baseCssUri.toString());
		htmlContent = htmlContent.replace('styles/button.css', buttonCssUri.toString());
		htmlContent = htmlContent.replace('menu.css', menuCssUri.toString());

		const logoUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "logo.png")
		);
		htmlContent = htmlContent.replace(/{{logo}}/g, logoUri.toString());

		return htmlContent;
	}

	// 生成题单
	_getProblemListHtml(webview) {
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const listCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "list.css"));
		const styleCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "styles.css"));
		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "data.js"));
		const appUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "app.js"));
		let listTitle = 1;
		if (this._currentProblemListId)
			listTitle = this._currentProblemListId;

		const passedProblems = this.saveData.progress ? this.saveData.progress.passedProblems : [];

		return `
			<!DOCTYPE html>
			<html lang="zh-CN">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>算法题单</title>
				<link rel="stylesheet" href="${variablesCssUri}">
				<link rel="stylesheet" href="${baseCssUri}">
				<link rel="stylesheet" href="${listCssUri}">
				<link rel="stylesheet" href="${styleCssUri}">
				<link rel="stylesheet" href="${vscodeCssUri}">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
			</head>
			<body>
				<div class="header">
        	<button class="tp-back-btn" id="back-btn" onclick="switchPageToMain()"><i class="fa fa-arrow-left"></i></button>
        	<h3 class="tp-page-title" id="listTitle">知识树</h3>
        	<div class="tp-header-buttons">
        		<button id="aiLearnBtn" class="tp-header-btn tp-header-btn-primary">AI指导学习</button>
        	</div>
    		</div>

				<div class="stats">
					<div class="stat-item">
						<div class="stat-value" id="total-count">0</div>
						<div class="stat-label">总题目数</div>
					</div>
					<div class="stat-item">
						<div class="stat-value" id="passed-count">0</div>
						<div class="stat-label">已通过</div>
					</div>
					<div class="stat-item">
						<div class="stat-value" id="progress">0%</div>
						<div class="stat-label">完成进度</div>
					</div>
				</div>
				<div class="problem-list" id="problem-list">
				</div>
				<script src="${dataUri}"></script>
				<script src="${appUri}"></script>
				
				<script>
					window.currentListId = "${listTitle}";
					window.passedProblems = ${JSON.stringify(passedProblems)};
				</script>
			</body>

			</html>`
	}
	// 生成题目界面
	_getProblemHtml(webview) {
		const appUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemPage", "app.js"));
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const listCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "list.css"));
		const problemCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "problem.css"));
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const katex_min_css_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "katex.min.css")); // katex.min.css
		const katex_min_js_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "katex.min.js")); // katex.min.js
		const katex_auto_render_min_js_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "auto-render.min.js")); // auto-render.min.js

		let title = "整型与布尔型的转换";
		let ref = 1;
		let listId = 1;
		if (this._currentProblemRef) ref = this._currentProblemRef;
		if (this._currentProblemTitle) title = this._currentProblemTitle;
		if (this._currentProblemListId) listId = this._currentProblemListId;
		console.log("当前题单id", listId);

		const filePath = path.join(this._extensionUri.fsPath, "res", "Problem", `${ref}.md`);
		const fileContent = fs.readFileSync(filePath, 'utf8');

		return `<!DOCTYPE html>
			<html lang="zh-CN">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>题目</title>
				<link rel="stylesheet" href="${variablesCssUri}">
				<link rel="stylesheet" href="${baseCssUri}">
				<link rel="stylesheet" href="${listCssUri}">
				<link rel="stylesheet" href="${problemCssUri}">
				<link rel="stylesheet" href="${styleVSCodeUri}">
				<link rel="stylesheet" href="${katex_min_css_Uri}">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
				<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  			<script src="${katex_min_js_Uri}"></script>
  			<script src="${katex_auto_render_min_js_Uri}"></script>
			</head>

			<body>
				<div class="tp-problem-header">
					<button class="tp-back-btn" id="back-btn" onclick="switchPageToProblemList()"><i class="fa fa-arrow-left"></i></button>
					<h3 class="tp-problem-title" id="listTitle">题目</h3>
					<div class="tp-header-buttons">
						<button id="decomposeBtn" class="tp-header-btn tp-header-btn-primary">AI问题分解</button>
						<button id="completeBtn" class="tp-header-btn tp-header-btn-success" onclick="completeProblem()" style="display: none;">完成题目</button>
						<button id="judgeBtn" class="tp-header-btn tp-header-btn-info">评测</button>
					</div>
				</div>
				<div id="markdownDisplay"></div>
				<div id="judgeStatus" class="tp-judge-status"></div>
				<script>
					let markdownText = ${JSON.stringify(fileContent)};
					window.currentProblemTitle = "${title || "整型与布尔型的转换"}";
					window.currentProblemListID = "${listId || 1}";
					window.currentProblemRef = ${ref};
				</script>
				<script src="${appUri}"></script>
			</body>

			</html>`;
	}
	_getRecommendProblemListHtml(webview) {
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const listCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "list.css"));
		const styleCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "RecommendProblemList", "styles.css"));

		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "RecommendProblemList", "data.js"));
		const recommendationUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "RecommendProblemList", "recommendation.js"));
		const abilityCalculatorUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "AbilityMap", "ability.js"));

		const appUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "RecommendProblemList", "app.js"));
		const treeNodeDataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "data.js"));
		const passedProblems = this.saveData.progress ? this.saveData.progress.passedProblems : [];

		return `
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>推荐题单</title>
      <link rel="stylesheet" href="${variablesCssUri}">
      <link rel="stylesheet" href="${baseCssUri}">
      <link rel="stylesheet" href="${listCssUri}">
      <link rel="stylesheet" href="${styleCssUri}">
      <link rel="stylesheet" href="${vscodeCssUri}">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
    </head>
    <body>
      <div class="header">
        <button class="tp-back-btn" onclick="switchPageToMain()"><i class="fa fa-arrow-left"></i></button>
        <h3 id="listTitle">推荐题单</h3>
      </div>

      <div class="stats">
        <div class="stat-item">
          <div class="stat-value" id="total-count">0</div>
          <div class="stat-label">推荐题目数</div>
        </div>
        <div class="stat-item">
          <div class="stat-value" id="passed-count">0</div>
          <div class="stat-label">已通过</div>
        </div>
        <div class="stat-item">
          <div class="stat-value" id="progress">0%</div>
          <div class="stat-label">完成进度</div>
        </div>
      </div>

      <div class="problem-list" id="reproblem-list"></div>
		<script src="${treeNodeDataUri}"></script>
      <script src="${dataUri}"></script>
      <script src="${abilityCalculatorUri}"></script>
      <script src="${recommendationUri}"></script>

      <script>
        window.passedProblems = ${JSON.stringify(passedProblems)};
      </script>

      <script src="${appUri}"></script>
    </body>
    </html>
  `;
	}

	// 生成登录界面
	_getLoginHtml(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const loginCssPath = path.join(this._extensionUri.fsPath, "media", "Login", "login.css");
		const loginJsUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "Login", "login.js"));

		const leetcodeIcon = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "leetcode.png"));
		const luoguIcon = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "luogu.png"));
		const githubIcon = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "github.png"));
		const logoUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "logo.png"));
		const backgroundUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "image", "back.jpg"));

		let cssContent = fs.readFileSync(loginCssPath, 'utf8');
		cssContent = cssContent.replace(/{{logoUri}}/g, logoUri.toString())
			.replace(/{{backgroundUri}}/g, backgroundUri.toString());

		const accounts = this.storage.getAccounts();
		if (accounts.length === 0) console.log("账号列表为空");
		return `<!DOCTYPE html>
			<html lang="en">

			<head>
				<meta charset="UTF-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
				<link href="${variablesCssUri}" rel="stylesheet" />
				<link href="${styleVSCodeUri}" rel="stylesheet" />
				<style>
					${cssContent}
				</style>
			</head>

			<body>
				<div class="top-background"></div>

				<div class="logo-container">
					<div class="logo"></div>
					<div class="logo-method">智能助手</div>
				</div>

				<div class="login-card" id="accountList">
						<h2 style="text-align:center">本地账号</h2>
						<button id="createAccountBtn" class="button">新建账号</button>
					<div id="accountsContainer" class="accounts-container">
						<!-- 账号列表将在这里动态生成 -->
					</div>
				</div>

				<div class="divider"></div>
				<div class="alt-login-title">可关联平台</div>
				<div class="alt-login">
					<img src="${leetcodeIcon}" title="LeetCode" data-method="LeetCode" />
					<img src="${luoguIcon}" alt="洛谷" data-method="洛谷" />
					<img src="${githubIcon}" alt="github" data-method="github" />
				</div>

				<div class="bottom-options">
					<span id="importAccount">导入账号</span>
					<span id="exportAccount">帮助</span>
				</div>

				<div class="success-message" id="successMsg">操作成功</div>
				<script>
					// 加载账号信息
					let accounts = ${JSON.stringify(accounts)};
				</script>
				<script src="${loginJsUri}"></script>
			</body>

			</html>`;
	}

	// 生成题目树
	_getTreeHtml(webview) {
		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "data.js"));
		const logicUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "logic.js"));
		const problemDataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "data.js"));
		const styleCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "style.css"))
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"))
		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));

		let treeTitle = "知识树";
		if (this._currentSubTree) {
			treeTitle = this._currentSubTree;
		}

		const passedProblems = this.saveData.progress ? this.saveData.progress.passedProblems : [];

		return `
			<!DOCTYPE html>
			<html lang="zh-CN">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>知识树图谱</title>
				<link rel="stylesheet" href="${vscodeCssUri}">
				<link rel="stylesheet" href="${variablesCssUri}">
				<link rel="stylesheet" href="${baseCssUri}">
				<link rel="stylesheet" href="${styleCssUri}">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
			</head>

			<body>
				<div class="header">
        	<button class="tp-back-btn" id="back-btn" onclick="switchPageToMain()"><i class="fa fa-arrow-left"></i></button>
        	<h3 class="tp-page-title">${treeTitle}</h3>
    		</div>
				
			  <div class="spacer"></div>
				<div class="tech-tree-container">
					<div class="tech-tree" id="techTree">
					</div>
				</div>

				<script src="${dataUri}"></script>
				<script src="${problemDataUri}"></script>
				<script>
					// 设置当前子树ID
					window.currentSubTreeId = "${this._currentSubTree || "知识树"}";
					window.passedProblems = ${JSON.stringify(passedProblems)};
				</script>
				<script src="${logicUri}"></script>
			</body>

			</html>
		`
	}

	// 生成日历
	_getCalenderHtml(webview) {
		const calenderPath = path.join(__dirname, '../.././media/calender.html');

		const htmlContent = fs.readFileSync(calenderPath, 'utf8');

		const variablesCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "variables.css"));
		const baseCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "base.css"));
		const calenderCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "styles", "calender.css"));

		let result = htmlContent.replace('styles/variables.css', variablesCssUri.toString());
		result = result.replace('styles/base.css', baseCssUri.toString());
		result = result.replace('styles/calender.css', calenderCssUri.toString());

		return result;
	}

	// 打开数据文件夹
	openDataFolder() {
		try {
			// 获取数据文件夹路径
			const dataFolderPath = path.join(this._extensionUri.fsPath, 'saveData');

			// 检查文件夹是否存在
			if (fs.existsSync(dataFolderPath)) {
				vscode.commands.executeCommand('revealFileInOS', vscode.Uri.file(dataFolderPath));
			} else {
				// 如果文件夹不存在，创建它
				fs.mkdirSync(dataFolderPath, { recursive: true });
				vscode.commands.executeCommand('revealFileInOS', vscode.Uri.file(dataFolderPath));
			}
		} catch (error) {
			vscode.window.showErrorMessage(`打开数据文件夹失败: ${error.message}`);
		}
	}
}

Live2dViewProvider.viewType = "vscode-live2d.live2dView";
// 生成随机字符串用于 CSP（内容安全策略）
function getNonce() {
	let text = "";
	const possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	for (let i = 0; i < 32; i++) {
		text += possible.charAt(Math.floor(Math.random() * possible.length));
	}
	return text;
}
