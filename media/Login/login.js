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
          <button class="close-button" onclick="closeModal('deleteModal')">×</button>
        </div>
        <div class="modal-content">
          <p>确定要删除这个账号吗？此操作不可恢复。</p>
        </div>
        <div class="modal-actions">
          <button class="confirm-button" onclick="confirmDeleteAccount()">确认</button>
          <button class="cancel-button" onclick="closeModal('deleteModal')">取消</button>
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

// 确认删除账号
function confirmDeleteAccount() {
  if (currentDeleteAccountId !== null) {
    vscode.postMessage({ type: 'deleteAccount', accountId: currentDeleteAccountId });
    accounts = accounts.filter(account => account.id !== currentDeleteAccountId);

    renderAccounts();
    showSuccessMessage('账号删除成功');
    closeModal('deleteModal');
  }
}

// 创建新账号
function createNewAccount() {
  showCreateAccountModal();
}

// 显示创建账号弹窗
function showCreateAccountModal() {
  const modalHtml = `
    <div class="delete-modal-overlay" id="createModal">
      <div class="delete-modal">
        <div class="modal-header">
          <h3>创建新账号</h3>
          <button class="close-button" onclick="closeModal('createModal')">×</button>
        </div>
        <div class="modal-content">
          <p>请输入新账号名称：</p>
          <input type="text" id="newAccountName" placeholder="NAME">
        </div>
        <div class="modal-actions">
          <button class="confirm-button" onclick="confirmCreateAccount()">确认创建</button>
          <button class="cancel-button" onclick="closeModal('createModal')">取消</button>
        </div>
      </div>
    </div>
  `;
  // 添加到body
  document.body.insertAdjacentHTML('beforeend', modalHtml);

  // 显示弹窗动画
  setTimeout(() => {
    const modal = document.getElementById('createModal');
    if (modal) {
      modal.classList.add('show');
    }
  }, 10);
}

// 确认创建账号
function confirmCreateAccount() {
  const newAccountName = document.getElementById('newAccountName').value.trim();
  if (!newAccountName) {
    closeModal('createModal')
    showErrorMessage('账号名称不能为空');
    return;
  }
  const newAccount = {
    id: Date.now(),
    name: newAccountName,
    platforms: {
      leetcode: false,
      luogu: false,
      github: false
    },
    lastLogin: new Date().toISOString().split('T')[0],
    checkInDays: {}
  };
  accounts.push(newAccount);
  renderAccounts();
  closeModal('createModal');
  vscode.postMessage({ type: 'addAccount', account: newAccount });
}

// 错误信息弹窗
function showErrorMessage(message) {
  const modalHtml = `
    <div class="delete-modal-overlay" id="warningModal">
      <div class="delete-modal">
        <h2 style="text-align:center">警告</h2>
        <div class="modal-content">
          <p>${message}</p>
        </div>
        <div class="modal-actions">
          <button class="cancel-button" onclick="closeModal('warningModal')">确认</button>
        </div>
      </div>
    </div>
  `;
  // 添加到body
  document.body.insertAdjacentHTML('beforeend', modalHtml);

  // 显示弹窗动画
  setTimeout(() => {
    const modal = document.getElementById('warningModal');
    if (modal) {
      modal.classList.add('show');
    }
  }, 10);
}

// 关闭弹窗函数
function closeModal(_id) {
  const modal = document.getElementById(_id);
  if (modal) {
    modal.classList.remove('show');
    setTimeout(() => {
      modal.remove();
    }, 300);
  }
}

// 显示帮助弹窗
function showHelpModal() {
  const modalHtml = `
    <div class="delete-modal-overlay" id="helpModal">
      <div class="delete-modal">
        <div class="modal-header">
          <h3>帮助信息</h3>
          <button class="close-button" onclick="closeModal('helpModal')">×</button>
        </div>
        <div class="modal-content">
          <div style="text-align: left; line-height: 1.6;">
            <p style="margin: 8px 0;">点击"新建账号"创建本地账号，只需输入账号名称即可，名称不能为空</p>
            <p style="margin: 8px 0;">在账号列表选择要使用的账号，点击即可登陆。也可以选择导入外部的数据，请确保数据格式正确！</p>
            <p style="margin: 8px 0;">在账号信息里面可以查看账号所绑定的平台，绿色为绑定成功，支持 LeetCode、洛谷、GitHub 平台的绑定，绑定后可以让我们根据您的学习情况，为您给出更好的学习计划</p>
            <p style="margin: 8px 0;">每个账号独立保存学习记录，并且账号信息储存在本地，一旦删除将无法恢复！</p>
          </div>
        </div>
      </div>
    </div>
  `;

  // 添加到body
  document.body.insertAdjacentHTML('beforeend', modalHtml);

  // 显示弹窗动画
  setTimeout(() => {
    const modal = document.getElementById('helpModal');
    if (modal) {
      modal.classList.add('show');
    }
  }, 10);
}

// 打开数据文件夹
function openDataFolder() {
  vscode.postMessage({ type: 'openDataFolder' });
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
    openDataFolder();
  });

  exportAccount.addEventListener('click', () => {
    showHelpModal();
  });
}

// 初始化
window.onload = function () {
  initAccountManager();
}