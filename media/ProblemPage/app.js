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

window.onload = function () {
  problemListID = window.currentProblemListID;
  problemTitle = window.currentProblemTitle;
  renderMarkdown();
}