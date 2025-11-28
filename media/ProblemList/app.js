const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";
function switchPageToMain() {
  vscode.postMessage({ type: 'switchPageToMain' });
}

// 更新统计信息
function updateStats() {
  const problems = problemSets["list_2"].problems;
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
  const problems = problemSets["list_2"].problems;

  // 更新统计信息
  updateStats();

  if (problems.length === 0) {
    problemListElement.innerHTML = `
      <div class="empty-state">
        <i>🔍</i>
        <h3>没有题目数据</h3>
      </div>
    `;
    return;
  }

  problemListElement.innerHTML = problems.map(problem => `
    <div class="problem-item" data-id="${problem.id}">
      <div class="problem-info">
        <div class="problem-title">
          <a href="${problem.url}" target="_blank">${problem.title}</a>
        </div>
        <div class="problem-meta">
          <span class="difficulty ${problem.difficulty}">
            ${problem.difficulty === 'easy' ? '简单' :
      problem.difficulty === 'medium' ? '中等' : '困难'}
          </span>
          <span>${problem.tags.join(', ')}</span>
        </div>
      </div>
      <div class="status ${problem.passed ? 'passed' : 'failed'}">
        <span class="status-icon">${problem.passed ? '✓' : '✗'}</span>
        <span>${problem.passed ? '已通过' : '未通过'}</span>
      </div>
    </div>
  `).join('');
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
  renderProblemList();
});