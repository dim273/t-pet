//题目难度映射
const difficultyScoreMap = {
  easy: 1,
  medium: 2,
  hard: 3
};

// 导入知识树数据
//import { treeData } from '../TreeNode/data.js';
treeData = window.treeData;
// 构建知识树节点映射，方便快速查找
function buildTreeNodeMap() {
  const nodeMap = new Map();

  function traverseNodes(nodes) {
    if (!nodes) return;

    nodes.forEach(node => {
      if (node.id) {
        nodeMap.set(node.id, node);
      }
      if (node.nodes) {
        traverseNodes(node.nodes);
      }
      if (node.myNode) {
        node.myNode.forEach(level => {
          if (level.nodes) {
            traverseNodes(level.nodes);
          }
        });
      }
    });
  }

  if (Array.isArray(treeData)) {
    treeData.forEach(level => {
      if (level.nodes) {
        traverseNodes(level.nodes);
      }
    });
  }

  return nodeMap;
}

// 构建题单到知识节点的映射
function buildQuestionListToNodeMap() {
  const map = new Map();
  const nodeMap = buildTreeNodeMap();

  nodeMap.forEach(node => {
    if (node.questionList && node.questionList > 0) {
      map.set(node.questionList, node);
    }
  });

  return map;
}

// 分析用户在知识树上的学习进度
function analyzeKnowledgeTreeProgress(userProfile) {
  const nodeMap = buildTreeNodeMap();
  const passedSet = new Set(userProfile.passedProblems || []);
  const questionListToNodeMap = buildQuestionListToNodeMap();

  const progress = {
    unlockedNodes: new Set(),
    completedNodes: new Set(),
    currentLearningPath: [],
    nextRecommendedNodes: []
  };

  // 标记已解锁和已完成的节点
  nodeMap.forEach(node => {
    if (node.unlocked) {
      progress.unlockedNodes.add(node.id);
    }

    // 检查节点是否已完成（对应题单的题目是否都已通过）
    if (node.questionList && node.questionList > 0) {
      const nodeProblems = userProfile.problemSets?.[`list_${node.questionList}`]?.problems || [];
      const allPassed = nodeProblems.every(problem => passedSet.has(problem.ref));
      if (allPassed) {
        progress.completedNodes.add(node.id);
      }
    }
  });

  // 构建当前学习路径和推荐的下一个节点
  function findPathAndRecommendations(nodeId, path = []) {
    const node = nodeMap.get(nodeId);
    if (!node) return;

    const newPath = [...path, nodeId];

    // 如果节点已完成，继续探索其子节点
    if (progress.completedNodes.has(nodeId) && node.children && node.children.length > 0) {
      node.children.forEach(childId => {
        if (childId) { // 跳过空字符串
          findPathAndRecommendations(childId, newPath);
        }
      });
    }
    // 如果节点已解锁但未完成，将其加入当前学习路径
    else if (progress.unlockedNodes.has(nodeId) && !progress.completedNodes.has(nodeId)) {
      progress.currentLearningPath = newPath;
    }
    // 如果节点未解锁，但父节点已完成，将其加入推荐节点
    else if (!progress.unlockedNodes.has(nodeId) && node.parent) {
      const allParentsCompleted = node.parent.every(parentId =>
        progress.completedNodes.has(parentId)
      );
      if (allParentsCompleted) {
        progress.nextRecommendedNodes.push(nodeId);
      }
    }
  }

  // 从根节点开始分析
  if (treeData && treeData.length > 0) {
    const rootNodes = treeData[0]?.nodes || [];
    rootNodes.forEach(rootNode => {
      if (rootNode.id) {
        findPathAndRecommendations(rootNode.id);
      }
    });
  }

  return progress;
}

export function recommendProblems(allProblemSets, userProfile, recommendCount = 5) {
  const allProblems = flattenAllProblems(allProblemSets);

  if (!allProblems || allProblems.length === 0) {
    return [];
  }

  const passedSet = new Set(userProfile.passedProblems || []);
  const masteryByTag = buildTagMastery(allProblems, passedSet);
  const candidateProblems = allProblems.filter(p => !passedSet.has(p.ref));

  // 分析知识树进度
  const knowledgeTreeProgress = analyzeKnowledgeTreeProgress(userProfile);
  const questionListToNodeMap = buildQuestionListToNodeMap();

  const scoredProblems = candidateProblems.map(problem => ({
    ...problem,
    score: computeProblemScore(problem, userProfile, masteryByTag, knowledgeTreeProgress, questionListToNodeMap)
  }));

  scoredProblems.sort((a, b) => b.score - a.score);

  return scoredProblems.slice(0, recommendCount);
}

// 支持两种输入：对象 problemSets 或者数组 allProblems
function flattenAllProblems(allProblemSets) {
  if (!allProblemSets) return [];

  let all = [];

  // 如果已经是数组，直接返回
  if (Array.isArray(allProblemSets)) {
    return allProblemSets;
  }

  // 如果是对象 {list_1:{problems:[]}}
  for (const listKey in allProblemSets) {
    const list = allProblemSets[listKey];
    if (list && Array.isArray(list.problems)) {
      all = all.concat(list.problems.map(p => ({ ...p, listId: listKey })));
    }
  }

  return all;
}

function computeProblemScore(problem, userProfile, masteryByTag, knowledgeTreeProgress, questionListToNodeMap) {
  let score = 0;

  const difficultyScore = difficultyScoreMap[problem.difficulty] || 1;

  const tags = problem.tags || [];

  tags.forEach(tag => {
    const tagMastery = masteryByTag[tag] || 0;
    score += 2 - Math.abs(tagMastery - 0.6) * 4;
  });

  // 加入知识树相关的分数
  let nodeStatus = "unlocked";
  if (problem.listId) {
    // 从listId中提取题单编号，例如从"list_1"中提取1
    const listNumber = parseInt(problem.listId.replace('list_', ''));
    if (!isNaN(listNumber)) {
      const node = questionListToNodeMap.get(listNumber);
      if (node) {
        // 如果题目所在节点在当前学习路径中，增加分数
        if (knowledgeTreeProgress.currentLearningPath.includes(node.id)) {
          score += 5;
          nodeStatus = "current";
        }
        // 如果题目所在节点是推荐的下一个节点，增加分数
        else if (knowledgeTreeProgress.nextRecommendedNodes.includes(node.id)) {
          score += 3;
          nodeStatus = "next";
        }
        // 如果题目所在节点已解锁，增加分数
        else if (knowledgeTreeProgress.unlockedNodes.has(node.id)) {
          score += 2;
          nodeStatus = "unlocked";
        }
        // 如果题目所在节点已完成，增加分数
        else if (knowledgeTreeProgress.completedNodes.has(node.id)) {
          score += 1;
          nodeStatus = "completed";
        }
        // 如果题目所在节点未解锁，增加基础分数
        else {
          score += 0.5;
          nodeStatus = "locked";
        }
      }
    }
  }

  // 根据节点状态调整难度偏好
  let targetDifficultyScore = 1; // 默认简单
  switch (nodeStatus) {
    case "completed":
      targetDifficultyScore = 3; // 已完成节点，偏好困难
      break;
    case "current":
    case "next":
      targetDifficultyScore = 2; // 当前学习路径或推荐节点，偏好中等
      break;
    case "unlocked":
      targetDifficultyScore = 2; // 已解锁但未在当前路径，偏好中等
      break;
    case "locked":
      targetDifficultyScore = 1; // 未解锁节点，偏好简单
      break;
  }

  // 计算难度匹配分数
  score += 5 - Math.abs(difficultyScore - targetDifficultyScore) * 2;
  score += Math.min(tags.length, 3) * 0.2;

  return score;
}

function buildTagMastery(allProblems, passedSet) {
  const tagStats = {};

  allProblems.forEach(problem => {
    const tags = problem.tags || [];
    tags.forEach(tag => {
      if (!tagStats[tag]) {
        tagStats[tag] = { total: 0, passed: 0 };
      }
      tagStats[tag].total += 1;
      if (passedSet.has(problem.ref)) {
        tagStats[tag].passed += 1;
      }
    });
  });

  return Object.keys(tagStats).reduce((acc, tag) => {
    const stat = tagStats[tag];
    acc[tag] = stat.total > 0 ? stat.passed / stat.total : 0;
    return acc;
  }, {});
}



export const __test__ = {
  flattenAllProblems,
  computeProblemScore,
  buildTagMastery,
  buildTreeNodeMap,
  buildQuestionListToNodeMap,
  analyzeKnowledgeTreeProgress
};
