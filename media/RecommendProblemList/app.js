// 使用全局变量
// 直接使用全局作用域中的变量，不重新声明

const vscode = acquireVsCodeApi();

let recommendedProblems = [];

// 返回主界面
function switchPageToMain() {
  vscode.postMessage({ type: "goBack" });
}

// 确保在全局作用域中可用
window.switchPageToMain = switchPageToMain;

// 跳转到题目界面
window.switchPageToProblem = function (problemRef) {
  const problem = recommendedProblems.find(p => p.ref === problemRef);
  if (problem) {
    vscode.postMessage({
      type: "switchPageToProblem",
      title: problem.title,
      ref: problem.ref,
      listId: -1 // 推荐题单可以用 -1 标识
    });
  }
};

// 更新统计信息
function updateStats() {
  const totalCount = recommendedProblems.length;
  const passedCount = recommendedProblems.filter(p => p.passed).length;
  const progress = totalCount === 0 ? 0 : Math.round((passedCount / totalCount) * 100);

  document.getElementById("total-count").textContent = totalCount;
  document.getElementById("passed-count").textContent = passedCount;
  document.getElementById("progress").textContent = `${progress}%`;
}

// 渲染题目列表
function renderProblemList() {
  const problemListElement = document.getElementById("reproblem-list");

  updateStats();

  if (!recommendedProblems || recommendedProblems.length === 0) {
    problemListElement.innerHTML = `
      <div class="empty-state">
        <i>📭</i>
        <h3>暂无推荐题目</h3>
        <p>请先完成一些知识节点的题目</p>
      </div>
    `;
    return;
  }

  problemListElement.innerHTML = recommendedProblems.map(problem => `
    <div class="problem-item" onclick="switchPageToProblem(${problem.ref})">
      <div class="problem-info">
        <div class="problem-title">
          <a href="${problem.url}" target="_blank">${problem.title}</a>
        </div>
        <div class="problem-meta">
          <span class="difficulty ${problem.difficulty}">
            ${problem.difficulty === "easy" ? "简单" :
      problem.difficulty === "medium" ? "中等" : "困难"}
          </span>
          <span>${Array.isArray(problem.tags) ? problem.tags.join(", ") : ""}</span>
        </div>
      </div>
      <div class="status ${problem.passed ? "passed" : "failed"}">
        <span class="status-icon">${problem.passed ? "✓" : "✗"}</span>
        <span>${problem.passed ? "已通过" : "未通过"}</span>
      </div>
    </div>
  `).join("");
}

// 页面初始化
window.onload = function () {
  // 先拿全局题库（目前暂时复用 problemSets）
  // 这里先把所有 list 的题合并成一个池子
  let allProblems = [];

  Object.keys(problemSets).forEach(listId => {
    const list = problemSets[listId];
    if (list && list.problems) {
      allProblems = allProblems.concat(list.problems.map(p => ({ ...p, listId: listId })));
    }
  });

  // passed 状态更新
  if (window.passedProblems && Array.isArray(window.passedProblems)) {
    allProblems.forEach(p => {
      if (window.passedProblems.includes(p.ref)) {
        p.passed = true;
      }
    });
  }

  // 用户画像
  const userProfile = {
    passedProblems: window.passedProblems || [],
    problemSets: problemSets // 传递题单数据，用于知识树进度分析
  };

  // 推荐算法输出推荐题
  recommendedProblems = recommendProblems(allProblems, userProfile, 5);

  renderProblemList();
};