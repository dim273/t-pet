"use strict";
// 设置模块导出标记
Object.defineProperty(exports, "__esModule", { value: true });
exports.activateLive2d = activateLive2d;

// 导入 VSCode API和自定义模块
const vscode = require("vscode");
const Main_1 = require("../live2dModify/Main");

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
		this._page = 'setting';  // 当前页面状态
	}

	// 解析 Webview 视图
	resolveWebviewView(webviewView, context, _token) {
		// 保存 Webview 实例引用
		this._view = webviewView;

		// 配置 Webview 选项
		webviewView.webview.options = {
			enableScripts: true,  // 允许执行脚本
			localResourceRoots: [this._extensionUri],  // 允许加载的资源路径
		};

		// 设置 HTML 内容
		// webviewView.webview.html = this._getTest3Html(webviewView.webview);
		webviewView.webview.html = this.updateWebviewContent(webviewView.webview);

		// 处理来自 Webview 的消息
		webviewView.webview.onDidReceiveMessage((data) => {
			switch (data.type) {
				case "switchPage":
					// 切换页面
					this._page = this._page === 'test' ? 'setting' : 'test';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "generateResources":
					// 生成资源文件
					Main_1.Main.Instance && Main_1.Main.Instance.generateResources();
					break;
				case "removeResources":
					// 移除资源文件（clean: true 表示彻底清理）
					Main_1.Main.Instance && Main_1.Main.Instance.removeResources(true);
					break;
			}
		});
	}

	updateWebviewContent(webview) {
		if (this._page === 'test') return this._getTestHtml(webview);
		else return this._getSettingHtml(webview);
	}

	// 生成 Webview 的 HTML 内容
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
				<div style="max-width: 450px; min-width: 100px; padding: 12px">
					<div class="common-title">基本操作:</div>
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

				<br />
					<div class="common-title">配置信息:</div>
					<div class="common-subtitle">自启动:</div>
					<div class="common-bar" >
						<button class="common-button" onclick="openAutoLodash()">开启</button>
						<button class="common-button" onclick="closeAutoLodash()">关闭</button>
					</div>
					<!-- <div style="display: flex;" >
						<div class="common-subtitle">定位依赖:</div>
						<span style="font-style: 12px;font-weight: 400;">(初始默认为右下角)</span>
					</div> -->
					<div class="common-subtitle">定位依赖:</div>
					<div class="common-bar">
						<button class="common-button" onclick="setAnchor('tl')">左上角</button>
						<button class="common-button" onclick="setAnchor('tr')">右上角</button>
						<button class="common-button" onclick="setAnchor('bl')">左下角</button>
						<button class="common-button" onclick="setAnchor('br')">右下角</button>
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

					<div class="common-title">背景图相关功能失效</div>
					<div class="common-subtitle">因为获取图片的接口没了</div>
					<div class="common-subtitle">背景图:(需要先启动live2d人物)</div>
					<div class="common-bar">
						<button class="common-button" onclick="saveBackground()">保存背景图</button>
						<button class="common-button" onclick="loadBackground()"> 加载背景图</button>
					</div>
					<div class="common-subtitle">定时切换(分钟):</div>
					<div class="common-bar">
						<input style="width: 30%" placeholder="默认30" type="number" onchange="handleChangeTime(event)" />
						<button style="width: 30%" onclick="openBackgroundSetTime()"> 开启</button>
						<button style="width: 30%" onclick="closeBackgroundSetTime()"> 关闭</button>
					</div>
					<div class="common-subtitle">背景图配置:(会默认使用最近配置)</div>
					<div class="common-bar">
						<div style="margin-right:6px" > 不透明度:  </div>
						<input id="background-opacity-input" style="width: 80%; flex: 1" type="number" placeholder="范围: 0-1，默认是0.2" onchange="handleChangeOpacity(event)" />
					</div>
					<div class="common-subtitle">页面切换:</div>
					<div class="common-bar" >
						<button class="common-button" onclick="switchPage()">切换</button>
					</div>
					<div class="common-bar">
						<div style="margin-right:6px" > 适配样式:  </div>
						<select id="background-mode-select" style="width: 80%; flex: 1" onchange="handleChangeMode(event)">
							<option value='' disabled selected style='display:none;'>背景图适配样式,默认是覆盖</option>  
							<option value="cover">覆盖</option>
							<option value="contain">适应</option>
						</select>
					</div>
					<div class="common-bar" style="justify-content: space-round" >
						<button style="width: 45%" onclick="modifyBackgroundConfig()"> 确认</button>
						<button style="width: 45%" onclick="restoreBgConfig()"> 恢复默认</button>
					</div>

					<br />
					<div class="common-title">测试功能:</div>
					<div class="common-subtitle">下载当前背景图(勿短时间内多次点击):</div>
					<div class="common-bar">
						<button class="common-button" onclick="downloadBackground()">获取当前背景</button>
						<button class="common-button" onclick="removeDownloadBackground()">移除下载展示</button>
					</div>
					<div id="currentBackground" class="common-bar"></div>
				</div>
			
				<script nonce="${nonce}" src="${scriptUri}"></script>
			</body>
			</html>`;
	};

	_getTestHtml(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test.css"));


		return `<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<link href="${styleVSCodeUri}" rel="stylesheet"> 
				<link href="${testCssUri}" rel="stylesheet">
				<title>Live 2d</title>
			</head>
			<body>
    <div style="position: fixed; top: 10px; right: 10px; z-index: 1000;">
        <button class="common-button" onclick= "switchPage()"
            style="padding: 5px 10px; background: #58CC02; border: none; border-radius: 3px; cursor: pointer;">
            返回主界面
        </button>
    </div>
    <div class="problem-sidebar">
        <!-- 题目卡片1 -->
        <div class="problem-card">
            <div class="card-header">
                <div class="problem-title">两数之和</div>
                <div class="difficulty easy">简单</div>
            </div>
            <div class="problem-desc">
                在数组中找到两个数，使它们的和等于目标值
            </div>
            <div class="tag-container">
                <span class="problem-tag">数组</span>
                <span class="problem-tag">哈希表</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
            <div class="card-footer">
                <span>68% 通过</span>
                <span>🔥 126k</span>
            </div>
        </div>

        <!-- 题目卡片2 -->
        <div class="problem-card">
            <div class="card-header">
                <div class="problem-title">反转链表</div>
                <div class="difficulty medium">中等</div>
            </div>
            <div class="problem-desc">
                使用迭代和递归两种方式反转单链表
            </div>
            <div class="tag-container">
                <span class="problem-tag">链表</span>
                <span class="problem-tag">递归</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 45%"></div>
            </div>
            <div class="card-footer">
                <span>52% 通过</span>
                <span>⭐ 89k</span>
            </div>
        </div>

        <!-- 题目卡片3 -->
        <div class="problem-card">
            <div class="card-header">
                <div class="problem-title">二叉树遍历</div>
                <div class="difficulty medium">中等</div>
            </div>
            <div class="problem-desc">
                实现二叉树的先序、中序、后序遍历的迭代算法
            </div>
            <div class="tag-container">
                <span class="problem-tag">二叉树</span>
                <span class="problem-tag">栈</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 38%"></div>
            </div>
            <div class="card-footer">
                <span>61% 通过</span>
                <span>📚 常考</span>
            </div>
        </div>

        <!-- 题目卡片4 -->
        <div class="problem-card">
            <div class="card-header">
                <div class="problem-title">动态规划</div>
                <div class="difficulty hard">困难</div>
            </div>
            <div class="problem-desc">
                硬币找零问题：计算凑成总金额的最少硬币个数
            </div>
            <div class="tag-container">
                <span class="problem-tag">DP</span>
                <span class="problem-tag">背包问题</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 28%"></div>
            </div>
            <div class="card-footer">
                <span>32% 通过</span>
                <span>🏆 大厂</span>
            </div>
        </div>

				<div class="common-subtitle">页面切换:</div>
					<div class="common-bar" >
						<button class="common-button" onclick="switchPage()">切换</button>
				</div>
    </div>

    <script>
        const vscode = acquireVsCodeApi();
				const MainOrigin = "vscode-file://vscode-app";
        function switchPage() {
    			vscode.postMessage({ type: 'switchPage' });
    		}
    </script>
	</body>

	</html>
		      
		`;
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