"use strict";
// 设置模块导出标记
Object.defineProperty(exports, "__esModule", { value: true });
exports.activateLive2d = activateLive2d;

// 导入 VSCode API和自定义模块
const vscode = require("vscode");
const Main_1 = require("../live2dModify/Main");
const fs = require('fs');
const path = require('path');
const { FileStorage } = require('../../manager/fileStorage');
const { fetchPage } = require('../../manager/GetluoguProblem');

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
		this._page = 'login';                // 当前页面状态，初始化为test5

		// 初始化文件存储管理器
		this.storage = new FileStorage(_extensionUri);
		this.saveData = {
			userInfo: {
				name: "张三",
				email: "zhangsan@example.com",
				department: "开发部"
			},
			checkIn: {
				checkInDays: []
			}
		};

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
		webviewView.webview.onDidReceiveMessage((data) => {
			switch (data.type) {
				// 切换页面
				case "switchPageToMain":
					this._history.push(this._page); // <-- 保存当前页
					this._page = 'main';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToProblemList":
					this._history.push(this._page);
					this._page = 'list';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToProblem":
					// 由于fetchPage是异步函数，需要等待它完成后再渲染页面
					fetchPage(data.id).then(() => {
						console.log('题目获取完成，开始渲染页面');
						this._history.push(this._page);
						this._page = 'problem';
						webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					});
					break;
				case "switchPageToLogin":
					this._history.push(this._page);
					this._page = 'login';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageTotree":
					this._history.push(this._page);
					this._page = 'tree';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToCalender":
					this._history.push(this._page);
					this._page = 'calender';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);

					// 加载日历数据并在DOMContentLoaded后发送
					const allData = this.storage.readData();
					const calenderData = allData.checkIn.checkInDays;
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
				case "switchPageToAiChat":
					this._history.push(this._page);
					this._page = 'aiChat';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "goBack":
					if (this._history.length > 0) {
						this._page = this._history.pop(); // 取出上一个页面
						webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					}
					break;
				case "generateResources":
					// 生成资源文件
					Main_1.Main.Instance && Main_1.Main.Instance.generateResources();
					break;
				case "removeResources":
					// 移除资源文件
					Main_1.Main.Instance && Main_1.Main.Instance.removeResources(true);
					break;
				// 处理日历打卡数据
				case "saveCalenderData":
					this.saveData.checkIn.checkInDays = data.data;
					this.storage.saveData(this.saveData);
					break;
			}
		});
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
			default:
				return this._getSettingHtml(webview);
		}
	}

	// 生成设置
	_getSettingHtml(webview) {
		const scriptUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "main.js"));
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const styleMainUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "main.css"));

		// 生成随机数用于 CSP 安全策略
		const nonce = getNonce();

		// 返回 HTML 模板
		return `<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<link href="${styleVSCodeUri}" rel="stylesheet"> 
				<link href="${styleMainUri}" rel="stylesheet">
				<title>Live 2d</title>
			</head>
			<body>
				<div class="common-bar" >
						<button class="common-button" onclick="switchPageToMain()">返回主界面</button>
				</div>
				<div style="max-width: 450px; min-width: 100px; padding: 12px">
					<div class="common-title">萌宠设置</div>
					<div class="common-subtitle">基本操作:</div>
					<div class="common-bar">
						<button class="common-button" onclick="lodashLive2d()">启动live2d</button>
						<button class="common-button" onclick="closeLive2d()"> 关闭live2d</button>
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

				  <br/>
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
						<input style="width: 30%" placeholder="默认30" type="number" onchange="handleChangeTime(event)" />
						<button style="width: 30%" onclick="openBackgroundSetTime()"> 开启</button>
						<button style="width: 30%" onclick="closeBackgroundSetTime()"> 关闭</button>
					</div>	
				</div>
			
				<script nonce="${nonce}" src="${scriptUri}"></script>
			</body>
			</html>`;
	};

	// 生成Ai助手
	_getAiChatHtml(webview) {
		const aiHtmlPath = path.join(this._extensionUri.fsPath, 'media', 'ai-assistant.html');
		let html = fs.readFileSync(aiHtmlPath, 'utf8');

		const scriptUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, 'media', 'ai-assistant.js')
		);

		html = html.replace('<!--SCRIPT_PLACEHOLDER-->', `<script type="module" src="${scriptUri}"></script>`);

		return html;
	}

	// 生成主菜单
	_getMainHtml(webview) {
		const htmlPath = path.join(__dirname, '../../media/menu.html');
		let htmlContent = fs.readFileSync(htmlPath, 'utf8');

		// 正确地动态替换本地资源路径
		const logoUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "logo.png")
		);
		htmlContent = htmlContent.replace(/{{logo}}/g, logoUri.toString());

		return htmlContent;
	}

	// 生成题单
	_getProblemListHtml(webview) {
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const styleCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "styles.css"));
		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "data.js"));
		const appUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "ProblemList", "app.js"));

		return `
			<!DOCTYPE html>
			<html lang="zh-CN">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>算法题单</title>
				<link rel="stylesheet" href="${vscodeCssUri}">
				<link rel="stylesheet" href="${styleCssUri}">
			</head>
			<body>
				<div class="header">
        	<button class="back-btn" id="back-btn" onclick="switchPageToMain()">←</button>
        	<h3 style="font-weight: 600;">知识树</h3>
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
			</body>

			</html>`
	}

	// 生成题目界面
	_getProblemHtml(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));		// css主题
		const katex_min_css_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "katex.min.css")); // katex.min.css
		const katex_min_js_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "katex.min.js")); // katex.min.js
		const katex_auto_render_min_js_Uri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "res", "katex", "auto-render.min.js")); // auto-render.min.js

		const filePath = path.join(this._extensionUri.fsPath, "saveData", "example.md");
		const fileContent = fs.readFileSync(filePath, 'utf8');

		return `<!DOCTYPE html>
			<html lang="en">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Markdown Displayer</title>
				<link href="${styleVSCodeUri}" rel="stylesheet" />
				<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
				<link rel="stylesheet" href="${katex_min_css_Uri}">
  			<script src="${katex_min_js_Uri}"></script>
  			<script src="${katex_auto_render_min_js_Uri}"></script>
			</head>

			<body>
				<button onclick="renderMarkdown()" class="common-button">渲染</button>
				<button onclick="goBack()" class="common-button">返回主界面</button>
				<div id="markdownDisplay"></div>
				<script>
					const vscode = acquireVsCodeApi();
					const MainOrigin = "vscode-file://vscode-app";
					const fs = require('fs');
					const path = require('path');
					

					function goBack() {
						vscode.postMessage({ type: 'switchPageToProblemList' });
					}

					function renderMarkdown() {
						var markdownDisplay = document.getElementById('markdownDisplay');
						var markdownText = ${JSON.stringify(fileContent)};
						var htmlContent = marked.parse(markdownText);
						markdownDisplay.innerHTML = htmlContent;
						renderMathInElement(markdownDisplay, {
        			delimiters: [
          			{ left: "$$", right: "$$", display: true },
          			{ left: "$", right: "$", display: false }
        			]
      			});
					}
				</script>
			</body>

			</html>`;
	}

	// 生成登录界面
	_getLoginHtml(webview) {
		const styleVSCodeUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css")
		);
		const logoUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "logo.png")
		);
		const backgroundUri = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "back.jpg")
		);
		const htmlPath = path.join(this._extensionUri.fsPath, "media", "login.html");
		const leetcodeIcon = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "leetcode.png")
		);
		const luoguIcon = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "luogu.png")
		);
		const githubIcon = webview.asWebviewUri(
			vscode.Uri.joinPath(this._extensionUri, "res", "image", "github.png")
		);
		let htmlContent = fs.readFileSync(htmlPath, 'utf8');

		htmlContent = htmlContent.replace(/{{styleVSCodeUri}}/g, styleVSCodeUri.toString())
			.replace(/{{logoUri}}/g, logoUri.toString())
			.replace(/{{backgroundUri}}/g, backgroundUri.toString())
			.replace(/{{leetcodeIcon}}/g, leetcodeIcon.toString())
			.replace(/{{luoguIcon}}/g, luoguIcon.toString())
			.replace(/{{githubIcon}}/g, githubIcon.toString());
		return htmlContent;
	}

	// 生成题目树
	_getTreeHtml(webview) {
		const dataUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "data.js"));
		const logicUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "logic.js"));
		const styleCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "TreeNode", "style.css"))
		const vscodeCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"))

		return `
			<!DOCTYPE html>
			<html lang="zh-CN">

			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>知识树图谱</title>
				<link rel="stylesheet" href="${vscodeCssUri}">
				<link rel="stylesheet" href="${styleCssUri}">
			</head>

			<body>
				<div class="header">
        	<button class="back-btn" id="back-btn" onclick="switchPageToMain()">←</button>
        	<h3 style="font-weight: 600;">知识树</h3>
    		</div>
				
				<div class="controls">
					<h3>测试控制（可删除）</h3>
					<button class="reset-btn" onclick="resetTechTree()">重置</button>
					<div class="info">点击蓝色节点解锁</div>
				</div>
			  <div class="spacer"></div>
				<div class="tech-tree-container">
					<div class="tech-tree" id="techTree">
					</div>
				</div>

				<script src="${dataUri}"></script>
				<script src="${logicUri}"></script>
			</body>

			</html>
		`
	}

	// 生成日历 
	_getCalenderHtml(webview) {
		const calenderPath = path.join(__dirname, '../.././media/calender.html');

		// 读取calender.html内容
		const htmlContent = fs.readFileSync(calenderPath, 'utf8');

		return htmlContent;
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
