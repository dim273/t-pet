const vscode = acquireVsCodeApi();

const accountsContainer = document.getElementById('accountsContainer');
const createAccountBtn = document.getElementById('createAccountBtn');
const successMsg = document.getElementById('successMsg');
const importAccount = document.getElementById('importAccount');
const exportAccount = document.getElementById('exportAccount');

// 弹窗相关变量
let currentDeleteAccountId = null;

// 初始化界面
function initAccountManager() {
  renderAccounts();
  setupEventListeners();
}

// 渲染账号列表
function renderAccounts() {
  // 处理无账号情况
  if (accounts.length === 0) {
    accountsContainer.innerHTML = `
      <div class="no-accounts">
        暂无账号，点击"新建账号"开始使用
      </div>
    `;
    return;
  }

  accountsContainer.innerHTML = accounts.map(account => `
    <div class="account-item" data-account-id="${account.id}">
      <div class="account-info">
        <span class="account-name">${account.name}</span>
        <div class="account-actions">
          <button class="delete-button" onclick="deleteAccount(${account.id})">删除</button>
        </div>
      </div>
      <div class="platform-status">
        <div class="platform ${account.platforms.leetcode ? 'connected' : 'disconnected'}">
          <span>LeetCode</span>
        </div>
        <div class="platform ${account.platforms.luogu ? 'connected' : 'disconnected'}">
          <span>洛谷</span>
        </div>
        <div class="platform ${account.platforms.github ? 'connected' : 'disconnected'}">
          <span>GitHub</span>
        </div>
      </div>
      <div style="font-size: 12px; color: #888; margin-top: 5px;">
        最后登录: ${account.lastLogin}
      </div>
    </div>
  `).join('');

  // 添加点击事件
  document.querySelectorAll('.account-item').forEach(item => {
    item.addEventListener('click', (e) => {
      if (!e.target.classList.contains('delete-button')) {
        selectAccount(parseInt(item.dataset.accountId));
      }
    });
  });
}

// 选择账号
function selectAccount(accountId) {
  document.querySelectorAll('.account-item').forEach(item => {
    item.classList.remove('active');
  });

  const selectedItem = document.querySelector(`[data-account-id="${accountId}"]`);
  if (selectedItem) {
    // 添加滑动动画
    selectedItem.style.transform = 'translateX(8px)';
    selectedItem.style.transition = 'transform 0.3s ease';

    setTimeout(() => {
      selectedItem.classList.add('active');
      selectedItem.style.transform = 'translateX(0)';
    }, 50);

    // 平滑滚动到选中项
    selectedItem.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest'
    });

    // 切换到主界面
    vscode.postMessage({ type: 'switchPageToMain' });
    vscode.postMessage({ type: 'selectAccount', accountId });
  }
}

// 删除账号
function deleteAccount(accountId) {
  currentDeleteAccountId = accountId;
  showDeleteConfirmModal();
}

// 显示删除确认弹窗
function showDeleteConfirmModal() {
  // 创建弹窗HTML
  const modalHtml = `
    <div class="delete-modal-overlay" id="deleteModal">
      <div class="delete-modal">
        <div class="modal-header">
          <h3>确认删除</h3>
          <button class="close-button" onclick="closeDeleteModal()">×</button>
        </div>
        <div class="modal-content">
          <p>确定要删除这个账号吗？此操作不可恢复。</p>
        </div>
        <div class="modal-actions">
          <button class="confirm-button" onclick="confirmDeleteAccount()">确认</button>
          <button class="cancel-button" onclick="closeDeleteModal()">取消</button>
        </div>
      </div>
    </div>
  `;

  // 添加到body
  document.body.insertAdjacentHTML('beforeend', modalHtml);

  // 显示弹窗动画
  setTimeout(() => {
    const modal = document.getElementById('deleteModal');
    if (modal) {
      modal.classList.add('show');
    }
  }, 10);
}

// 关闭删除确认弹窗
function closeDeleteModal() {
  const modal = document.getElementById('deleteModal');
  if (modal) {
    modal.classList.remove('show');
    setTimeout(() => {
      modal.remove();
      currentDeleteAccountId = null;
    }, 300);
  }
}

// 确认删除账号
function confirmDeleteAccount() {
  if (currentDeleteAccountId !== null) {
    vscode.postMessage({ type: 'deleteAccount', accountId: currentDeleteAccountId });
    accounts = accounts.filter(account => account.id !== currentDeleteAccountId);

    renderAccounts();
    showSuccessMessage('账号删除成功');
    closeDeleteModal();
  }
}

// 创建新账号
function createNewAccount() {
  const accountName = prompt('请输入新账号名称：');
  if (accountName && accountName.trim()) {
    const newAccount = {
      id: Date.now(),
      name: accountName.trim(),
      platforms: {
        leetcode: false,
        luogu: false,
        github: false
      },
      lastLogin: new Date().toISOString().split('T')[0]
    };

    accounts.push(newAccount);
    renderAccounts();
    showSuccessMessage('账号创建成功');
  }
}

// 显示成功消息
function showSuccessMessage(message) {
  successMsg.textContent = message;
  successMsg.style.display = 'block';
  setTimeout(() => {
    successMsg.style.display = 'none';
  }, 2000);
}

// 设置事件监听器
function setupEventListeners() {
  createAccountBtn.addEventListener('click', createNewAccount);

  importAccount.addEventListener('click', () => {
    showSuccessMessage('导入功能开发中...');
  });

  exportAccount.addEventListener('click', () => {
    showSuccessMessage('帮助功能开发中...');
  });
}

// 初始化
window.onload = function () {
  initAccountManager();
}