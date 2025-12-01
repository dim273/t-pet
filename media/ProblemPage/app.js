const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";

let problemListID = 1;
let problemTitle = "整型与布尔型的转换";

function switchPageToProblemList() {
  vscode.postMessage({ type: 'switchPageToProblemList', listId: problemListID });
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