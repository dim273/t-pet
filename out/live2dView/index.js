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
		this._page = 'test5';  // 当前页面状态
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
				// 切换页面
				case "switchPageToTest1":
					this._page = 'test1';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToTest2":
					this._page = 'test2';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToTest3":
					this._page = 'test3';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToTest4":
					this._page = 'test4';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToTest5":
					this._page = 'test5';
					webviewView.webview.html = this.updateWebviewContent(webviewView.webview);
					break;
				case "switchPageToSetting":
					this._page = 'setting';
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
		switch (this._page) {
			case 'test1':
				return this._getTestHtml1(webview);
			case 'test2':
				return this._getTestHtml2(webview);
			case 'test3':
				return this._getTestHtml3(webview);
			case 'test4':
				return this._getTestHtml4(webview);
			case 'test5':
				return this._getTestHtml5(webview);
			default:
				return this._getSettingHtml(webview);
		}
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

	_getTestHtml1(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test1.css"));

		return `<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
					<link href="${styleVSCodeUri}" rel="stylesheet"> 
					<link href="${testCssUri}" rel="stylesheet">
					<title>Live 2d</title>
				</head>
			<body>
					<div class="learning-container">
        	<!-- 顶部状态栏 -->
        	<div class="knowledge-header">
            <div class="knowledge-title">知识树</div>
        	</div>
        	<div class="status-header">
            <div class="status-item">
                <div class="status-label">今日任务</div>
                <div class="status-value">2/3</div>
            </div>
            <div class="status-item">
                <div class="status-label">连续打卡</div>
                <div class="status-value">7天</div>
            </div>
            <div class="status-item">
                <div class="status-label">总积分</div>
                <div class="status-value">1850</div>
            </div>
        	</div>

        	<!-- 算法学习路径 -->
        	<div class="skill-track">
            <!-- 排序算法 -->
            <div class="algorithm-node completed">
                <div class="node-xp">★ 300</div>
                <div class="node-core">
                    <div class="progress-ring"></div>
                    <div class="node-content">
                        <div class="node-title">💖</div>
                        <div class="node-title">排序算法</div>
                    </div>
                </div>
                <div class="status-indicator"></div>
            </div>

            <!-- 二分搜索 -->
            <div class="algorithm-node current">
                <div class="node-xp">★ 450</div>
                <div class="node-core">
                    <div class="progress-ring"></div>
                    <div class="node-content">
                        <div class="node-title">✨</div>
                        <div class="node-title">二分搜索</div>
                    </div>
                </div>
                <div class="status-indicator"></div>
            </div>

            <!-- 递归 -->
            <div class="algorithm-node">
                <div class="node-xp">★ 200</div>
                <div class="node-core">
                    <div class="progress-ring"></div>
                    <div class="node-content">
                        <div class="node-title">🎉</div>
                        <div class="node-title">递归算法</div>
                    </div>
                </div>
                <div class="status-indicator"></div>
            </div>

            <!-- 动态规划 -->
            <div class="algorithm-node locked">
                <div class="node-xp">🔒 锁定</div>
                <div class="node-core">
                    <div class="progress-ring"></div>
                    <div class="node-content">
                        <div class="node-title">🎨</div>
                        <div class="node-title">动态规划</div>
                    </div>
                </div>
                <div class="status-indicator"></div>
            </div>
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

	_getTestHtml2(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test1.css"));

		return `<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
					<link href="${styleVSCodeUri}" rel="stylesheet"> 
					<link href="${testCssUri}" rel="stylesheet">
					<title>Live 2d</title>
				</head>
			<body>
				<div class="ai-chat-container">
        <div class="ai-header">
            <div class="ai-title">AI HELPER</div>
        </div>
        <!-- 消息区域 -->
        <div class="chat-messages">
            <!-- AI消息 -->
            <div class="message-bubble ai-message">
                需要帮助解释这段代码吗？
                <pre class="code-block">function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        ...
    }
}</pre>
            </div>

            <!-- 用户消息 -->
            <div class="message-bubble user-message">
                为什么这里的循环条件是 left &lt;= right？
            </div>

            <!-- AI消息 -->
            <div class="message-bubble ai-message">
                这个条件确保搜索区间闭合，当left=right时仍需检查最后一个元素...
            </div>

            <!-- 加载状态 -->
            <div class="typing-indicator">
                <div class="typing-dot" style="animation-delay: 0s"></div>
                <div class="typing-dot" style="animation-delay: 0.2s"></div>
                <div class="typing-dot" style="animation-delay: 0.4s"></div>
            </div>
        </div>

        <!-- 输入区域 -->
        <div class="chat-input-area">
            <textarea 
                class="chat-input" 
                placeholder="向AI助手提问..."
                rows="1"
            ></textarea>
            <button class="send-button"></button>
        </div>
    </div>
				<script>
        	const vscode = acquireVsCodeApi();
					const MainOrigin = "vscode-file://vscode-app";
        	function switchPage() {
    				vscode.postMessage({ type: 'switchPage' });
    			}
					// 动态调整输入框高度
        	const textarea = document.querySelector('.chat-input');
        	textarea.addEventListener('input', () => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        	});

        	// 模拟发送消息
        	document.querySelector('.send-button').addEventListener('click', () => {
            const messages = document.querySelector('.chat-messages');
            
            // 添加用户消息
            const userMsg = document.createElement('div');
            userMsg.className = 'message-bubble user-message';
            userMsg.textContent = textarea.value;
            messages.appendChild(userMsg);

            // 显示加载状态
            const typing = document.querySelector('.typing-indicator');
            typing.style.display = 'flex';
            
            // 清空输入框
            textarea.value = '';
            
            // 模拟AI回复
            setTimeout(() => {
                typing.style.display = 'none';
                const aiMsg = document.createElement('div');
                aiMsg.className = 'message-bubble ai-message';
                aiMsg.textContent = '这是模拟的AI回复内容...';
                messages.appendChild(aiMsg);
                messages.scrollTop = messages.scrollHeight;
            }, 1500);
        	});
    		</script>
			</body>
			</html>
		`;
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

	_getTestHtml4(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test1.css"));

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
            <button class="back-btn">←</button>
            <div class="problem-meta">
                <div class="problem-title">两数之和</div>
                <div class="problem-tags">
                    <span>#数组</span>
                    <span>#哈希表</span>
                    <span>通过率 68%</span>
                </div>
            </div>
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
						function switchPage() {
							vscode.postMessage({ type: 'switchPage' });
						}
						// 复制功能
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
							document.getElementById('12').style.display = 'block';
							
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

	_getTestHtml5(webview) {
		const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
		const testCssUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "test1.css"));

		return `<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
					<link href="${styleVSCodeUri}" rel="stylesheet"> 
					<link href="${testCssUri}" rel="stylesheet">
					<title>Live 2d</title>
				</head>
			<body>
				<div class="auth-container">
        	<!-- 头部 -->
        	<div class="auth-header">
            <div class="auth-title">用户登录</div>
            <div class="auth-subtitle">选择OJ平台进行登录</div>
        	</div>

        	<!-- 平台切换 -->
        	<div class="platform-tabs">
            <div class="platform-tab active" data-platform="leetcode"><button class="common-button" onclick= "switchPage()"
            style="padding: 5px 10px; background: #58CC02; border: none; border-radius: 3px; cursor: pointer;">
            力扣
        </button>
            <div class="platform-tab" data-platform="luogu"><button class="common-button" onclick= "switchPage()"
            style="padding: 5px 10px; background:rgb(22, 86, 207); border: none; border-radius: 3px; cursor: pointer;">
            洛谷
        </button>
            <div class="platform-tab" data-platform="acwing"><button class="common-button" onclick= "switchPage()"
            style="padding: 5px 10px; background:rgb(149, 140, 71); border: none; border-radius: 3px; cursor: pointer;">
            Acwing
        </button>
        	</div>

        	<!-- 登录表单 -->
        	<form class="auth-form" id="loginForm">
            <!-- LeetCode -->
            <div class="form-group" data-platform="leetcode">
                <label class="form-label">用户名</label>
                <input type="text" class="form-input" placeholder="LeetCode用户名">
            </div>
            <div class="form-group" data-platform="leetcode">
                <label class="form-label">密码</label>
                <input type="password" class="form-input" placeholder="••••••••">
            </div>

            <!-- 洛谷 -->
            <div class="form-group" data-platform="luogu" style="display:none">
                <label class="form-label">账号</label>
                <input type="text" class="form-input" placeholder="用户名/邮箱/手机号">
            </div>
            <div class="form-group" data-platform="luogu" style="display:none">
                <label class="form-label">密码</label>
                <input type="password" class="form-input" placeholder="••••••••">
            </div>

            <!-- AcWing -->
            <div class="form-group" data-platform="acwing" style="display:none">
                <label class="form-label">账号</label>
                <input type="text" class="form-input" placeholder="用户名/手机号">
            </div>
            <div class="form-group" data-platform="acwing" style="display:none">
                <label class="form-label">密码</label>
                <input type="password" class="form-input" placeholder="••••••••">
            </div>

            <div class="remember-group">
                <input type="checkbox" class="checkbox" id="remember">
                <label for="remember">保持登录</label>
            </div>

            <button type="submit" class="submit-btn" onclick = "switchPageToTest1()">立即登录</button>

            <!-- 加载状态 -->
            <div class="auth-loading" id="loading">
                <div class="loading-spinner"></div>
            </div>

            <!-- 反馈信息 -->
            <div class="auth-feedback" id="feedback"></div>
        	</form>

        	<!-- 第三方登录 -->
        	<div class="oauth-login">
            <button class="oauth-btn" onclick = "switchPageToTest1()">
                <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor" style="margin-right:6px">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                GitHub登录
            </button>
        	</div>
    		</div>
				<script>
        	const vscode = acquireVsCodeApi();
					const MainOrigin = "vscode-file://vscode-app";
        	function switchPageToTest1() {
    				vscode.postMessage({ type: 'switchPageToTest1' });
    			}
					// 平台切换逻辑
        document.querySelectorAll('.platform-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                // 切换激活状态
                document.querySelectorAll('.platform-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                // 切换表单显示
                const platform = tab.dataset.platform;
                document.querySelectorAll('.form-group').forEach(group => {
                    group.style.display = group.dataset.platform === platform ? 'block' : 'none';
                });
            });
        });

        // 表单提交
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const loading = document.getElementById('loading');
            const feedback = document.getElementById('feedback');

            loading.style.display = 'flex';
            feedback.style.display = 'none';

            // 模拟API请求
            setTimeout(() => {
                loading.style.display = 'none';
                
                const isSuccess = Math.random() > 0.3;
                feedback.style.display = 'block';
                feedback.className = isSuccess ? 'auth-feedback success' : 'auth-feedback error';
                feedback.textContent = isSuccess 
                    ? '✓ 登录成功，正在跳转...' 
                    : '✗ 登录失败：用户名或密码错误';
            }, 1200);
        	});

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