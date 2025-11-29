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
    name: "基本数据类型",
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
  "list_2": {
    name: "基本运算",
    problems: [
      {
        id: 1,
        title: "计算分数的浮点数值",
        url: "https://www.luogu.com.cn/problem/B2011",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 6
      },
      {
        id: 2,
        title: "入门测试题目",
        url: "https://www.luogu.com.cn/problem/B2001",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构", "模拟"],
        ref: 7
      },
      {
        id: 3,
        title: "计算 (a+b)/c 的值",
        url: "https://www.luogu.com.cn/problem/B2009",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 8
      },
      {
        id: 4,
        title: "计算 (a+b) x c 的值",
        url: "https://www.luogu.com.cn/problem/B2008",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 9
      },
      {
        id: 5,
        title: "带余除法",
        url: "https://www.luogu.com.cn/problem/B2010",
        difficulty: "easy",
        passed: false,
        tags: ["顺序结构"],
        ref: 10
      }
    ]
  },
  "list_3": {
    name: "程序基本语句",
    problems: [
      {
        id: 1,
        title: "求 1+2+3+...+N 的值",
        url: "https://www.luogu.com.cn/problem/B2142",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 11
      },
      {
        id: 2,
        title: "判断数正负",
        url: "https://www.luogu.com.cn/problem/B2035 ",
        difficulty: "easy",
        passed: false,
        tags: ["分支结构"],
        ref: 12
      },
      {
        id: 3,
        title: "星期几",
        url: "https://www.luogu.com.cn/problem/U503340",
        difficulty: "easy",
        passed: false,
        tags: ["无"],
        ref: 13
      },
      {
        id: 4,
        title: "分类平均",
        url: "https://www.luogu.com.cn/problem/P5719",
        difficulty: "easy",
        passed: false,
        tags: ["无"],
        ref: 14
      }
    ]
  },
  "list_4": {
    name: "数组与字符串",
    problems: [
      {
        id: 1,
        title: "小鱼的数字游戏",
        url: "https://www.luogu.com.cn/problem/P1427",
        difficulty: "easy",
        passed: false,
        tags: ["栈"],
        ref: 15
      },
      {
        id: 2,
        title: "找出字符串中第一个匹配项的下标",
        url: "https://leetcode-cn.com/problems/implement-strstr",
        difficulty: "easy",
        passed: false,
        tags: ["字符串"],
        ref: 16
      },
      {
        id: 3,
        title: "小鱼比可爱",
        url: "https://www.luogu.com.cn/problem/P1428",
        difficulty: "easy",
        passed: false,
        tags: ["模拟"],
        ref: 17
      },
      {
        id: 4,
        title: "自动修正",
        url: "https://www.luogu.com.cn/problem/P5733",
        difficulty: "easy",
        passed: false,
        tags: ["无"],
        ref: 18
      },
      {
        id: 5,
        title: "验证回文串",
        url: "https://leetcode-cn.com/problems/valid-palindrome",
        difficulty: "easy",
        passed: false,
        tags: ["字符串"],
        ref: 19
      }
    ]
  },
  "list_5": {
    name: "指针与引用",
    problems: [
      {
        id: 1,
        title: "约瑟夫问题",
        url: "https://www.luogu.com.cn/problem/P1996",
        difficulty: "easy",
        passed: false,
        tags: ["模拟", "队列", "链表", "树状数组"],
        ref: 20
      },
      {
        id: 2,
        title: "【模板】堆",
        url: "https://www.luogu.com.cn/problem/P3378",
        difficulty: "easy",
        passed: false,
        tags: ["堆", "O2优化"],
        ref: 21
      },
      {
        id: 3,
        title: "反转链表",
        url: "https://leetcode.cn/problems/reverse-linked-list",
        difficulty: "easy",
        passed: false,
        tags: ["递归", "链表"],
        ref: 22
      },
      {
        id: 4,
        title: "合并两个有序链表",
        url: "https://leetcode.cn/problems/merge-two-sorted-lists",
        difficulty: "easy",
        passed: false,
        tags: ["递归", "链表"],
        ref: 23
      }
    ]
  }
};
