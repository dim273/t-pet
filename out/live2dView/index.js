"use strict";
// 设置模块导出标记
Object.defineProperty(exports, "__esModule", { value: true });
exports.activateLive2d = activateLive2d;

// 导入 VSCode API和自定义模块
const vscode = require("vscode");
const Main_1 = require("../live2dModify/Main");
const fs = require('fs');
const path = require('path');

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
		// webviewView.webview.html = this._getTest3Html(webviewView.webview);
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
				case "switchPageToTest3":
					this._history.push(this._page);
					this._page = 'test3';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToTest4":
					this._history.push(this._page);
					this._page = 'test4';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToLogin":
					this._history.push(this._page);
					this._page = 'login';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToCalender":
					this._history.push(this._page);
					this._page = 'calender';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
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
					// 移除资源文件（clean: true 表示彻底清理）
					Main_1.Main.Instance && Main_1.Main.Instance.removeResources(true);
					break;
			}
		});
	}

	updateWebviewContent(webview) {
		switch (this._page) {
			case 'main':
				return this._getMainHtml(webview);
			case 'test3':
				return this._getTestHtml3(webview);
			case 'test4':
				return this._getTestHtml4(webview);
			case 'login':
				return this._getLoginHtml(webview);
			case 'calender':
				return this._getCalenderHtml(webview);
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
		htmlContent = htmlContent.replace(/(src|href)="(.+?)"/g, (match, attr, relPath) => {
			// 构造绝对路径
			const resourcePath = vscode.Uri.joinPath(this._extensionUri, 'media', relPath);
			const webviewUri = webview.asWebviewUri(resourcePath);
			return `${attr}="${webviewUri}"`;
		});

		return htmlContent;
	}

	_getTestHtml3(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test3.css"));


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
        	<button class="common-button" onclick= "goBack()"
            style="padding: 5px 10px; background: #58CC02; border: none; border-radius: 3px; cursor: pointer;">
            返回主界面
        	</button>
    		</div>
    		<div class="problem-sidebar">
        <!-- 题目卡片1 -->
        <div class="problem-card" onclick= "switchPageToTest4()">
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
        	<div class="problem-card" onclick = "switchPageToTest4()">
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
        	<div class="problem-card" onclick= "switchPageToTest4()">
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
        	<div class="problem-card" onclick= "switchPageToTest4()">
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
    		</div>

    		<script>
       	 	const vscode = acquireVsCodeApi();
					const MainOrigin = "vscode-file://vscode-app";
        	function switchPageToMain() {
						vscode.postMessage({ type: 'switchPageToMain' });
					}
					function switchPageToTest4() {
						vscode.postMessage({ type: 'switchPageToTest4' });
					}
					function goBack() {
						vscode.postMessage({ type: 'goBack' });
					}
    		</script>
			</body>
		</html>
		      
		`;
	}

	_getTestHtml4(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test4.css"));

		return `<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
					<link href="${styleVSCodeUri}" rel="stylesheet"> 
					<link href="${testCssUri}" rel="stylesheet">
					<title>Live 2d</title>
				</head>
			<body>
				<div class="problem-detail">
        <!-- 头部 -->
        <div class="detail-header">
            <button class="back-btn" onclick = "goBack()">返回</button>
            <div class="problem-meta">
                <div class="problem-title">两数之和</div>
                <div class="problem-tags">
                    <span>#数组</span>
                    <span>#哈希表</span>
                    <span>通过率 68%</span>
                </div>
            </div>
						<button class= "problem-AI" onclick = "switchPageToAiChat()">AI助手</button>
        </div>

        <!-- 内容区 -->
        <div class="detail-content">
            <div class="problem-description">
                给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的两个整数，并返回它们的数组下标。
                
                你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
            </div>

            <!-- 样例切换 -->
            <div class="sample-tabs">
                <div class="tab-item active" onclick="switchSample(1)">样例1</div>
                <div class="tab-item" onclick="switchSample(2)">样例2</div>
            </div>

            <!-- 样例内容 -->
            <div class="sample-io" id="sample1">
                <div class="io-box">
                    <div class="io-header">输入</div>
                    <div class="io-content">nums = [2,7,11,15], target = 9</div>
                    <button class="copy-btn" onclick="copyCode(event)">复制</button>
                </div>
                <div class="io-box">
                    <div class="io-header">输出</div>
                    <div class="io-content">[0,1]</div>
                    <button class="copy-btn" onclick="copyCode(event)">复制</button>
                </div>
                <div class="code-sample">
                    <div>解释：nums[0] + nums[1] = 2 + 7 = 9</div>
                </div>
            </div>

            <div class="sample-io" id="sample2" style="display:none">
                <div class="io-box">
                    <div class="io-header">输入</div>
                    <div class="io-content">nums = [3,2,4], target = 6</div>
                    <button class="copy-btn" onclick="copyCode(event)">复制</button>
                </div>
                <div class="io-box">
                    <div class="io-header">输出</div>
                    <div class="io-content">[1,2]</div>
                    <button class="copy-btn" onclick="copyCode(event)">复制</button>
                </div>
            	</div>
        	</div>

        	<!-- 提交区域 -->
        	<div class="submit-area">
            <button class="submit-btn" onclick="submitCode()">提交代码</button>
            	<div class="loading-indicator" id="loading">
                <div class="loading-dot"></div>
                <div class="loading-dot" style="animation-delay:0.2s"></div>
                <div class="loading-dot" style="animation-delay:0.4s"></div>
                <span>判题中...</span>
            	</div>
            <div class="result-feedback" id="result"></div>
        	</div>
    			</div>
					<script>
						const vscode = acquireVsCodeApi();
						const MainOrigin = "vscode-file://vscode-app";
						function switchPageToMain() {
							vscode.postMessage({ type: 'switchPageToMain' });
						}
						function switchPageToAiChat() {
							vscode.postMessage({ type: 'switchPageToAiChat' });
						}
						// 复制功能
						function goBack() {
							vscode.postMessage({ type: 'goBack' });
						}
        		function copyCode(event) {
            	const content = event.target.parentElement.querySelector('.io-content').innerText;
            	navigator.clipboard.writeText(content).then(() => {
                const originalText = event.target.textContent;
                event.target.textContent = '已复制!';
                setTimeout(() => {
                    event.target.textContent = originalText;
                }, 1500);
            	}).catch(err => {
                console.error('复制失败:', err);
            });
        		}

        		// 切换样例
        		function switchSample(num) {
            	document.querySelectorAll('.sample-io').forEach(el => {
                el.style.display = 'none';
            	});
							var sam = document.getElementById('sample' + num).style.display = 'block';
            
            	document.querySelectorAll('.tab-item').forEach(el => {
                el.classList.remove('active');
            	});
            	event.target.classList.add('active');
        		}

        		// 模拟提交
        		function submitCode() {
            	const loading = document.getElementById('loading');
            	const result = document.getElementById('result');
            
            	loading.style.display = 'flex';
            	result.style.display = 'none';

            // 模拟API请求延迟
            	setTimeout(() => {
                loading.style.display = 'none';
                result.style.display = 'block';
                
                // 随机模拟成功或失败
                const isSuccess = Math.random() > 0.3;
                if (isSuccess) {
                    result.className = 'result-feedback success';
                    result.textContent = '✔ 通过所有测试用例 (执行用时：12ms)';
                } else {
                    result.className = 'result-feedback error';
                    result.textContent = '✘ 未通过测试用例：输入 [3,3] 6';
                }
            	}, 1500);
        		}

        		// 返回按钮功能
        		document.querySelector('.back-btn').addEventListener('click', () => {
            	console.log('返回上一页');
            // 实际应用中这里应该是返回逻辑
          });
    		</script>
			</body>
			</html>
		      
		`;
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