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
}

module.exports = { FileStorage };
