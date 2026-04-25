const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";

let currentListId = "list_1";
let currentListName = "";
let listIdFromVSCode = 1;
let userProfile = {
  passedProblems: [],
  weakTags: [],
  currentTags: [],
  targetDifficulty: "easy"
};


function switchPageToMain() {
  vscode.postMessage({ type: 'goBack' });
}

function switchPageToProblem(problemId) {
  const problems = problemSets[currentListId].problems;
  const problem = problems.find(p => p.id === problemId);

  if (problem) {
    vscode.postMessage({
      type: 'switchPageToProblem',
      title: problem.title,
      ref: problem.ref,
      listId: listIdFromVSCode
    });
  }
}

function aiKnowledgeLearn() {
  vscode.postMessage({
    type: 'switchPageToAiChat',
    bootstrap: {
      mode: 'knowledge',
      knowledgeName: currentListName
    }
  });
}

// 更新统计信息
function updateStats() {
  const problems = problemSets[currentListId].problems;
  const totalCount = problems.length;
  const passedCount = problems.filter(p => p.passed).length;
  const progress = Math.round((passedCount / totalCount) * 100);

  document.getElementById('total-count').textContent = totalCount;
  document.getElementById('passed-count').textContent = passedCount;
  document.getElementById('progress').textContent = `${progress}%`;
}

// 渲染题目列表
function renderProblemList() {
  const problemListElement = document.getElementById('problem-list');
  const problems = problemSets[currentListId].problems;

  document.getElementById('listTitle').textContent = problemSets[currentListId].name;

  // 更新统计信息
  updateStats();

  if (problems.length === 0) {
    problemListElement.innerHTML = `
      <div class="tp-empty-state">
        <div class="tp-empty-state-title">没有题目数据</div>
      </div>
    `;
    return;
  }

  problemListElement.innerHTML = problems.map(problem => `
    <div class="tp-problem-item" data-id="${problem.id}" onclick="switchPageToProblem(${problem.id})">
      <div class="tp-problem-info">
        <div class="tp-problem-title">
          <a href="${problem.url}" target="_blank">${problem.title}</a>
        </div>
        <div class="tp-problem-meta">
          <span class="tp-difficulty tp-difficulty-${problem.difficulty}">
            ${problem.difficulty === 'easy' ? '简单' :
      problem.difficulty === 'medium' ? '中等' : '困难'}
          </span>
          <span>${problem.tags.join(', ')}</span>
        </div>
      </div>
      <div class="tp-status tp-status-${problem.passed ? 'passed' : 'failed'}">
        <span class="tp-status-icon">${problem.passed ? '&#10003;' : '&#10007;'}</span>
        <span>${problem.passed ? '已通过' : '未通过'}</span>
      </div>
    </div>
  `).join('');
}
window.onload = function () {
  listIdFromVSCode = window.currentListId;
  currentListId = `list_${listIdFromVSCode}` || currentListId;

  if (problemSets[currentListId]) {
    currentListName = problemSets[currentListId].name || "";
  }

  if (window.passedProblems && Array.isArray(window.passedProblems)) {
    if (problemSets[currentListId] && problemSets[currentListId].problems) {
      problemSets[currentListId].problems.forEach(p => {
        if (window.passedProblems.includes(p.ref)) {
          p.passed = true;
        }
      });
    }
  }
  renderProblemList();

  const aiLearnBtn = document.getElementById('aiLearnBtn');
  if (aiLearnBtn) {
    aiLearnBtn.addEventListener('click', () => {
      aiKnowledgeLearn();
    });
  }
}