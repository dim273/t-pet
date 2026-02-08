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
  const candidateProblems = allProblems.filter(p => !passedSet.has(p.ref));

  const scoredProblems = candidateProblems.map(problem => ({
    ...problem,
    score: computeProblemScore(problem, userProfile)
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

function computeProblemScore(problem, userProfile) {
  let score = 0;

  const difficultyScore = difficultyScoreMap[problem.difficulty] || 1;

  const tags = problem.tags || [];
  const weakTags = userProfile.weakTags || [];
  const currentTags = userProfile.currentTags || [];

  tags.forEach(tag => {
    if (weakTags.includes(tag)) score += 3;
    if (currentTags.includes(tag)) score += 1;
  });

  const targetDifficulty = userProfile.targetDifficulty || "easy";
  const targetScore = difficultyScoreMap[targetDifficulty] || 1;

  score += 5 - Math.abs(difficultyScore - targetScore) * 2;

  return score;
}
