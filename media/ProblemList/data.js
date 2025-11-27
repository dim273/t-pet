// 题单数据
/*
    {
      id:         // 题目在题单中的序号
      title:      // 题目名称
      url:        // 网址
      difficulty: // 难度
      passed:     // 是否通过
      tags:       // 标签
      ref:        // 在题库中的编号
    }

*/

const problemSets = {
  "list_1": {
    problems: [
      {
        id: 1,
        title: "整型与布尔型的转换",
        url: "https://www.luogu.com.cn/problem/B2019",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 1
      },
      {
        id: 2,
        title: "输出浮点数",
        url: "https://www.luogu.com.cn/problem/B2024",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 2
      },
      {
        id: 3,
        title: "输出保留3位小数的浮点数",
        url: "https://www.luogu.com.cn/problem/B2021",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 3
      },
      {
        id: 4,
        title: "统计数字字符个数",
        url: "https://www.luogu.com.cn/problem/B2019",
        difficulty: "easy",
        passed: false,
        tags: ["字符串"],
        ref: 4
      },
      {
        id: 5,
        title: "打印字符",
        url: "https://www.luogu.com.cn/problem/B2018",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 5
      }
    ]
  },
  "dynamic-programming": {
    name: "动态规划专题",
    description: "动态规划经典题目",
    problems: [
      {
        id: 101,
        title: "斐波那契数列",
        url: "https://leetcode-cn.com/problems/fibonacci-number/",
        difficulty: "easy",
        passed: true,
        tags: ["动态规划"],
        lastAttempt: "2023-05-20"
      },
      {
        id: 102,
        title: "爬楼梯",
        url: "https://leetcode-cn.com/problems/climbing-stairs/",
        difficulty: "easy",
        passed: true,
        tags: ["动态规划"],
        lastAttempt: "2023-05-18"
      },
      {
        id: 103,
        title: "最长递增子序列",
        url: "https://leetcode-cn.com/problems/longest-increasing-subsequence/",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "二分查找"],
        lastAttempt: "2023-05-16"
      },
      {
        id: 104,
        title: "零钱兑换",
        url: "https://leetcode-cn.com/problems/coin-change/",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划"],
        lastAttempt: "2023-05-14"
      },
      {
        id: 105,
        title: "编辑距离",
        url: "https://leetcode-cn.com/problems/edit-distance/",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划"],
        lastAttempt: "2023-05-12"
      }
    ]
  },
  "data-structures": {
    name: "数据结构基础",
    description: "常见数据结构练习题",
    problems: [
      {
        id: 201,
        title: "反转链表",
        url: "https://leetcode-cn.com/problems/reverse-linked-list/",
        difficulty: "easy",
        passed: true,
        tags: ["链表"],
        lastAttempt: "2023-05-22"
      },
      {
        id: 202,
        title: "有效的括号",
        url: "https://leetcode-cn.com/problems/valid-parentheses/",
        difficulty: "easy",
        passed: true,
        tags: ["栈", "字符串"],
        lastAttempt: "2023-05-20"
      },
      {
        id: 203,
        title: "二叉树的层序遍历",
        url: "https://leetcode-cn.com/problems/binary-tree-level-order-traversal/",
        difficulty: "medium",
        passed: false,
        tags: ["树", "广度优先搜索"],
        lastAttempt: "2023-05-18"
      },
      {
        id: 204,
        title: "实现 Trie (前缀树)",
        url: "https://leetcode-cn.com/problems/implement-trie-prefix-tree/",
        difficulty: "medium",
        passed: false,
        tags: ["设计", "字典树"],
        lastAttempt: "2023-05-16"
      }
    ]
  }
};

// 当前选中的题单
let currentProblemSet = "dynamic-programming";

// 获取当前题单的题目列表
function getCurrentProblems() {
  return problemSets[currentProblemSet].problems;
}

// 获取所有题单信息
function getProblemSetInfo() {
  return Object.keys(problemSets).map(key => ({
    id: key,
    name: problemSets[key].name,
    description: problemSets[key].description,
    problemCount: problemSets[key].problems.length
  }));
}
