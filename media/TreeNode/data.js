/*
这是一个储存知识树节点的代码，每个节点的基本结构如下所示

nodes: [
      {
        id: "",             // 节点id
        icon: "🔒",         // 图标
        type: "",           // 节点类型，控制节点的显示
        unlocked: false,    // 解锁状态
        parent: "",         // 父节点，只能有一个
        children: []        // 儿子节点，可以有很多，也可以没有
      }
    ]
*/

// 科技树数据结构
const techData = [
  {
    level: 0,
    title: "编程基础",
    icon: "🚩",
    type: "root",
    unlocked: true,
    children: ["基本数据结构"]
  },
  {
    level: 1,
    title: "编程进阶1",
    nodes: [
      {
        id: "基础数据结构",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        parent: "编程基础",
        children: ["基础算法思想"]
      }
    ]
  },
  {
    level: 2,
    title: "编程进阶2",
    nodes: [
      {
        id: "基础算法思想",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        parent: "基础数据结构",
        children: ["动态规划", "搜索技术"]
      }
    ]
  },
  {
    level: 3,
    title: "编程进阶3",
    nodes: [
      {
        id: "动态规划",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        parent: "基础算法思想",
        children: ["树基础"]
      },
      {
        id: "搜索技术",
        icon: "🔒",
        type: "ultimate",
        unlocked: false,
        parent: "基础算法思想",
        children: []
      }
    ]
  },
  {
    level: 4,
    title: "编程进阶4",
    nodes: [
      {
        id: "树基础",
        icon: "🔒",
        type: "tech",
        unlocked: false,
        parent: "动态规划",
        children: ["并查集", "二叉树"]
      }
    ]
  },
  {
    level: 5,
    title: "编程进阶5",
    nodes: [
      {
        id: "并查集",
        icon: "🔒",
        type: "ultimate",
        unlocked: false,
        parent: "树基础",
        children: []
      },
      {
        id: "二叉树",
        icon: "🔒",
        type: "ultimate",
        unlocked: false,
        parent: "树基础",
        children: []
      }
    ]
  }
];