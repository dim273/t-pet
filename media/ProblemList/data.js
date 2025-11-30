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
  },
  "list_13": {
    name: "递归",
    problems: [
      {
        id: 1,
        title: "求正整数 2 和 n 之间的完全数",
        url: "https://www.luogu.com.cn/problem/B2127",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 56
      },
      {
        id: 2,
        title: "素数个数",
        url: "https://www.luogu.com.cn/problem/B2128",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 57
      },
      {
        id: 3,
        title: "进制转换",
        url: "https://www.luogu.com.cn/problem/B2143",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 58
      },
      {
        id: 4,
        title: "区间内的真素数",
        url: "https://www.luogu.com.cn/problem/B2139",
        difficulty: "easy",
        passed: false,
        tags: ["函数与递归"],
        ref: 59
      },
      {
        id: 5,
        title: "灵感",
        url: "https://www.luogu.com.cn/problem/B4026",
        difficulty: "easy",
        passed: false,
        tags: ["分支结构", "O2优化"],
        ref: 60
      }
    ]
  },
  "list_14": {
    name: "贪心",
    problems: [
      {
        id: 1,
        title: "种花问题",
        url: "https://leetcode.cn/problems/can-place-flowers/description/",
        difficulty: "easy",
        passed: false,
        tags: ["贪心", "数组"],
        ref: 61
      },
      {
        id: 2,
        title: "盛最多水的容器",
        url: "https://leetcode.cn/problems/container-with-most-water/description/",
        difficulty: "medium",
        passed: false,
        tags: ["贪心", "数组", "双指针"],
        ref: 62
      },
      {
        id: 3,
        title: "独木桥",
        url: "https://www.luogu.com.cn/problem/P1007",
        difficulty: "medium",
        passed: false,
        tags: ["贪心", "模拟"],
        ref: 63
      },
      {
        id: 4,
        title: "删数问题",
        url: "https://www.luogu.com.cn/problem/P1106",
        difficulty: "medium",
        passed: false,
        tags: ["贪心", "字符串"],
        ref: 64
      },
      {
        id: 5,
        title: "矩形分割",
        url: "https://www.luogu.com.cn/problem/P1324",
        difficulty: "medium",
        passed: false,
        tags: ["贪心"],
        ref: 65
      }
    ]
  },
  "list_15": {
    name: "简单排序算法",
    problems: [
      {
        id: 1,
        title: "对链表进行插入排序",
        url: "https://leetcode.cn/problems/insertion-sort-list/description/",
        difficulty: "medium",
        passed: false,
        tags: ["链表", "排序"],
        ref: 66
      },
      {
        id: 2,
        title: "多数元素",
        url: "https://leetcode.cn/problems/majority-element/description/",
        difficulty: "easy",
        passed: false,
        tags: ["排序", "数组", "分治", "计数"],
        ref: 67
      },
      {
        id: 3,
        title: "第k小整数",
        url: "https://www.luogu.com.cn/problem/P1138",
        difficulty: "easy",
        passed: false,
        tags: ["排序", "模拟"],
        ref: 68
      },
      {
        id: 4,
        title: "谁拿了最多奖学金",
        url: "https://www.luogu.com.cn/problem/P1051",
        difficulty: "easy",
        passed: false,
        tags: ["排序", "字符串"],
        ref: 69
      },
      {
        id: 5,
        title: "最大数",
        url: "https://leetcode.cn/problems/largest-number/description/",
        difficulty: "medium",
        passed: false,
        tags: ["贪心", "排序", "字符串"],
        ref: 70
      }
    ]
  },
  "list_16": {
    name: "分治算法",
    problems: [
      {
        id: 1,
        title: "最大子数组和",
        url: "https://leetcode.cn/problems/maximum-subarray/description/",
        difficulty: "medium",
        passed: false,
        tags: ["分治", "数组", "动态规划"],
        ref: 71
      },
      {
        id: 2,
        title: "盛最多水的容器",
        url: "https://leetcode.cn/problems/reverse-bits/description/",
        difficulty: "easy",
        passed: false,
        tags: ["位运算", "分治"],
        ref: 72
      },
      {
        id: 3,
        title: "数组中的第K个最大元素",
        url: "https://leetcode.cn/problems/kth-largest-element-in-an-array/description/ ",
        difficulty: "medium",
        passed: false,
        tags: ["数组", "分治", "快速选择", "排序"],
        ref: 73
      },
      {
        id: 4,
        title: "平面最近点对(加强版)",
        url: "https://www.luogu.com.cn/problem/P1429",
        difficulty: "hard",
        passed: false,
        tags: ["分治", "递归", "计算几何"],
        ref: 74
      }
    ]
  },
  "list_17": {
    name: "前缀和与差分",
    problems: [
      {
        id: 1,
        title: "区域和检索 - 数组不可变",
        url: "https://leetcode.cn/problems/range-sum-query-immutable/description/  ",
        difficulty: "easy",
        passed: false,
        tags: ["设计", "数组", "前缀和"],
        ref: 75
      },
      {
        id: 2,
        title: "和为K的子数组",
        url: "https://leetcode.cn/problems/subarray-sum-equals-k/description/ ",
        difficulty: "medium",
        passed: false,
        tags: ["哈希表", "数组", "前缀和"],
        ref: 76
      },
      {
        id: 3,
        title: "连续数组",
        url: "https://leetcode.cn/problems/contiguous-array/description/",
        difficulty: "medium",
        passed: false,
        tags: ["数组", "哈希表", "前缀和"],
        ref: 77
      },
      {
        id: 4,
        title: "航班预订统计",
        url: "https://leetcode.cn/problems/corporate-flight-bookings/description/?envType=problem-list-v2&envId=prefix-sum",
        difficulty: "medium",
        passed: false,
        tags: ["数组", "前缀和"],
        ref: 78
      },
      {
        id: 5,
        title: "拼车",
        url: "https://leetcode.cn/problems/car-pooling/description/?envType=problem-list-v2&envId=prefix-sum",
        difficulty: "medium",
        passed: false,
        tags: ["数组", "排序", "前缀和", "模拟", "堆"],
        ref: 79
      }
    ]
  },
  "list_18": {
    name: "倍增",
    problems: [
      {
        id: 1,
        title: "调和级数求和",
        url: "https://www.luogu.com.cn/problem/P5702",
        difficulty: "hard",
        passed: false,
        tags: ["数学", "倍增"],
        ref: 80
      },
      {
        id: 2,
        title: "修学旅行",
        url: "https://www.luogu.com.cn/problem/P6043",
        difficulty: "hard",
        passed: false,
        tags: ["数学", "倍增"],
        ref: 81
      },
      {
        id: 3,
        title: "整式递推",
        url: "https://www.luogu.com.cn/problem/P6115",
        difficulty: "hard",
        passed: false,
        tags: ["数学", "倍增"],
        ref: 82
      },
      {
        id: 4,
        title: "[ICPC 2022 Xi'an R] Contests",
        url: "https://www.luogu.com.cn/problem/P9361",
        difficulty: "hard",
        passed: false,
        tags: ["倍增"],
        ref: 83
      },
      {
        id: 5,
        title: "魔法值",
        url: "https://www.luogu.com.cn/problem/P6569",
        difficulty: "hard",
        passed: false,
        tags: ["倍增", "矩阵运算"],
        ref: 84
      }
    ]
  },
  "list_19": {
    name: "DFS",
    problems: [
      {
        id: 1,
        title: "八皇后",
        url: "https://www.luogu.com.cn/problem/P1219",
        difficulty: "medium",
        passed: false,
        tags: ["搜索", "深度优先搜索"],
        ref: 85
      },
      {
        id: 2,
        title: "字典序排数",
        url: "https://leetcode.cn/problems/lexicographical-numbers/description/?envType=problem-list-v2&envId=depth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["深度优先搜索", "字典树"],
        ref: 86
      },
      {
        id: 3,
        title: "吃奶酪",
        url: "https://www.luogu.com.cn/problem/P1433",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划DP", "搜索", "深度优先搜索", "剪枝", "记忆化搜索"],
        ref: 87
      },
      {
        id: 4,
        title: "扫雷游戏",
        url: "https://leetcode.cn/problems/minesweeper/description/?envType=problem-list-v2&envId=depth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["深度优先搜索", "广度优先搜索", "数组", "矩阵"],
        ref: 88
      },
      {
        id: 5,
        title: "取数游戏",
        url: "https://www.luogu.com.cn/problem/P1123",
        difficulty: "medium",
        passed: false,
        tags: ["搜索", "深度优先搜索", "枚举"],
        ref: 89
      }
    ]
  },
  "list_20": {
    name: "BFS",
    problems: [
      {
        id: 1,
        title: "腐烂的橘子",
        url: "https://leetcode.cn/problems/rotting-oranges/description/?envType=problem-list-v2&envId=breadth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["广度优先搜索", "数组", "矩阵"],
        ref: 90
      },
      {
        id: 2,
        title: "跳跃游戏III",
        url: "https://leetcode.cn/problems/jump-game-iii/description/?envType=problem-list-v2&envId=breadth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["广度优先搜索", "数组", "矩阵"],
        ref: 91
      },
      {
        id: 3,
        title: "所有可能的路径",
        url: "https://leetcode.cn/problems/all-paths-from-source-to-target/description/?envType=problem-list-v2&envId=breadth-first-search ",
        difficulty: "medium",
        passed: false,
        tags: ["深度优先搜索", "广度优先搜索", "图", "回溯"],
        ref: 92
      },
      {
        id: 4,
        title: "钥匙和房间",
        url: "https://leetcode.cn/problems/keys-and-rooms/?envType=problem-list-v2&envId=breadth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["广度优先搜索", "深度优先搜索", "图"],
        ref: 93
      },
      {
        id: 5,
        title: "01矩阵",
        url: "https://leetcode.cn/problems/01-matrix/description/?envType=problem-list-v2&envId=breadth-first-search",
        difficulty: "medium",
        passed: false,
        tags: ["广度优先搜索", "动态规划DP", "矩阵", "数组"],
        ref: 94
      }
    ]
  }
};
