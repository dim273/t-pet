import assert from "assert";
import { recommendProblems, __test__ } from "../media/RecommendProblemList/recommendation.js";

const mockProblemSets = {
  list_1: {
    problems: [
      { ref: 1, title: "A", difficulty: "easy", tags: ["数组"] },
      { ref: 2, title: "B", difficulty: "medium", tags: ["数组", "哈希"] }
    ]
  },
  list_2: {
    problems: [
      { ref: 3, title: "C", difficulty: "hard", tags: ["动态规划"] },
      { ref: 4, title: "D", difficulty: "medium", tags: ["哈希"] }
    ]
  }
};

describe("recommendation", () => {
  it("能够扁平化题单并保留 listId", () => {
    const flat = __test__.flattenAllProblems(mockProblemSets);
    assert.strictEqual(flat.length, 4);
    assert.ok(flat.some(problem => problem.listId === "list_1"));
    assert.ok(flat.some(problem => problem.listId === "list_2"));
  });

  it("会过滤已通过题目", () => {
    const result = recommendProblems(mockProblemSets, {
      passedProblems: [1, 2]
    }, 10);
    assert.ok(result.every(problem => problem.ref !== 1 && problem.ref !== 2));
  });

  it("会优先推荐接近目标难度且弱项标签的题目", () => {
    const result = recommendProblems(mockProblemSets, {
      passedProblems: [],
      weakTags: ["哈希"],
      currentTags: ["数组"],
      targetDifficulty: "medium",
      recentDifficulty: "easy"
    }, 2);
    assert.strictEqual(result.length, 2);
    assert.strictEqual(result[0].ref, 2);
  });

  it("标签掌握度计算正确", () => {
    const mastery = __test__.buildTagMastery([
      { ref: 1, tags: ["数组", "哈希"] },
      { ref: 2, tags: ["数组"] },
      { ref: 3, tags: ["哈希"] }
    ], new Set([1, 3]));

    assert.strictEqual(mastery["数组"], 0.5);
    assert.strictEqual(mastery["哈希"], 1);
  });

  it("渐进挑战奖励遵循目标难度", () => {
    const bonus = __test__.getProgressiveChallengeBonus(
      { difficulty: "medium" },
      { recentDifficulty: "easy", targetDifficulty: "hard" },
      3
    );

    assert.ok(bonus > 0);
  });
});
