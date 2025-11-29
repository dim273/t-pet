const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";

// 返回主菜单
function switchPageToMain() {
  if (pageID != "知识树")
    vscode.postMessage({ type: 'switchPageTotree' });
  else
    vscode.postMessage({ type: 'switchPageToMain' });
}

// 初始化知识树
function initTechTree() {
  const techTree = document.getElementById('techTree');
  techTree.innerHTML = '';

  // 创建连接线容器
  const connectionsContainer = document.createElement('div');
  connectionsContainer.className = 'connection-lines';
  techTree.appendChild(connectionsContainer);

  // 为每个层级创建节点
  treeData.forEach((levelData, index) => {
    const treeLevel = document.createElement('div');
    treeLevel.className = 'tech-level';
    treeLevel.dataset.level = index;

    // 添加层级标题
    const levelTitle = document.createElement('div');
    levelTitle.className = 'tech-level-title';
    levelTitle.textContent = levelData.title;
    treeLevel.appendChild(levelTitle);

    // 根据层级类型创建节点
    if (index === 0) {
      // 根节点
      const rootNode = createTechNode(levelData);
      treeLevel.appendChild(rootNode);
    } else {
      // 其他层级的节点
      levelData.nodes.forEach(nodeData => {
        const node = createTechNode(nodeData);
        treeLevel.appendChild(node);
      });
    }

    techTree.appendChild(treeLevel);
  });

  // 绘制连接线
  drawConnections();

  // 更新节点状态
  updateNodeStates();
}

// 创建节点
function createTechNode(nodeData) {
  const node = document.createElement('div');
  node.className = 'tech-node';
  node.dataset.id = nodeData.id || nodeData.title;

  // 根据类型添加相应样式类
  if (nodeData.type === 'root') {
    node.classList.add('root');
  } else if (nodeData.type === 'ultimate') {
    node.classList.add('ultimate');
  }

  // 如果节点已解锁，添加相应样式
  if (nodeData.unlocked) {
    node.classList.add('unlocked');
  }

  // 添加节点图标和标题
  const icon = document.createElement('div');
  icon.className = 'tech-node-icon';
  icon.textContent = nodeData.icon;

  const title = document.createElement('div');
  title.className = 'tech-node-title';
  title.textContent = nodeData.id || nodeData.title;

  node.appendChild(icon);
  node.appendChild(title);

  // 添加点击事件
  node.addEventListener('click', function () {
    if (nodeData.type === "root") return;   // 若为根节点, 暂无点击事件

    // 下面的注释是为方便测试，实际应该启用
    //if ((!nodeData.unlocked && CheckParentUnlocked(nodeData)) || nodeData.unlocked) {

    if (nodeData.lay == 1) {
      // 通过消息机制通知扩展端切换子树
      vscode.postMessage({
        type: 'switchToSubTree',
        subTreeId: nodeData.id || nodeData.title
      });
    }
    else if (nodeData.lay == 2) {
      if (nodeData.questionList != 0)
        switchPageToProblemList(nodeData.questionList);
    }
    //}
    //if (nodeData.questionList === 0)
    //  unlockNode(nodeData.id || nodeData.title);
  });

  return node;
}

// 切换页面到对应题单
function switchPageToProblemList(ListId) {
  vscode.postMessage({ type: 'switchPageToProblemList', listId: ListId });
}

// 解锁节点
function unlockNode(nodeId) {
  // 在数据结构中查找节点
  let nodeToUnlock = null;

  for (const levelData of treeData) {
    if (levelData.nodes) {
      const node = levelData.nodes.find(n => n.id === nodeId);
      if (node) {
        nodeToUnlock = node;
        break;
      }
    } else if (levelData.id === nodeId || levelData.title === nodeId) {
      nodeToUnlock = levelData;
      break;
    }
  }

  if (!nodeToUnlock) return;

  // 检查是否已解锁
  if (nodeToUnlock.unlocked) {
    showMessage("该知识点已经解锁");
    return;
  }

  // 检查所有父节点是否已解锁
  if (!CheckParentUnlocked(nodeToUnlock)) return;

  // 解锁节点
  nodeToUnlock.unlocked = true;
  nodeToUnlock.icon = "⭐"

  // 更新UI
  initTechTree();

  // 显示消息
  showMessage("已解锁: " + nodeId);
}

// 检查所有父节点是否已解锁
function CheckParentUnlocked(nodeToUnlock) {
  if (nodeToUnlock.parent && Array.isArray(nodeToUnlock.parent)) {
    for (const parentId of nodeToUnlock.parent) {
      let parentUnlocked = false;

      for (const levelData of treeData) {
        if (levelData.nodes) {
          const parentNode = levelData.nodes.find(n => n.id === parentId);
          if (parentNode && parentNode.unlocked) {
            parentUnlocked = true;
            break;
          }
        } else if ((levelData.id === parentId || levelData.title === parentId) && levelData.unlocked) {
          parentUnlocked = true;
          break;
        }
      }

      if (!parentUnlocked) {
        showMessage("需要先解锁父节点: " + parentId);
        return false;
      }
    }
    return true;
  }
  return true;
}

// 更新节点状态
function updateNodeStates() {
  // 检查哪些节点是可解锁的
  for (const levelData of treeData) {
    if (levelData.nodes) {
      for (const node of levelData.nodes) {
        if (!node.unlocked && node.parent) {
          // 检查父节点是否已解锁
          let parentUnlocked = false;

          for (const parentLevelData of treeData) {
            if (parentLevelData.nodes) {
              const parentNode = parentLevelData.nodes.find(n => n.id === node.parent);
              if (parentNode && parentNode.unlocked) {
                parentUnlocked = true;
                break;
              }
            } else if ((parentLevelData.id === node.parent || parentLevelData.title === node.parent) && parentLevelData.unlocked) {
              parentUnlocked = true;
              break;
            }
          }

          if (parentUnlocked) {
            // 添加可解锁样式
            const nodeElement = document.querySelector(`[data-id="${node.id}"]`);
            if (nodeElement) {
              nodeElement.classList.add('available');
            }
          }
        }
      }
    }
  }
}

// 绘制连接线
function drawConnections() {
  const connectionsContainer = document.querySelector('.connection-lines');
  connectionsContainer.innerHTML = '';

  // 为每个节点连接到其父节点绘制直线
  for (const levelData of treeData) {
    if (levelData.nodes) {
      for (const node of levelData.nodes) {
        if (node.parent && Array.isArray(node.parent)) {
          for (const parentId of node.parent) {
            // 找到父节点和当前节点的位置
            const parentNode = document.querySelector(`[data-id="${parentId}"]`);
            const currentNode = document.querySelector(`[data-id="${node.id}"]`);

            if (parentNode && currentNode) {
              const parentRect = parentNode.getBoundingClientRect();
              const currentRect = currentNode.getBoundingClientRect();
              const containerRect = connectionsContainer.getBoundingClientRect();

              // 计算相对位置
              const parentX = parentRect.left + parentRect.width / 2 - containerRect.left;
              const parentY = parentRect.bottom - containerRect.top;
              const currentX = currentRect.left + currentRect.width / 2 - containerRect.left;
              const currentY = currentRect.top - containerRect.top;

              // 创建直线连接线
              const line = document.createElement('div');
              line.className = 'connection-line';
              line.style.position = 'absolute';
              line.style.left = parentX + 'px';
              line.style.top = parentY + 'px';
              line.style.width = Math.sqrt(Math.pow(currentX - parentX, 2) + Math.pow(currentY - parentY, 2)) + 'px';
              line.style.transformOrigin = '0 0';
              line.style.transform = `rotate(${Math.atan2(currentY - parentY, currentX - parentX)}rad)`;
              line.style.height = '2px';
              line.style.backgroundColor = node.unlocked ? '#4CAF50' : '#888';

              connectionsContainer.appendChild(line);
            }
          }
        }
      }
    }
  }
}

// 重置科技树
function resetTechTree() {
  // 重置所有节点状态（除了根节点）
  for (const levelData of treeData) {
    if (levelData.nodes) {
      levelData.nodes.forEach(node => {
        node.unlocked = false;
        node.icon = "🔒"
      });
    } else if (levelData.type !== 'root') {
      levelData.unlocked = false;
    }
  }

  // 重新初始化科技树
  initTechTree();

  // 显示消息
  showMessage("科技树已重置");
}

// 显示消息
function showMessage(message) {
  // 移除已存在的消息弹窗
  const existingPopup = document.querySelector('.message-popup');
  if (existingPopup) {
    existingPopup.remove();
  }

  // 创建新的消息弹窗
  const msgDiv = document.createElement('div');
  msgDiv.className = 'message-popup';
  msgDiv.textContent = message;
  document.body.appendChild(msgDiv);

  // 2秒后自动移除
  setTimeout(() => {
    msgDiv.remove();
  }, 2000);
}

// 页面加载完成后初始化科技树
window.onload = function () {
  // 根据当前子树ID动态设置treeData
  if (window.currentSubTreeId && window.currentSubTreeId !== "知识树") {
    // 根据子树ID找到对应的myNode数据
    for (const levelData of treeMain) {
      if (levelData.nodes) {
        const node = levelData.nodes.find(n => n.id === window.currentSubTreeId);
        if (node && node.myNode) {
          treeData = node.myNode;
          break;
        }
      }
    }
  }
  pageID = window.currentSubTreeId;
  initTechTree();
};

// 窗口大小改变时重新绘制连接线
window.addEventListener('resize', function () {
  drawConnections();
});