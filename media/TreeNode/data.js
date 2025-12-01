/*
这是一个储存知识树节点的代码，每个节点的基本结构如下所示

nodes: [
      {
        id: "",             // 节点id
        icon: "🔒",         // 图标
        type: "",           // 节点类型，控制节点的显示
        unlocked: false,    // 解锁状态
        lay: 2,             // 节点所在层级
        questionList:       // 对应的题单编号，值为0时表示没有
        parent: "",         // 父节点，只能有一个
        children: []        // 儿子节点，可以有很多，也可以没有
      }
    ]
*/

// 知识树数据结构
const treeNode_1 = [
  {
    level: 0,
    title: "编程语言基础",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["基本数据类型", "基本运算", "程序基本语句", "数组与字符串", "指针与引用", "结构体", "函数与递归", "数据库常用函数"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "基本数据类型",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 1,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "基本运算",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 2,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "程序基本语句",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 3,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "数组与字符串",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 4,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "指针与引用",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 5,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "结构体",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 6,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "函数与递归",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 7,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      },
      {
        id: "数据库常用函数",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 8,
        parent: ["编程语言基础"],
        children: [""],
        lay: 2
      }
    ]
  }
]

const treeNode_2 = [
  {
    level: 0,
    title: "模拟与枚举",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["模拟", "枚举"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "模拟",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 9,
        parent: ["模拟与枚举"],
        children: [""],
      },
      {
        id: "枚举",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 10,
        parent: ["模拟与枚举"],
        children: [""],
      }
    ]
  }
]

const treeNode_3 = [
  {
    level: 0,
    title: "基础算法",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["递推", "二分", "递归", "贪心", "倍增", "简单排序算法", "分治算法", "前缀和差分"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "递推",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 11,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "二分",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 12,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "递归",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 13,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "贪心",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 14,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "倍增",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 18,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "简单排序算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 15,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "分治算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 16,
        parent: ["基础算法"],
        children: [""]
      },
      {
        id: "前缀和与差分",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 17,
        parent: ["基础算法"],
        children: [""]
      },
    ]
  }
]

const treeNode_4 = [
  {
    level: 0,
    title: "简单搜索算法",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["DFS", "BFS"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "DFS",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 19,
        parent: ["简单搜索算法"],
        children: [""]
      },
      {
        id: "BFS",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 20,
        parent: ["简单搜索算法"],
        children: [""]
      }
    ]
  }
]

const treeNode_5 = [
  {
    level: 0,
    title: "字符串匹配",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["字符串匹配算法"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "字符串匹配算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 21,
        parent: ["字符串匹配"],
        children: [""]
      }
    ]
  }
]

const treeNode_6 = [
  {
    level: 0,
    title: "线性结构",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["栈", "队列", "链表"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "栈",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 22,
        parent: ["线性结构"],
        children: [""]
      },
      {
        id: "队列",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 23,
        parent: ["线性结构"],
        children: [""]
      },
      {
        id: "链表",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 24,
        parent: ["线性结构"],
        children: [""]
      }
    ]
  }
]

const treeNode_7 = [
  {
    level: 0,
    title: "简单动态规划",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["一维DP", "背包问题"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "一维DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 25,
        parent: ["简单动态规划"],
        children: [""]
      },
      {
        id: "背包问题",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 26,
        parent: ["简单动态规划"],
        children: [""]
      }
    ]
  }
]

const treeNode_8 = [
  {
    level: 0,
    title: "简单树",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["简单树算法"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "简单树算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 27,
        parent: ["简单树"],
        children: [""],
      }
    ]
  }
]

const treeNode_9 = [
  {
    level: 0,
    title: "特殊树",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["特殊树算法"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "特殊树算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 28,
        parent: ["特殊树"],
        children: [""]
      }
    ]
  }
]

const treeNode_10 = [
  {
    level: 0,
    title: "深入搜索算法",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["剪枝/记忆化", "双向BFS/迭代加深"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "剪枝/记忆化",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 29,
        parent: ["深入搜索算法"],
        children: [""]
      },
      {
        id: "双向BFS/迭代加深",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 30,
        parent: ["深入搜索算法"],
        children: [""]
      }
    ]
  }
]

const treeNode_11 = [
  {
    level: 0,
    title: "深入排序算法",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["归并算法", "快速排序", "堆", "桶", "基数"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "归并算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 31,
        parent: ["深入排序算法"],
        children: [""]
      },
      {
        id: "快速排序",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 32,
        parent: ["深入排序算法"],
        children: [""]
      },
      {
        id: "堆",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 33,
        parent: ["深入排序算法"],
        children: [""]
      },
      {
        id: "桶",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 34,
        parent: ["深入排序算法"],
        children: [""]
      },
      {
        id: "基数",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 35,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      }
    ]
  }
]

const treeNode_12 = [
  {
    level: 0,
    title: "复杂动态规划",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["复杂DP优化", "树型DP", "区间DP", "状态压缩DP"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "复杂DP优化",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 36,
        parent: ["复杂动态规划"],
        children: [""]
      },
      {
        id: "树型DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 37,
        parent: ["复杂动态规划"],
        children: [""]
      },
      {
        id: "区间DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 38,
        parent: ["复杂动态规划"],
        children: [""]
      },
      {
        id: "状态压缩DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 39,
        parent: ["复杂动态规划"],
        children: [""]
      },
    ]
  }
]

const treeNode_13 = [
  {
    level: 0,
    title: "图*",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["图"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "图",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 40,
        parent: ["图*"],
        children: [""]
      }
    ]
  }
]

const treeNode_14 = [
  {
    level: 0,
    title: "图论算法*",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["图论算法"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "图论算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        lay: 2,
        questionList: 41,
        parent: ["图论算法*"],
        children: [""]
      }
    ]
  }
]

const treeMain = [
  {
    level: 0,
    title: "编程学习之旅",
    icon: "🚩",
    type: "root",
    unlocked: true,
    questionList: 0,
    children: ["编程语言基础"]
  },
  {
    level: 1,
    title: "",
    nodes: [
      {
        id: "编程语言基础",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程学习之旅"],
        children: ["模拟与枚举"],
        myNode: treeNode_1,
        lay: 1
      },
    ]
  },
  {
    level: 2,
    title: "",
    nodes: [
      {
        id: "模拟与枚举",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程语言基础"],
        children: [""],
        myNode: treeNode_2,
        lay: 1
      },
    ]
  },
  {
    level: 3,
    title: "",
    nodes: [
      {
        id: "基础算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["模拟与枚举"],
        children: [""],
        myNode: treeNode_3,
        lay: 1
      },
    ]
  },
  {
    level: 4,
    title: "",
    nodes: [
      {
        id: "简单搜索算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单动态规划"],
        myNode: treeNode_4,
        lay: 1
      },
      {
        id: "线性结构",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单树"],
        myNode: treeNode_6,
        lay: 1
      },
      {
        id: "字符串匹配",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: [""],
        myNode: treeNode_5,
        lay: 1
      }
    ]
  },
  {
    level: 5,
    title: "",
    nodes: [
      {
        id: "简单动态规划",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单搜索算法"],
        children: [""],
        myNode: treeNode_7,
        lay: 1
      },
      {
        id: "简单树",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["线性结构"],
        children: ["特殊树", "图"],
        myNode: treeNode_8,
        lay: 1
      }
    ]
  },
  {
    level: 6,
    title: "",
    nodes: [
      {
        id: "图",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单树"],
        children: ["图论算法"],
        myNode: treeNode_13,
        lay: 1
      },
      {
        id: "特殊树",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单树"],
        children: ["深入排序算法", "深入搜索算法", "复杂动态规划"],
        myNode: treeNode_9,
        lay: 1
      }
    ]
  },
  {
    level: 7,
    title: "",
    nodes: [
      {
        id: "图论算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["图"],
        children: [""],
        myNode: treeNode_14,
        lay: 1
      },
      {
        id: "深入搜索算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["特殊树"],
        children: [""],
        myNode: treeNode_10,
        lay: 1
      },
      {
        id: "深入排序算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["特殊树"],
        children: [""],
        myNode: treeNode_11,
        lay: 1
      },
      {
        id: "复杂动态规划",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["特殊树"],
        children: [""],
        myNode: treeNode_12,
        lay: 1
      }
    ]
  }
]

let treeData = treeMain;
let pageID = "知识树";