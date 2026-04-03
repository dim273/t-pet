//题目难度映射
const difficultyScoreMap = {
  easy: 1,
  medium: 2,
  hard: 3
};

export function recommendProblems(allProblemSets, userProfile, recommendCount = 5) {
  const allProblems = flattenAllProblems(allProblemSets);

  if (!allProblems || allProblems.length === 0) {
    return [];
  }

  const passedSet = new Set(userProfile.passedProblems || []);
  const masteryByTag = buildTagMastery(allProblems, passedSet);
  const candidateProblems = allProblems.filter(p => !passedSet.has(p.ref));

  const scoredProblems = candidateProblems.map(problem => ({
    ...problem,
    score: computeProblemScore(problem, userProfile, masteryByTag)
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

function computeProblemScore(problem, userProfile, masteryByTag) {
  let score = 0;

  const difficultyScore = difficultyScoreMap[problem.difficulty] || 1;

  const tags = problem.tags || [];
  const weakTags = userProfile.weakTags || [];
  const currentTags = userProfile.currentTags || [];

  tags.forEach(tag => {
    if (weakTags.includes(tag)) score += 3;
    if (currentTags.includes(tag)) score += 1;
    const tagMastery = masteryByTag[tag] || 0;
    score += 2 - Math.abs(tagMastery - 0.6) * 4;
  });

  const targetDifficulty = userProfile.targetDifficulty || "easy";
  const targetScore = difficultyScoreMap[targetDifficulty] || 1;

  score += 5 - Math.abs(difficultyScore - targetScore) * 2;
  score += getProgressiveChallengeBonus(problem, userProfile, difficultyScoreMap[targetDifficulty] || 1);
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

function getProgressiveChallengeBonus(problem, userProfile, targetScore) {
  const recentDifficulty = userProfile.recentDifficulty || userProfile.targetDifficulty || "easy";
  const recentScore = difficultyScoreMap[recentDifficulty] || 1;
  const currentScore = difficultyScoreMap[problem.difficulty] || 1;
  const towardTarget = Math.max(0, targetScore - recentScore);
  const step = currentScore - recentScore;

  if (towardTarget === 0) {
    return step === 0 ? 1 : -1;
  }

  if (step === towardTarget || step === towardTarget - 1) {
    return 2;
  }

  if (step > towardTarget + 1) {
    return -2;
  }

  return 0.5;
}

export const __test__ = {
  flattenAllProblems,
  computeProblemScore,
  buildTagMastery,
  getProgressiveChallengeBonus
};
