/*
这是一个储存知识树节点的代码，每个节点的基本结构如下所示

nodes: [
      {
        id: "",             // 节点id
        icon: "🔒",         // 图标
        type: "",           // 节点类型，控制节点的显示
        unlocked: false,    // 解锁状态
        questionList:       // 对应的题单编号，值为0时表示没有
        parent: "",         // 父节点，只能有一个
        children: []        // 儿子节点，可以有很多，也可以没有
      }
    ]
*/

// 知识树数据结构
const treeData = [
  {
    level: 0,
    title: "编程基础",
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
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "基本运算",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "程序基本语句",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "数组与字符串",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "指针与引用",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "结构体",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "函数与递归",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      },
      {
        id: "数据库常用函数",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["编程基础"],
        children: ["模拟与枚举"]
      }
    ]
  },
  {
    level: 2,
    title: "模拟与枚举",
    nodes: [
      {
        id: "模拟与枚举",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基本数据类型", "基本运算", "程序基本语句", "数组与字符串", "指针与引用", "结构体", "函数与递归", "数据库常用函数"],
        children: ["模拟", "枚举"]
      },
    ]
  },
  {
    level: 3,
    title: "",
    nodes: [
      {
        id: "模拟",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["模拟与枚举"],
        children: ["基础算法"]
      },
      {
        id: "枚举",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["模拟与枚举"],
        children: ["基础算法"]
      }
    ]
  },
  {
    level: 4,
    title: "基础算法",
    nodes: [
      {
        id: "基础算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["模拟", "枚举"],
        children: ["递推", "二分", "递归", "贪心", "倍增", "简单排序算法", "分治算法", "前缀和差分"]
      }
    ]
  },
  {
    level: 5,
    title: "",
    nodes: [
      {
        id: "递推",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "二分",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "递归",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "贪心",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "倍增",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "简单排序算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "分治算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
      {
        id: "前缀和差分",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["基础算法"],
        children: ["简单搜索算法"]
      },
    ]
  },
  {
    level: 6,
    title: "简单搜索算法",
    nodes: [
      {
        id: "简单搜索算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["递推", "二分", "递归", "贪心", "倍增", "简单排序算法", "分治算法", "前缀和差分"],
        children: ["DFS", "BFS"]
      }
    ]
  },
  {
    level: 7,
    title: "",
    nodes: [
      {
        id: "DFS",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单搜索算法"],
        children: ["字符串匹配"]
      },
      {
        id: "BFS",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单搜索算法"],
        children: ["字符串匹配"]
      }
    ]
  },
  {
    level: 8,
    title: "字符串匹配",
    nodes: [
      {
        id: "字符串匹配",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["DFS", "BFS"],
        children: ["线性结构"]
      }
    ]
  },
  {
    level: 9,
    title: "线性结构",
    nodes: [
      {
        id: "线性结构",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["字符串匹配"],
        children: ["栈", "队列", "链表"]
      }
    ]
  },
  {
    level: 10,
    title: "",
    nodes: [
      {
        id: "栈",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["线性结构"],
        children: ["简单动态规划"]
      },
      {
        id: "队列",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["线性结构"],
        children: ["简单动态规划"]
      },
      {
        id: "链表",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["线性结构"],
        children: ["简单动态规划"]
      }
    ]
  },
  {
    level: 11,
    title: "简单动态规划",
    nodes: [
      {
        id: "简单动态规划",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["栈", "队列", "链表"],
        children: ["一维DP", "背包问题"]
      }
    ]
  },
  {
    level: 12,
    title: "",
    nodes: [
      {
        id: "一维DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单动态规划"],
        children: ["简单树"]
      },
      {
        id: "背包问题",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单动态规划"],
        children: ["简单树"]
      }
    ]
  },
  {
    level: 13,
    title: "简单树",
    nodes: [
      {
        id: "简单树",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["一维DP", "背包问题"],
        children: ["特殊树"]
      },
    ]
  },
  {
    level: 14,
    title: "特殊树",
    nodes: [
      {
        id: "特殊树",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["简单树"],
        children: ["深入搜索算法"]
      }
    ]
  },
  {
    level: 15,
    title: "深入搜索算法",
    nodes: [
      {
        id: "深入搜索算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["特殊树"],
        children: ["剪枝/记忆化", "双向BFS/迭代加深"]
      }
    ]
  },
  {
    level: 16,
    title: "",
    nodes: [
      {
        id: "剪枝/记忆化",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入搜索算法"],
        children: ["深入排序算法"]
      },
      {
        id: "双向BFS/迭代加深",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入搜索算法"],
        children: ["深入排序算法"]
      }
    ]
  },
  {
    level: 17,
    title: "深入排序算法",
    nodes: [
      {
        id: "深入排序算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["剪枝/记忆化", "双向BFS/迭代加深"],
        children: ["归并算法", "快速排序", "堆", "桶", "基数"]
      }
    ]
  },
  {
    level: 18,
    title: "",
    nodes: [
      {
        id: "归并算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      },
      {
        id: "快速排序",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      },
      {
        id: "堆",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      },
      {
        id: "桶",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      },
      {
        id: "基数",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["深入排序算法"],
        children: ["复杂动态规划"]
      }
    ]
  },
  {
    level: 19,
    title: "复杂动态规划",
    nodes: [
      {
        id: "复杂动态规划",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["归并算法", "快速排序", "堆", "桶", "基数"],
        children: ["复杂DP优化", "树型DP", "区间DP", "状态压缩DP"]
      }
    ]
  },
  {
    level: 20,
    title: "",
    nodes: [
      {
        id: "复杂DP优化",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["复杂动态规划"],
        children: ["图"]
      },
      {
        id: "树型DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["复杂动态规划"],
        children: ["图"]
      },
      {
        id: "区间DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["复杂动态规划"],
        children: ["图"]
      },
      {
        id: "状态压缩DP",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["复杂动态规划"],
        children: ["图"]
      },
    ]
  },
  {
    level: 21,
    title: "图",
    nodes: [
      {
        id: "图",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["复杂DP优化", "树型DP", "区间DP", "状态压缩DP"],
        children: ["图论算法"]
      }
    ]
  },
  {
    level: 22,
    title: "图论算法",
    nodes: [
      {
        id: "图论算法",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        questionList: 0,
        parent: ["图"],
        children: [""]
      }
    ]
  }
];