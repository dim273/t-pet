const vscode = require('vscode');

/**
 * VSCodeStorage — 基于 VS Code globalState 的存储管理器
 * 
 * 替代原有的 FileStorage（基于 JSON 文件），使用 VS Code 官方持久化 API。
 * 数据存储在 VS Code 全局状态中，与工作区无关，随插件卸载自动清理。
 */
class VSCodeStorage {
	/**
	 * @param {vscode.ExtensionContext['globalState']} globalState - VS Code 扩展全局状态
	 */
	constructor(globalState) {
		this._globalState = globalState;
		this._DATA_KEY = 'algorithmLearning.data'; // 全局存储键名
	}

	// ==================== 底层读写 ====================

	/** 获取完整数据对象 */
	_readAll() {
		return this._globalState.get(this._DATA_KEY, null);
	}

	/** 写入完整数据对象 */
	async _writeAll(data) {
		try {
			await this._globalState.update(this._DATA_KEY, data);
			return true;
		} catch (error) {
			console.error(`[VSCodeStorage] 写入失败:`, error);
			return false;
		}
	}

	// ==================== 账号 CRUD ====================

	/** 获取所有账号列表 */
	getAccounts() {
		const data = this._readAll();
		if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
			return [];
		}
		return data.userInfo.accounts;
	}

	/** 获取账号数量 */
	getAccountCount() {
		return this.getAccounts().length;
	}

	/** 根据 id 获取单个账号 */
	getAccountByIndex(id) {
		try {
			const account = this.getAccounts().find(account => account.id === id);
			return account || null;
		} catch (error) {
			console.error(`[VSCodeStorage] 获取索引 ${id} 的账号信息失败:`, error);
			return null;
		}
	}

	/** 添加新账号 */
	async addAccount(newAccount) {
		try {
			let data = this._readAll();
			if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
				data = { userInfo: { accounts: [] } };
			}

			data.userInfo.accounts.push(newAccount);
			return await this._writeAll(data);
		} catch (error) {
			console.error('[VSCodeStorage] 添加新账号失败:', error);
			return false;
		}
	}

	/** 根据 id 更新账号信息（浅合并） */
	async updateAccountByIndex(id, updatedAccount) {
		try {
			const data = this._readAll();
			if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
				return false;
			}

			const accountIndex = data.userInfo.accounts.findIndex(account => account.id === id);
			if (accountIndex === -1) {
				return false;
			}

			data.userInfo.accounts[accountIndex] = {
				...data.userInfo.accounts[accountIndex],
				...updatedAccount
			};

			console.log("[VSCodeStorage] 更新成功");
			return await this._writeAll(data);
		} catch (error) {
			console.error(`[VSCodeStorage] 更新ID ${id} 的账号信息失败:`, error);
			return false;
		}
	}

	/** 根据 id 删除账号 */
	async deleteAccountByIndex(index) {
		try {
			const data = this._readAll();
			if (!data || !data.userInfo || !Array.isArray(data.userInfo.accounts)) {
				return false;
			}
			const newAccounts = data.userInfo.accounts.filter(account => account.id !== index);
			data.userInfo.accounts = newAccounts;

			return await this._writeAll(data);
		} catch (error) {
			console.error(`[VSCodeStorage] 删除索引 ${index} 的账号失败:`, error);
			return false;
		}
	}
}

module.exports = { VSCodeStorage };
