const fs = require('fs');
const path = require('path');
const vscode = require('vscode'); // 确保引入vscode模块

class FileStorage {
  constructor(_extensionUri) {
    // 设置存储路径
    this._storagePath = path.join(
      vscode.workspace.fsPath || _extensionUri.fsPath,
      'saveData',
      'data.json'
    );

    // 确保存储目录存在
    this.ensureDirectoryExists(path.dirname(this._storagePath));
  }

  ensureDirectoryExists(dirPath) {
    if (!fs.existsSync(dirPath)) {
      fs.mkdirSync(dirPath, { recursive: true });
    }
  }

  // 保存数据
  saveData(data) {
    try {
      const content = typeof data === 'string'
        ? data
        : JSON.stringify(data, null, 2);

      fs.writeFileSync(this._storagePath, content, 'utf8');
      return true;
    } catch (error) {
      console.error(`保存数据到${this._storagePath}失败:`, error);
      return false;
    }
  }

  // 读取数据
  readData() {
    try {
      if (!fs.existsSync(this._storagePath)) {
        return null;
      }

      const content = fs.readFileSync(this._storagePath, 'utf8');

      try {
        return JSON.parse(content);
      } catch {
        return content;
      }
    } catch (error) {
      console.error(`从${this._storagePath}读取数据失败:`, error);
      return null;
    }
  }

  // 删除数据文件
  deleteData() {
    try {
      if (fs.existsSync(this._storagePath)) {
        fs.unlinkSync(this._storagePath);
        return true;
      }
      return false;
    } catch (error) {
      console.error(`删除${this._storagePath}失败:`, error);
      return false;
    }
  }

  // 获取存储目录下的所有文件
  getAllFiles() {
    try {
      const dirPath = path.dirname(this._storagePath);
      if (!fs.existsSync(dirPath)) {
        return [];
      }

      return fs.readdirSync(dirPath)
        .filter(file => fs.statSync(path.join(dirPath, file)).isFile());
    } catch (error) {
      console.error('获取文件列表失败:', error);
      return [];
    }
  }

  // 清空存储目录下的所有文件
  clearAll() {
    try {
      const dirPath = path.dirname(this._storagePath);
      const files = this.getAllFiles();
      files.forEach(file => {
        fs.unlinkSync(path.join(dirPath, file));
      });
      return true;
    } catch (error) {
      console.error('清空存储失败:', error);
      return false;
    }
  }

  // 根据信息id获取指定账号信息
  getAccountByIndex(index) {
    try {
      const data = this.readData();
      // 获取全部的信息，然后根据索引返回对应的账号信息
      if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
        return null;
      }
      const account = data.userInfo.accounts.find(account => account.id === index);
      if (!account)
        return null;
      return account;
    } catch (error) {
      console.error(`获取索引 ${index} 的账号信息失败:`, error);
      return null;
    }
  }

  // 根据索引更新指定账号信息
  updateAccountByIndex(index, updatedAccount) {
    try {
      const data = this.readData();
      if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
        return false;
      }

      if (index < 0 || index >= data.userInfo.accounts.length) {
        return false;
      }

      // 更新指定索引的账号信息
      data.userInfo.accounts[index] = { ...data.userInfo.accounts[index], ...updatedAccount };

      return this.saveData(data);
    } catch (error) {
      console.error(`更新索引 ${index} 的账号信息失败:`, error);
      return false;
    }
  }

  // 根据索引删除指定账号
  deleteAccountByIndex(index) {
    try {
      const data = this.readData();
      if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
        return false;
      }
      const newAccounts = data.userInfo.accounts.filter(account => account.id !== index);
      data.userInfo.accounts = newAccounts;

      return this.saveData(data);
    } catch (error) {
      console.error(`删除索引 ${index} 的账号失败:`, error);
      return false;
    }
  }

  // 添加新账号
  addAccount(newAccount) {
    try {
      const data = this.readData() || { userInfo: { accounts: [] } };

      if (!data.userInfo) {
        data.userInfo = { accounts: [] };
      }
      if (!Array.isArray(data.userInfo.accounts)) {
        data.userInfo.accounts = [];
      }

      // 生成新的ID（最大ID+1）
      const maxId = data.userInfo.accounts.reduce((max, account) =>
        Math.max(max, account.id || 0), 0);

      const accountWithId = {
        ...newAccount,
        id: maxId + 1
      };

      data.userInfo.accounts.push(accountWithId);

      return this.saveData(data);
    } catch (error) {
      console.error('添加新账号失败:', error);
      return false;
    }
  }

  // 获取所有账号数量
  getAccountCount() {
    try {
      const data = this.readData();
      if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
        return 0;
      }

      return data.userInfo.accounts.length;
    } catch (error) {
      console.error('获取账号数量失败:', error);
      return 0;
    }
  }
}

module.exports = { FileStorage };
