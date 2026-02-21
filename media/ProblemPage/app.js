const vscode = acquireVsCodeApi();
let problemListID = 1;
let problemTitle = "整型与布尔型的转换";

function switchPageToProblemList() {
  vscode.postMessage({ type: 'goBack' });
}

function completeProblem() {
  const ref = window.currentProblemRef;
  vscode.postMessage({
    type: 'problemPassed',
    ref: ref
  });
  const btn = document.querySelector('.complete-btn');
  if (btn) {
    btn.textContent = "已完成";
    btn.style.backgroundColor = "#888";
    btn.disabled = true;
  }
}

function renderMarkdown() {
  document.getElementById('listTitle').textContent = problemTitle;
  var markdownDisplay = document.getElementById('markdownDisplay');

  var htmlContent = marked.parse(markdownText);
  markdownDisplay.innerHTML = htmlContent;
  renderMathInElement(markdownDisplay, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false }
    ]
  });
}
window.addEventListener('message', event => {
  const message = event.data;
  if (message.type === "judgeResult") {
    const results = message.results;
    // 只取总评测状态
    const total = results;
    console.log("评测结果:", total);
    const statusDiv = document.getElementById("judgeStatus");
    if (statusDiv) {
      statusDiv.textContent = `评测结果: ${total}`;
    }
    if (total === "AC") {
      const ref = window.currentProblemRef;
      vscode.postMessage({
        type: 'problemPassed',
        ref: ref
      });
    }
  }
});
window.onload = function () {
  problemListID = window.currentProblemListID;
  problemTitle = window.currentProblemTitle;
  renderMarkdown();

  // 绑定已有的评测按钮
  const judgeBtn = document.getElementById("judgeBtn");
  if (judgeBtn) {
    judgeBtn.addEventListener("click", () => {
      const ref = window.currentProblemRef;

      // 发送消息给 VSCode 执行评测
      vscode.postMessage({
        type: "judge",
        ref: ref
      });

      // 更新状态显示区域
      let statusDiv = document.getElementById("judgeStatus");
      if (!statusDiv) {
        statusDiv = document.createElement("pre");
        statusDiv.id = "judgeStatus";
        statusDiv.style.marginTop = "12px";
        statusDiv.style.padding = "12px 16px";
        statusDiv.style.borderRadius = "12px";
        statusDiv.style.background = "linear-gradient(135deg, #e0f7fa, #b2ebf2)"; // 背景浅一点
        statusDiv.style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";
        statusDiv.style.fontFamily = 'Arial, "Microsoft YaHei", sans-serif';
        statusDiv.style.fontSize = "14px";
        statusDiv.style.color = "#004040";  // 深色字体，更易阅读
        statusDiv.style.whiteSpace = "pre-wrap";
        statusDiv.style.wordBreak = "break-word";

        // 将状态区域放在“完成题目”按钮下方
        const completeBtn = document.querySelector('.complete-btn');
        if (completeBtn) completeBtn.insertAdjacentElement('afterend', statusDiv);
        else document.body.appendChild(statusDiv);
      }

      statusDiv.textContent = "开始评测，请稍候...";
    });
  }
};