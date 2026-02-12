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
//passed标签我感觉是没用了，交给之后的人删除吧，题目通没通过应该是存在账号里面的。————jcy

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
        url: "https://www.luogu.com.cn/problem/B2109",
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
        title: "颠倒二进制位",
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
  },
  "list_21": {
    name: "字符串匹配",
    problems: [
      {
        id: 1,
        title: "统计包含给定前缀的字符串",
        url: "https://leetcode.cn/problems/counting-words-with-a-given-prefix/description/",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "前缀匹配"],
        ref: 95
      },
      {
        id: 2,
        title: "找出字符串中第一个匹配项的下标",
        url: "https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/",
        difficulty: "easy",
        passed: false,
        tags: ["字符串", "子串搜索"],
        ref: 96
      },
      {
        id: 3,
        title: "重复的子字符串",
        url: "https://leetcode.cn/problems/repeated-substring-pattern/description/",
        difficulty: "medium",
        passed: false,
        tags: ["字符串", "模式匹配"],
        ref: 97
      },
      {
        id: 4,
        title: "驼峰式匹配",
        url: "https://leetcode.cn/problems/camelcase-matching/description/",
        difficulty: "medium",
        passed: false,
        tags: ["字符串", "模式匹配"],
        ref: 98
      },
      {
        id: 5,
        title: "找到所有好字符串",
        url: "https://leetcode.cn/problems/find-all-good-strings/description/",
        difficulty: "hard",
        passed: false,
        tags: ["字符串", "动态规划", "状态压缩"],
        ref: 99
      }
    ]
  },
  "list_22": {
    name: "栈",
    problems: [
      {
        id: 1,
        title: "最小栈",
        url: "https://leetcode.cn/problems/min-stack/description/",
        difficulty: "medium",
        passed: false,
        tags: ["栈", "设计"],
        ref: 100
      },
      {
        id: 2,
        title: "有效的括号",
        url: "https://leetcode.cn/problems/valid-parentheses/description/",
        difficulty: "easy",
        passed: false,
        tags: ["栈", "字符串"],
        ref: 101
      },
      {
        id: 3,
        title: "简化路径",
        url: "https://leetcode.cn/problems/simplify-path/description/",
        difficulty: "medium",
        passed: false,
        tags: ["栈", "字符串"],
        ref: 102
      },
      {
        id: 4,
        title: "移掉K位数字",
        url: "https://leetcode.cn/problems/remove-k-digits/description/",
        difficulty: "medium",
        passed: false,
        tags: ["栈", "贪心", "字符串"],
        ref: 103
      },
      {
        id: 5,
        title: "后缀表达式",
        url: "https://www.luogu.com.cn/problem/P1449",
        difficulty: "easy",
        passed: false,
        tags: ["栈", "表达式求值"],
        ref: 104
      }
    ]
  },
  "list_23": {
    name: "队列",
    problems: [
      {
        id: 1,
        title: "最近的请求次数",
        url: "https://leetcode.cn/problems/number-of-recent-calls/description/",
        difficulty: "easy",
        passed: false,
        tags: ["队列", "设计"],
        ref: 105
      },
      {
        id: 2,
        title: "图书整理 II",
        url: "https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/description/",
        difficulty: "easy",
        passed: false,
        tags: ["栈", "队列", "设计"],
        ref: 106
      },
      {
        id: 3,
        title: "数据流中的移动平均值",
        url: "https://leetcode.cn/problems/qIsx9U/description/?envType=problem-list-v2&envId=queue",
        difficulty: "easy",
        passed: false,
        tags: ["队列", "设计", "滑动窗口"],
        ref: 107
      },
      {
        id: 4,
        title: "找出游戏的获胜者",
        url: "https://leetcode.cn/problems/find-the-winner-of-the-circular-game/description/?envType=problem-list-v2&envId=queue",
        difficulty: "medium",
        passed: false,
        tags: ["队列", "数学", "递归", "模拟"],
        ref: 108
      },
      {
        id: 5,
        title: "按递增顺序显示卡牌",
        url: "https://leetcode.cn/problems/reveal-cards-in-increasing-order/description/",
        difficulty: "medium",
        passed: false,
        tags: ["队列", "数组", "排序", "模拟"],
        ref: 109
      }
    ]
  },
  "list_24": {
    name: "链表",
    problems: [
      {
        id: 1,
        title: "设计链表",
        url: "https://leetcode.cn/problems/design-linked-list/description/",
        difficulty: "medium",
        passed: false,
        tags: ["链表", "设计"],
        ref: 110
      },
      {
        id: 2,
        title: "奇偶链表",
        url: "https://leetcode.cn/problems/odd-even-linked-list/description/",
        difficulty: "medium",
        passed: false,
        tags: ["链表"],
        ref: 111
      },
      {
        id: 3,
        title: "删除排序链表中的重复元素",
        url: "https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/",
        difficulty: "easy",
        passed: false,
        tags: ["链表"],
        ref: 112
      },
      {
        id: 4,
        title: "合并两个有序链表",
        url: "https://leetcode.cn/problems/merge-two-sorted-lists/description/",
        difficulty: "easy",
        passed: false,
        tags: ["链表", "递归"],
        ref: 113
      },
      {
        id: 5,
        title: "约瑟夫问题",
        url: "https://www.luogu.com.cn/problem/P1996",
        difficulty: "easy",
        passed: false,
        tags: ["链表", "模拟"],
        ref: 114
      }
    ]
  },
  "list_25": {
    name: "一维DP",
    problems: [
      {
        id: 1,
        title: "ICPC 2023 Nanjing R 背包",
        url: "https://www.luogu.com.cn/problem/P13957",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "01背包"],
        ref: 115
      },
      {
        id: 2,
        title: "打家劫舍",
        url: "https://leetcode.cn/problems/house-robber/description/?envType=problem-list-v2&envId=dynamic-programming",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划"],
        ref: 116
      },
      {
        id: 3,
        title: "最大子数组和",
        url: "https://leetcode.cn/problems/maximum-subarray/description/",
        difficulty: "easy",
        passed: false,
        tags: ["动态规划", "数组"],
        ref: 117
      },
      {
        id: 4,
        title: "单词拆分",
        url: "https://leetcode.cn/problems/word-break/description/?envType=problem-list-v2&envId=dynamic-programming",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "完全背包"],
        ref: 118
      },
      {
        id: 5,
        title: "买卖股票的最佳时机",
        url: "https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=dynamic-programming",
        difficulty: "easy",
        passed: false,
        tags: ["动态规划", "贪心"],
        ref: 119
      }
    ]
  },
  "list_26": {
    name: "背包问题",
    problems: [
      {
        id: 1,
        title: "装箱问题",
        url: "https://www.luogu.com.cn/problem/P1049",
        difficulty: "easy",
        passed: false,
        tags: ["动态规划", "01背包"],
        ref: 120
      },
      {
        id: 2,
        title: "宝物筛选",
        url: "https://www.luogu.com.cn/problem/P1776",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "多重背包"],
        ref: 121
      },
      {
        id: 3,
        title: "旅行商的背包",
        url: "https://www.luogu.com.cn/problem/solution/P1782",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "多重背包"],
        ref: 122
      },
      {
        id: 4,
        title: "多人背包",
        url: "https://www.luogu.com.cn/problem/P1858",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "01背包", "前K优解"],
        ref: 123
      },
      {
        id: 5,
        title: "ICPC 2023 Nanjing R 背包",
        url: "https://www.luogu.com.cn/problem/solution/P13957",
        difficulty: "medium",
        passed: false,
        tags: ["动态规划", "01背包"],
        ref: 124
      }
    ]
  },
  "list_27": {
    name: "简单树",
    problems: [
      {
        id: 1,
        title: "二叉树的最大深度",
        url: "https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/",
        difficulty: "easy",
        passed: false,
        tags: ["二叉树", "深度优先搜索", "递归"],
        ref: 125
      },
      {
        id: 2,
        title: "二叉树的中序遍历",
        url: "https://leetcode.cn/problems/binary-tree-inorder-traversal/description/",
        difficulty: "easy",
        passed: false,
        tags: ["二叉树", "深度优先搜索", "递归"],
        ref: 126
      },
      {
        id: 3,
        title: "验证二叉搜索树",
        url: "https://leetcode.cn/problems/validate-binary-search-tree/description/",
        difficulty: "medium",
        passed: false,
        tags: ["二叉树", "二叉搜索树", "深度优先搜索"],
        ref: 127
      },
      {
        id: 4,
        title: "二叉树的层序遍历",
        url: "https://leetcode.cn/problems/binary-tree-level-order-traversal/description/",
        difficulty: "medium",
        passed: false,
        tags: ["二叉树", "广度优先搜索"],
        ref: 128
      },
      {
        id: 5,
        title: "路径总和 II",
        url: "https://leetcode.cn/problems/path-sum-ii/description/",
        difficulty: "medium",
        passed: false,
        tags: ["二叉树", "深度优先搜索", "回溯"],
        ref: 129
      }
    ]
  },
  "list_28": {
    name: "特殊树",
    problems: [
      {
        id: 1,
        title: "普通平衡树",
        url: "https://www.luogu.com.cn/problem/P3369",
        difficulty: "hard",
        passed: false,
        tags: ["平衡树", "数据结构", "模板"],
        ref: 130
      },
      {
        id: 2,
        title: "文艺平衡树",
        url: "https://www.luogu.com.cn/problem/P3391",
        difficulty: "hard",
        passed: false,
        tags: ["平衡树", "Splay", "区间翻转"],
        ref: 131
      },
      {
        id: 3,
        title: "将有序数组转换为二叉搜索树",
        url: "https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/",
        difficulty: "easy",
        passed: false,
        tags: ["二叉搜索树", "递归", "数组"],
        ref: 132
      },
      {
        id: 4,
        title: "不同的二叉搜索树",
        url: "https://leetcode.cn/problems/unique-binary-search-trees/",
        difficulty: "medium",
        passed: false,
        tags: ["二叉搜索树", "动态规划", "计数"],
        ref: 133
      },
      {
        id: 5,
        title: "郁闷的出纳员",
        url: "https://www.luogu.com.cn/problem/P1486",
        difficulty: "hard",
        passed: false,
        tags: ["平衡树", "数据结构", "NOI"],
        ref: 134
      }
    ]
  },
  "list_29": {
    name: "剪枝/记忆化",
    problems: [
      {
        id: 1,
        title: "引水入城",
        url: "https://www.luogu.com.cn/problem/P1514",
        difficulty: "hard",
        passed: false,
        tags: ["搜索", "记忆化搜索", "NOIP"],
        ref: 135
      },
      {
        id: 2,
        title: "Cow Travelling S",
        url: "https://www.luogu.com.cn/problem/P1535",
        difficulty: "medium",
        passed: false,
        tags: ["搜索", "记忆化搜索", "DP"],
        ref: 136
      },
      {
        id: 3,
        title: "小木棍",
        url: "https://www.luogu.com.cn/problem/P1120",
        difficulty: "hard",
        passed: false,
        tags: ["搜索", "剪枝", "回溯"],
        ref: 137
      },
      {
        id: 4,
        title: "Mayan 游戏",
        url: "https://www.luogu.com.cn/problem/P1312",
        difficulty: "hard",
        passed: false,
        tags: ["搜索", "剪枝", "模拟"],
        ref: 138
      },
      {
        id: 5,
        title: "逛公园",
        url: "https://www.luogu.com.cn/problem/P3953",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "记忆化搜索", "最短路",],
        ref: 139
      }
    ]
  },
  "list_30": {
    name: "双向BFS/迭代加深",
    problems: [
      {
        id: 1,
        title: "[USACO12OPEN] Balanced Cow Subsets G",
        url: "https://www.luogu.com.cn/problem/P3067",
        difficulty: "hard",
        passed: false,
        tags: ["双向BFS", "搜索", "meet-in-the-middle"],
        ref: 140
      },
      {
        id: 2,
        title: "[CEOI 2015] 世界冰球锦标赛",
        url: "https://www.luogu.com.cn/problem/P4799",
        difficulty: "hard",
        passed: false,
        tags: ["双向BFS", "搜索", "meet-in-the-middle"],
        ref: 141
      },
      {
        id: 3,
        title: "[USACO05DEC] Knights of Ni S",
        url: "https://www.luogu.com.cn/problem/P5195",
        difficulty: "medium",
        passed: false,
        tags: ["双向BFS", "搜索", "最短路"],
        ref: 142
      },
      {
        id: 4,
        title: "[USACO06JAN] The Grove S",
        url: "https://www.luogu.com.cn/problem/P2864",
        difficulty: "medium",
        passed: false,
        tags: ["迭代加深", "搜索", "最短路"],
        ref: 143
      },
      {
        id: 5,
        title: "单词接龙",
        url: "https://leetcode.cn/problems/word-ladder/",
        difficulty: "hard",
        passed: false,
        tags: ["双向BFS", "图论", "最短路"],
        ref: 144
      }
    ]
  },
  "list_31": {
    name: "归并算法",
    problems: [
      {
        id: 1,
        title: "排序数组",
        url: "https://leetcode.cn/problems/sort-an-array/",
        difficulty: "medium",
        passed: false,
        tags: ["归并排序", "排序", "分治"],
        ref: 145
      },
      {
        id: 2,
        title: "逆序对",
        url: "https://www.luogu.com.cn/problem/P1908",
        difficulty: "hard",
        passed: false,
        tags: ["归并排序", "逆序对", "分治"],
        ref: 146
      },
      {
        id: 3,
        title: "合并区间",
        url: "https://leetcode.cn/problems/merge-intervals/",
        difficulty: "medium",
        passed: false,
        tags: ["归并", "排序", "区间"],
        ref: 147
      },
      {
        id: 4,
        title: "搜索二维矩阵 II",
        url: "https://leetcode.cn/problems/search-a-2d-matrix-ii/",
        difficulty: "medium",
        passed: false,
        tags: ["归并", "搜索", "矩阵"],
        ref: 148
      },
      {
        id: 5,
        title: "[NOIP 2011 普及组] 瑞士轮",
        url: "https://www.luogu.com.cn/problem/P1309",
        difficulty: "hard",
        passed: false,
        tags: ["归并排序", "模拟", "排序"],
        ref: 149
      }
    ]
  },
  "list_32": {
    name: "快速排序",
    problems: [
      {
        id: 1,
        title: "排序数组",
        url: "https://leetcode.cn/problems/sort-an-array/",
        difficulty: "medium",
        passed: false,
        tags: ["快速排序", "排序", "分治"],
        ref: 150
      },
      {
        id: 2,
        title: "【模板】排序",
        url: "https://www.luogu.com.cn/problem/P1177",
        difficulty: "hard",
        passed: false,
        tags: ["快速排序", "排序", "模板"],
        ref: 151
      },
      {
        id: 3,
        title: "数组中的第K个最大元素",
        url: "https://leetcode.cn/problems/kth-largest-element-in-an-array/",
        difficulty: "medium",
        passed: false,
        tags: ["快速排序", "堆", "分治"],
        ref: 152
      },
      {
        id: 4,
        title: "[NOIP 1998 提高组] 拼数",
        url: "https://www.luogu.com.cn/problem/P1012",
        difficulty: "hard",
        passed: false,
        tags: ["快速排序", "排序", "贪心"],
        ref: 153
      },
      {
        id: 5,
        title: "滑动窗口最大值",
        url: "https://leetcode.cn/problems/sliding-window-maximum/",
        difficulty: "hard",
        passed: false,
        tags: ["快速排序", "单调队列", "滑动窗口"],
        ref: 154
      }
    ]
  },
  "list_33": {
    name: "堆",
    problems: [
      {
        id: 1,
        title: "【模板】堆",
        url: "https://www.luogu.com.cn/problem/P3378",
        difficulty: "medium",
        passed: false,
        tags: ["堆", "优先队列", "模板"],
        ref: 155
      },
      {
        id: 2,
        title: "最接近原点的 K 个点",
        url: "https://leetcode.cn/problems/k-closest-points-to-origin/",
        difficulty: "medium",
        passed: false,
        tags: ["堆", "排序", "几何"],
        ref: 156
      },
      {
        id: 3,
        title: "[NOIP 2004 提高组] 合并果子",
        url: "https://www.luogu.com.cn/problem/P1090",
        difficulty: "hard",
        passed: false,
        tags: ["堆", "贪心", "优先队列"],
        ref: 157
      },
      {
        id: 4,
        title: "中位数",
        url: "https://www.luogu.com.cn/problem/P1168",
        difficulty: "hard",
        passed: false,
        tags: ["堆", "对顶堆", "中位数"],
        ref: 158
      },
      {
        id: 5,
        title: "[USACO12FEB] Cow Coupons G",
        url: "https://www.luogu.com.cn/problem/P3045",
        difficulty: "hard",
        passed: false,
        tags: ["堆", "贪心", "优先队列"],
        ref: 159
      }
    ]
  },
  "list_34": {
    name: "桶",
    problems: [
      {
        id: 1,
        title: "【模板】排序",
        url: "https://www.luogu.com.cn/problem/P1177",
        difficulty: "hard",
        passed: false,
        tags: ["桶排序", "排序", "模板"],
        ref: 160
      },
      {
        id: 2,
        title: "前 K 个高频元素",
        url: "https://leetcode.cn/problems/top-k-frequent-elements/",
        difficulty: "medium",
        passed: false,
        tags: ["桶排序", "哈希表", "频率统计"],
        ref: 161
      },
      {
        id: 3,
        title: "最大间距",
        url: "https://leetcode.cn/problems/maximum-gap/",
        difficulty: "hard",
        passed: false,
        tags: ["桶排序", "排序", "线性时间"],
        ref: 162
      },
      {
        id: 4,
        title: "[蓝桥杯 2022 省 Python B] 数位排序",
        url: "https://www.luogu.com.cn/problem/P12366",
        difficulty: "medium",
        passed: false,
        tags: ["桶排序", "排序", "数位和"],
        ref: 163
      },
      {
        id: 5,
        title: "[CSP-J 2020] 直播获奖",
        url: "https://www.luogu.com.cn/problem/P7072",
        difficulty: "hard",
        passed: false,
        tags: ["桶排序", "排序", "计数"],
        ref: 164
      }
    ]
  },
  "list_35": {
    name: "基数",
    problems: [
      {
        id: 1,
        title: "【模板】排序",
        url: "https://www.luogu.com.cn/problem/P1177",
        difficulty: "hard",
        passed: false,
        tags: ["基数排序", "排序", "模板"],
        ref: 165
      },
      {
        id: 2,
        title: "排序数组",
        url: "https://leetcode.cn/problems/sort-an-array/",
        difficulty: "medium",
        passed: false,
        tags: ["基数排序", "排序", "线性时间"],
        ref: 166
      },
      {
        id: 3,
        title: "最大间距",
        url: "https://leetcode.cn/problems/maximum-gap/",
        difficulty: "hard",
        passed: false,
        tags: ["基数排序", "排序", "桶排序"],
        ref: 167
      },
      {
        id: 4,
        title: "【模板】后缀排序",
        url: "https://www.luogu.com.cn/problem/P3809",
        difficulty: "hard",
        passed: false,
        tags: ["基数排序", "后缀排序", "字符串"],
        ref: 168
      },
      {
        id: 5,
        title: "[WC2017] 挑战",
        url: "https://www.luogu.com.cn/problem/P4604",
        difficulty: "hard",
        passed: false,
        tags: ["基数排序", "排序", "优化"],
        ref: 169
      }
    ]
  },
  "list_36": {
    name: "复杂DP优化",
    problems: [
      {
        id: 1,
        title: "规划兼职工作",
        url: "https://leetcode.cn/problems/maximum-profit-in-job-scheduling/",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "二分查找", "优化"],
        ref: 170
      },
      {
        id: 2,
        title: "买卖股票的最佳时机 IV",
        url: "https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "状态压缩", "优化"],
        ref: 171
      },
      {
        id: 3,
        title: "戳气球",
        url: "https://leetcode.cn/problems/burst-balloons/",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "区间DP", "优化"],
        ref: 172
      },
      {
        id: 4,
        title: "[USACO11OPEN] Mowing the Lawn G",
        url: "https://www.luogu.com.cn/problem/P2627",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "单调队列", "优化"],
        ref: 173
      },
      {
        id: 5,
        title: "[NOI2009] 诗人小G",
        url: "https://luogu.com.cn/problem/P1912",
        difficulty: "hard",
        passed: false,
        tags: ["动态规划", "决策单调性", "优化"],
        ref: 174
      }
    ]
  },
  "list_37": {
    name: "树型DP",
    problems: [
      {
        id: 1,
        title: "没有上司的舞会",
        url: "https://www.luogu.com.cn/problem/P1352",
        difficulty: "medium",
        passed: false,
        tags: ["树型DP", "状态转移", "DFS"],
        ref: 175
      },
      {
        id: 2,
        title: "[NOIP 2003 提高组] 加分二叉树",
        url: "https://www.luogu.com.cn/problem/P1040",
        difficulty: "medium",
        passed: false,
        tags: ["树型DP", "区间DP", "二叉树"],
        ref: 176
      },
      {
        id: 3,
        title: "移除无效的括号",
        url: "https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/",
        difficulty: "medium",
        passed: false,
        tags: ["树型DP", "栈", "括号匹配"],
        ref: 177
      },
      {
        id: 4,
        title: "二叉树中的最大路径和",
        url: "https://leetcode.cn/problems/binary-tree-maximum-path-sum/",
        difficulty: "hard",
        passed: false,
        tags: ["树型DP", "二叉树", "最大路径"],
        ref: 178
      },
      {
        id: 5,
        title: "[ZJOI2008] 骑士",
        url: "https://www.luogu.com.cn/problem/P2607",
        difficulty: "hard",
        passed: false,
        tags: ["树型DP", "基环树", "状态转移"],
        ref: 179
      }
    ]
  },
  "list_38": {
    name: "区间DP",
    problems: [
      {
        id: 1,
        title: "[NOI1995] 石子合并",
        url: "https://www.luogu.com.cn/problem/P1880",
        difficulty: "hard",
        passed: false,
        tags: ["区间DP", "环形DP", "最大最小值"],
        ref: 180
      },
      {
        id: 2,
        title: "[USACO16OPEN] 248 G",
        url: "https://www.luogu.com.cn/problem/P3146",
        difficulty: "hard",
        passed: false,
        tags: ["区间DP", "序列合并", "贪心"],
        ref: 181
      },
      {
        id: 3,
        title: "[NOIP 2006 提高组] 能量项链",
        url: "https://www.luogu.com.cn/problem/P1063",
        difficulty: "hard",
        passed: false,
        tags: ["区间DP", "环形DP", "最大值"],
        ref: 182
      },
      {
        id: 4,
        title: "[CQOI2007] 涂色",
        url: "https://www.luogu.com.cn/problem/P4170",
        difficulty: "hard",
        passed: false,
        tags: ["区间DP", "状态压缩", "最小操作次数"],
        ref: 183
      },
      {
        id: 5,
        title: "移除盒子",
        url: "https://leetcode.cn/problems/remove-boxes/",
        difficulty: "hard",
        passed: false,
        tags: ["区间DP", "状态压缩", "优化"],
        ref: 184
      }
    ]
  },
  "list_39": {
    name: "状态压缩DP",
    problems: [
      {
        id: 1,
        title: "[NOI2001] 炮兵阵地",
        url: "https://www.luogu.com.cn/problem/P2704",
        difficulty: "hard",
        passed: false,
        tags: ["状态压缩DP", "网格DP", "位运算"],
        ref: 185
      },
      {
        id: 2,
        title: "[USACO06NOV] Corn Fields G",
        url: "https://www.luogu.com.cn/problem/P1879",
        difficulty: "hard",
        passed: false,
        tags: ["状态压缩DP", "网格DP", "位运算"],
        ref: 186
      },
      {
        id: 3,
        title: "[SCOI2005] 互不侵犯",
        url: "https://www.luogu.com.cn/problem/P1896",
        difficulty: "hard",
        passed: false,
        tags: ["状态压缩DP", "棋盘DP", "位运算"],
        ref: 187
      },
      {
        id: 4,
        title: "划分为k个相等的子集",
        url: "https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/",
        difficulty: "hard",
        passed: false,
        tags: ["状态压缩DP", "子集划分", "位运算"],
        ref: 188
      },
      {
        id: 5,
        title: "[NOIP 2017 提高组] 宝藏",
        url: "https://www.luogu.com.cn/problem/P3959",
        difficulty: "hard",
        passed: false,
        tags: ["状态压缩DP", "图论", "最小生成树"],
        ref: 189
      }
    ]
  },
  "list_40": {
    name: "图",
    problems: [
      {
        id: 1,
        title: "克隆图",
        url: "https://leetcode.cn/problems/clone-graph/",
        difficulty: "medium",
        passed: false,
        tags: ["图", "DFS", "BFS"],
        ref: 190
      },
      {
        id: 2,
        title: "课程表",
        url: "https://leetcode.cn/problems/course-schedule/",
        difficulty: "medium",
        passed: false,
        tags: ["图", "拓扑排序", "DFS"],
        ref: 191
      },
      {
        id: 3,
        title: "[NOIP 2015 提高组] 信息传递",
        url: "https://www.luogu.com.cn/problem/P2661",
        difficulty: "hard",
        passed: false,
        tags: ["图", "并查集", "环检测"],
        ref: 192
      },
      {
        id: 4,
        title: "[USACO08DEC] Trick or Treat on the Farm G",
        url: "https://www.luogu.com.cn/problem/P2921",
        difficulty: "hard",
        passed: false,
        tags: ["图", "记忆化搜索", "环检测"],
        ref: 193
      },
      {
        id: 5,
        title: "K 站中转内最便宜的航班",
        url: "https://leetcode.cn/problems/cheapest-flights-within-k-stops/",
        difficulty: "medium",
        passed: false,
        tags: ["图", "最短路", "动态规划"],
        ref: 194
      }
    ]
  },
  "list_41": {
    name: "图论算法",
    problems: [
      {
        id: 1,
        title: "【模板】单源最短路径（标准版）",
        url: "https://www.luogu.com.cn/problem/P4779",
        difficulty: "hard",
        passed: false,
        tags: ["图论算法", "最短路", "Dijkstra"],
        ref: 195
      },
      {
        id: 2,
        title: "[USACO03FALL / HAOI2006] 受欢迎的牛 G",
        url: "https://www.luogu.com.cn/problem/P2341",
        difficulty: "hard",
        passed: false,
        tags: ["图论算法", "强连通分量", "Tarjan"],
        ref: 196
      },
      {
        id: 3,
        title: "【模板】二分图最大匹配",
        url: "https://www.luogu.com.cn/problem/P3386",
        difficulty: "hard",
        passed: false,
        tags: ["图论算法", "二分图", "最大匹配"],
        ref: 197
      },
      {
        id: 4,
        title: "【模板】网络最大流",
        url: "https://www.luogu.com.cn/problem/P3376",
        difficulty: "hard",
        passed: false,
        tags: ["图论算法", "网络流", "最大流"],
        ref: 198
      },
      {
        id: 5,
        title: "访问消失节点的最少时间",
        url: "https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/",
        difficulty: "medium",
        passed: false,
        tags: ["图论算法", "最短路", "Dijkstra"],
        ref: 199
      }
    ]
  }
};
