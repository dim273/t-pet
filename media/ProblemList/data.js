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
  },
  "list_6": {
    name: "结构体",
    problems: [
      {
        id: 1,
        title: "三元组排序",
        url: "https://www.acwing.com/problem/content/864",
        difficulty: "easy",
        passed: false,
        tags: ["排序", "结构体"],
        ref: 24
      },
      {
        id: 2,
        title: "结构体之时间设计",
        url: "https://www.dotcpp.com/oj/problem1049.html",
        difficulty: "easy",
        passed: false,
        tags: ["结构体"],
        ref: 25
      },
      {
        id: 3,
        title: "结构体之成绩记录",
        url: "https://www.dotcpp.com/oj/problem1050.html",
        difficulty: "easy",
        passed: false,
        tags: ["结构体"],
        ref: 26
      },
      {
        id: 4,
        title: "结构体之成绩统计2",
        url: "https://www.dotcpp.com/oj/problem1051.html",
        difficulty: "easy",
        passed: false,
        tags: ["结构体"],
        ref: 27
      }
    ]
  },
  "list_7": {
    name: "函数与递归",
    problems: [
      {
        id: 1,
        title: "求正整数 2 和 n 之间的完全数",
        url: "https://www.luogu.com.cn/problem/B2127",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 28
      },
      {
        id: 2,
        title: "素数个数",
        url: "https://www.luogu.com.cn/problem/B2128",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 29
      },
      {
        id: 3,
        title: "进制转换",
        url: "https://www.luogu.com.cn/problem/B2143",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 30
      },
      {
        id: 4,
        title: "区间内的真素数",
        url: "https://www.luogu.com.cn/problem/B2139",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 31
      },
      {
        id: 5,
        title: "灵感",
        url: "https://www.luogu.com.cn/problem/B4026",
        difficulty: "easy",
        passed: false,
        tags: ["分支结构", "O2优化"],
        ref: 32
      }
    ]
  },
  "list_8": {
    name: "数据库常用函数",
    problems: [
      {
        id: 1,
        title: "三角形面积",
        url: "https://www.luogu.com.cn/problem/P5708",
        difficulty: "easy",
        passed: false,
        tags: ["无"],
        ref: 33
      },
      {
        id: 2,
        title: "幂次方",
        url: "https://www.luogu.com.cn/problem/P1010",
        difficulty: "easy",
        passed: false,
        tags: ["数学", "递归", "分治"],
        ref: 34
      },
      {
        id: 3,
        title: "分数到小数",
        url: "https://leetcode.cn/problems/fraction-to-recurring-decimal/description/",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "数学", "哈希表"],
        ref: 35
      }
    ]
  },
  "list_9": {
    name: "模拟",
    problems: [
      {
        id: 1,
        title: "扫雷游戏",
        url: "https://www.luogu.com.cn/problem/P2670",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "搜索", "枚举", "模拟"],
        ref: 36
      },
      {
        id: 2,
        title: "乒乓球",
        url: "https://www.luogu.com.cn/problem/P1042",
        difficulty: "easy",
        passed: false,
        tags: ["模拟", "字符串"],
        ref: 37
      },
      {
        id: 3,
        title: "生活大爆炸版石头剪刀布",
        url: "https://www.luogu.com.cn/problem/P1328",
        difficulty: "easy",
        passed: false,
        tags: ["模拟"],
        ref: 38
      },
      {
        id: 4,
        title: "字符串的展开",
        url: "https://www.luogu.com.cn/problem/P1098",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "模拟"],
        ref: 39
      },
      {
        id: 5,
        title: "帮贡排序",
        url: "https://www.luogu.com.cn/problem/P1786",
        difficulty: "easy",
        passed: false,
        tags: ["模拟", "排序"],
        ref: 40
      }
    ]
  },
  "list_10": {
    name: "枚举",
    problems: [
      {
        id: 1,
        title: "三连击（升级版）",
        url: "https://www.luogu.com.cn/problem/P1618",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "枚举", "模拟"],
        ref: 41
      },
      {
        id: 2,
        title: "最大公约数和最小公倍数问题",
        url: "https://www.luogu.com.cn/problem/P1029",
        difficulty: "easy",
        passed: false,
        tags: ["枚举", "数学"],
        ref: 42
      },
      {
        id: 3,
        title: "火柴棒等式",
        url: "https://www.luogu.com.cn/problem/P1149",
        difficulty: "easy",
        passed: false,
        tags: ["搜索", "枚举"],
        ref: 43
      },
      {
        id: 4,
        title: "K皇后",
        url: "https://www.luogu.com.cn/problem/P2105",
        difficulty: "medium",
        passed: false,
        tags: ["枚举"],
        ref: 44
      },
      {
        id: 5,
        title: "小 Y 拼木棒",
        url: "https://www.luogu.com.cn/problem/P3799",
        difficulty: "medium",
        passed: false,
        tags: ["枚举", "数学"],
        ref: 45
      }
    ]
  },
  "list_11": {
    name: "递推",
    problems: [
      {
        id: 1,
        title: "禽兽的传染病",
        url: "https://www.luogu.com.cn/problem/P1634",
        difficulty: "easy",
        passed: false,
        tags: ["数学", "递推", "模拟"],
        ref: 46
      },
      {
        id: 2,
        title: "快速幂",
        url: "https://www.luogu.com.cn/problem/P1226",
        difficulty: "easy",
        passed: false,
        tags: ["递推", "数学", "递归"],
        ref: 47
      },
      {
        id: 3,
        title: "斐波那契数列（升级版）",
        url: "https://www.luogu.com.cn/problem/P2626",
        difficulty: "easy",
        passed: false,
        tags: ["递推", "模拟"],
        ref: 48
      },
      {
        id: 4,
        title: "三角形计数",
        url: "https://www.luogu.com.cn/problem/P2807",
        difficulty: "easy",
        passed: false,
        tags: ["递推"],
        ref: 49
      },
      {
        id: 5,
        title: "Hanoi 双塔问题",
        url: "https://www.luogu.com.cn/problem/P1096",
        difficulty: "medium",
        passed: false,
        tags: ["递推", "数学", "递归", "高精度"],
        ref: 50
      }
    ]
  },
  "list_12": {
    name: "二分",
    problems: [
      {
        id: 1,
        title: "x的平方根 ",
        url: "https://leetcode.cn/problems/sqrtx/description/",
        difficulty: "easy",
        passed: false,
        tags: ["数学", "二分"],
        ref: 51
      },
      {
        id: 2,
        title: "切绳子",
        url: "https://www.luogu.com.cn/problem/P1577",
        difficulty: "medium",
        passed: false,
        tags: ["二分"],
        ref: 52
      },
      {
        id: 3,
        title: "吃冰棍",
        url: "https://www.luogu.com.cn/problem/B3629",
        difficulty: "easy",
        passed: false,
        tags: ["二分"],
        ref: 53
      },
      {
        id: 4,
        title: "奇怪的函数",
        url: "https://www.luogu.com.cn/problem/P2759",
        difficulty: "medium",
        passed: false,
        tags: ["二分", "数学"],
        ref: 54
      },
      {
        id: 5,
        title: "查找不重复元素出现的位置",
        url: "https://www.luogu.com.cn/problem/B2166",
        difficulty: "medium",
        passed: false,
        tags: ["二分"],
        ref: 55
      }
    ]
  }
};
