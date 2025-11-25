const vscode = acquireVsCodeApi();
const MainOrigin = "vscode-file://vscode-app";
function switchPageToMain() {
  vscode.postMessage({ type: 'switchPageToMain' });
}


// 初始化科技树
function initTechTree() {
  const techTree = document.getElementById('techTree');
  techTree.innerHTML = '';

  // 创建连接线容器
  const connectionsContainer = document.createElement('div');
  connectionsContainer.className = 'connection-lines';
  techTree.appendChild(connectionsContainer);

  // 为每个层级创建科技节点
  techData.forEach((levelData, index) => {
    const techLevel = document.createElement('div');
    techLevel.className = 'tech-level';
    techLevel.dataset.level = index;

    // 添加层级标题
    const levelTitle = document.createElement('div');
    levelTitle.className = 'tech-level-title';
    levelTitle.textContent = levelData.title;
    techLevel.appendChild(levelTitle);

    // 根据层级类型创建节点
    if (index === 0) {
      // 根节点
      const rootNode = createTechNode(levelData);
      techLevel.appendChild(rootNode);
    } else {
      // 其他层级的节点
      levelData.nodes.forEach(nodeData => {
        const node = createTechNode(nodeData);
        techLevel.appendChild(node);
      });
    }

    techTree.appendChild(techLevel);
  });

  // 绘制连接线
  drawConnections();

  // 更新节点状态
  updateNodeStates();
}

// 创建科技节点
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
    unlockNode(nodeData.id || nodeData.title);
  });

  return node;
}

// 解锁节点
function unlockNode(nodeId) {
  // 在数据结构中查找节点
  let nodeToUnlock = null;

  for (const levelData of techData) {
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

  // 检查父节点是否已解锁
  if (nodeToUnlock.parent) {
    let parentUnlocked = false;

    for (const levelData of techData) {
      if (levelData.nodes) {
        const parentNode = levelData.nodes.find(n => n.id === nodeToUnlock.parent);
        if (parentNode && parentNode.unlocked) {
          parentUnlocked = true;
          break;
        }
      } else if ((levelData.id === nodeToUnlock.parent || levelData.title === nodeToUnlock.parent) && levelData.unlocked) {
        parentUnlocked = true;
        break;
      }
    }

    if (!parentUnlocked) {
      showMessage("需要先解锁父节点: " + nodeToUnlock.parent);
      return;
    }
  }

  // 解锁节点
  nodeToUnlock.unlocked = true;
  nodeToUnlock.icon = "⭐"

  // 更新UI
  initTechTree();

  // 显示消息
  showMessage("已解锁: " + nodeId);
}

// 更新节点状态
function updateNodeStates() {
  // 检查哪些节点是可解锁的
  for (const levelData of techData) {
    if (levelData.nodes) {
      for (const node of levelData.nodes) {
        if (!node.unlocked && node.parent) {
          // 检查父节点是否已解锁
          let parentUnlocked = false;

          for (const parentLevelData of techData) {
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

  // 为每个节点连接到其父节点绘制线
  for (const levelData of techData) {
    if (levelData.nodes) {
      for (const node of levelData.nodes) {
        if (node.parent) {
          // 找到父节点和当前节点的位置
          const parentNode = document.querySelector(`[data-id="${node.parent}"]`);
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

            // 创建垂直线（从父节点向下）
            const verticalLine = document.createElement('div');
            verticalLine.className = 'connection-line vertical-line';
            verticalLine.style.left = parentX + 'px';
            verticalLine.style.bottom = (containerRect.height - parentY) + 'px';

            if (node.unlocked) {
              verticalLine.classList.add('unlocked');
            }

            // 创建水平线（从垂直线到当前节点）
            const horizontalLine = document.createElement('div');
            horizontalLine.className = 'connection-line horizontal-line';
            horizontalLine.style.top = parentY + 'px';
            horizontalLine.style.left = Math.min(parentX, currentX) + 'px';
            horizontalLine.style.width = Math.abs(currentX - parentX) + 'px';

            // 创建第二条垂直线（从水平线到当前节点）
            const verticalLine2 = document.createElement('div');
            verticalLine2.className = 'connection-line vertical-line';
            verticalLine2.style.left = currentX + 'px';
            verticalLine2.style.top = parentY + 'px';
            verticalLine2.style.height = (currentY - parentY) + 'px';
            verticalLine2.style.bottom = 'auto';

            if (node.unlocked) {
              verticalLine2.classList.add('unlocked');
              horizontalLine.classList.add('unlocked');
            }

            connectionsContainer.appendChild(verticalLine);
            connectionsContainer.appendChild(horizontalLine);
            connectionsContainer.appendChild(verticalLine2);
          }
        }
      }
    }
  }
}

// 重置科技树
function resetTechTree() {
  // 重置所有节点状态（除了根节点）
  for (const levelData of techData) {
    if (levelData.nodes) {
      levelData.nodes.forEach(node => {
        node.unlocked = false;
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
  initTechTree();
};

// 窗口大小改变时重新绘制连接线
window.addEventListener('resize', function () {
  drawConnections();
});