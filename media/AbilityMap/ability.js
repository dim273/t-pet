// 能力图谱主逻辑

// 能力图谱计算模块
// 提供能力图谱相关的计算功能

// 构建标签掌握程度映射
function buildTagMastery(allProblems, passedSet) {
  const tagStats = {};

  allProblems.forEach(problem => {
    const tags = problem.tags || [];
    tags.forEach(tag => {
      if (!tagStats[tag]) {
        tagStats[tag] = { total: 0, passed: 0 };
      }
      tagStats[tag].total += 1;
      if (passedSet.has(problem.ref)) {
        tagStats[tag].passed += 1;
      }
    });
  });

  return Object.keys(tagStats).reduce((acc, tag) => {
    const stat = tagStats[tag];
    acc[tag] = stat.total > 0 ? stat.passed / stat.total : 0;
    return acc;
  }, {});
}

// 计算领域掌握程度
function calculateDomainMastery(domainNode, allProblems, passedSet) {
  const domainId = domainNode.id;
  console.log('Calculating domain mastery for:', domainId);

  // 获取领域下的二级节点
  const secondaryNodes = [];
  if (domainNode.myNode) {
    console.log('Domain has myNode:', domainNode.myNode);
    domainNode.myNode.forEach(subLevel => {
      if (subLevel.nodes) {
        subLevel.nodes.forEach(subNode => {
          secondaryNodes.push(subNode);
        });
      }
    });
  }
  console.log('Secondary nodes:', secondaryNodes);

  // 计算二级节点的掌握程度
  const secondaryNodeMastery = {};
  let totalSecondaryMastery = 0;
  let validSecondaryNodes = 0;

  secondaryNodes.forEach(secondaryNode => {
    const nodeId = secondaryNode.id;
    const questionList = secondaryNode.questionList;
    console.log('Secondary node:', nodeId, 'questionList:', questionList);

    let nodeTotalProblems = 0;
    let nodePassedProblems = 0;

    // 根据questionList找到对应的题单，计算该二级节点相关的题目总数和已通过数
    if (questionList > 0) {
      const problemSetKey = `list_${questionList}`;
      const problemSet = window.problemSets[problemSetKey];
      console.log('Problem set for', nodeId, ':', problemSet);

      if (problemSet && problemSet.problems) {
        problemSet.problems.forEach(problem => {
          nodeTotalProblems++;
          if (passedSet.has(problem.ref)) {
            nodePassedProblems++;
          }
        });
        console.log('Found', nodeTotalProblems, 'problems for', nodeId, 'passed:', nodePassedProblems);
      }
    }

    const nodeMastery = nodeTotalProblems > 0 ? Math.round((nodePassedProblems / nodeTotalProblems) * 100) : 0;
    secondaryNodeMastery[nodeId] = nodeMastery;
    console.log('Secondary node', nodeId, 'mastery:', nodeMastery, '(', nodePassedProblems, '/', nodeTotalProblems, ')');

    // 只有当二级节点有相关题目时，才计入一级节点的掌握程度计算
    if (nodeTotalProblems > 0) {
      totalSecondaryMastery += nodeMastery;
      validSecondaryNodes++;
    }
  });
  console.log('Secondary node masteries:', secondaryNodeMastery);

  // 计算领域掌握程度：二级节点掌握程度的平均值
  const mastery = validSecondaryNodes > 0 ? Math.round(totalSecondaryMastery / validSecondaryNodes) : 0;
  console.log('Domain', domainId, 'mastery:', mastery);

  // 计算领域相关的题目总数和已通过数
  let totalProblems = 0;
  let passedProblems = 0;

  secondaryNodes.forEach(secondaryNode => {
    const questionList = secondaryNode.questionList;

    if (questionList > 0) {
      const problemSetKey = `list_${questionList}`;
      const problemSet = window.problemSets[problemSetKey];

      if (problemSet && problemSet.problems) {
        problemSet.problems.forEach(problem => {
          totalProblems++;
          if (passedSet.has(problem.ref)) {
            passedProblems++;
          }
        });
      }
    }
  });
  console.log('Domain', domainId, 'problems:', totalProblems, 'passed:', passedProblems);

  return {
    mastery,
    secondaryNodeMastery,
    totalProblems,
    passedProblems
  };
}

// 计算总体掌握程度
function calculateOverallMastery(treeData, allProblems, passedSet) {
  let totalDomains = 0;
  let overallMasteryScore = 0;

  // 遍历所有领域
  if (Array.isArray(treeData)) {
    console.log('Tree data levels:', treeData.length);
    treeData.forEach((level, levelIndex) => {
      console.log('Level', levelIndex, 'has nodes:', level.nodes ? level.nodes.length : 0);
      if (level.nodes) {
        level.nodes.forEach(node => {
          if (node.id && node.id !== "编程学习之旅") {
            totalDomains++;
            // 计算该领域的掌握程度
            const domainInfo = calculateDomainMastery(node, allProblems, passedSet);
            overallMasteryScore += domainInfo.mastery;
          }
        });
      }
    });
  }
  console.log('Total domains:', totalDomains, 'Overall mastery score:', overallMasteryScore);

  // 计算总体掌握程度百分比
  const overallMastery = totalDomains > 0 ? Math.round((overallMasteryScore / totalDomains)) : 0;
  console.log('Overall mastery:', overallMastery);
  return overallMastery;
}

// 生成能力图谱数据
function generateAbilityData(treeData, allProblems, passedSet) {
  // 从知识树数据中提取能力数据
  const abilityData = {
    labels: [],
    datasets: [{
      label: '掌握程度',
      data: [],
      backgroundColor: 'rgba(79, 70, 229, 0.2)',
      borderColor: 'rgba(79, 70, 229, 1)',
      borderWidth: 2,
      pointBackgroundColor: 'rgba(79, 70, 229, 1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(79, 70, 229, 1)'
    }]
  };

  const domains = [];
  const domainMastery = {};
  const domainDetails = {};

  // 遍历知识树的根节点
  if (Array.isArray(treeData)) {
    // 处理知识树的层级结构
    treeData.forEach(level => {
      if (level.nodes) {
        level.nodes.forEach(node => {
          // 跳过根节点"编程学习之旅"
          if (node.id && node.id !== "编程学习之旅") {
            domains.push(node.id);
            // 计算该领域的掌握程度
            const domainInfo = calculateDomainMastery(node, allProblems, passedSet);
            domainMastery[node.id] = domainInfo.mastery;
            domainDetails[node.id] = domainInfo;
          }
        });
      }
    });
  }
  console.log('Extracted domains:', domains);

  // 如果没有提取到领域，使用默认领域
  if (domains.length === 0) {
    console.log('No domains extracted, using default domains');
    const defaultDomains = [
      '编程语言基础',
      '模拟与枚举',
      '基础算法',
      '简单搜索算法',
      '字符串匹配',
      '线性结构',
      '简单动态规划',
      '简单树',
      '特殊树',
      '深入搜索算法',
      '深入排序算法',
      '复杂动态规划',
      '图',
      '图论算法'
    ];

    defaultDomains.forEach(domain => {
      domains.push(domain);
      domainMastery[domain] = Math.floor(Math.random() * 30);
      domainDetails[domain] = {
        mastery: domainMastery[domain],
        secondaryNodeMastery: {},
        totalProblems: 0,
        passedProblems: 0
      };
    });
  }

  domains.forEach(domain => {
    abilityData.labels.push(domain);
    abilityData.datasets[0].data.push(domainMastery[domain]);
  });
  console.log('Chart data:', abilityData);

  // 计算总体掌握程度
  const overallProgress = calculateOverallMastery(treeData, allProblems, passedSet);
  console.log('Overall progress:', overallProgress);

  return {
    chartData: abilityData,
    overallProgress,
    domainDetails
  };
}

// 处理返回按钮点击
function setupBackButton() {
  try {
    const vscode = acquireVsCodeApi();
    const backButton = document.getElementById('backButton');
    if (backButton) {
      backButton.addEventListener('click', () => {
        console.log('Back button clicked, sending goBack message');
        vscode.postMessage({ type: 'goBack' });
      });
      console.log('Back button event listener added successfully');
    } else {
      console.error('Back button not found');
    }
  } catch (error) {
    console.error('Error setting up back button:', error);
  }
}

// 从知识树数据中提取能力数据
function generateAbilityMapData() {
  console.log('Generating ability map data...');

  // 获取用户已通过的题目
  const passedProblems = window.passedProblems || [];
  console.log('Passed problems:', passedProblems);
  const passedSet = new Set(passedProblems);

  // 收集所有题目
  const allProblems = [];
  const problemSets = window.problemSets || {};
  console.log('Problem sets:', problemSets);

  for (const listKey in problemSets) {
    const problemSet = problemSets[listKey];
    if (problemSet && problemSet.problems) {
      allProblems.push(...problemSet.problems);
    }
  }
  console.log('All problems:', allProblems);

  // 使用能力计算模块生成数据
  const treeData = window.treeData || [];
  console.log('Tree data:', treeData);

  const abilityData = generateAbilityData(treeData, allProblems, passedSet);
  console.log('Generated ability data:', abilityData);

  // 存储领域详情，用于鼠标悬停显示
  window.domainDetails = abilityData.domainDetails;
  console.log('Domain details:', window.domainDetails);

  return {
    chartData: abilityData.chartData,
    overallProgress: abilityData.overallProgress,
    totalNodes: 0,
    completedNodes: 0
  };
}

// 初始化能力图谱
function initAbilityChart() {
  try {
    console.log('Initializing ability chart...');

    const canvas = document.getElementById('abilityChart');
    if (!canvas) {
      console.error('Canvas element not found');
      return;
    }

    const ctx = canvas.getContext('2d');
    if (!ctx) {
      console.error('Canvas context not found');
      return;
    }

    if (typeof Chart === 'undefined') {
      console.error('Chart.js not loaded');
      return;
    }

    const abilityData = generateAbilityMapData();
    console.log('Ability data for chart:', abilityData);

    // 显示总体掌握度
    const overallProgress = document.getElementById('overallProgress');
    const overallPercentage = document.getElementById('overallPercentage');
    if (overallProgress && overallPercentage) {
      overallProgress.style.width = `${abilityData.overallProgress}%`;
      overallPercentage.textContent = `${abilityData.overallProgress}%`;
      console.log('Overall progress updated to:', abilityData.overallProgress);
    } else {
      console.error('Overall progress elements not found');
    }

    // 生成能力详情
    const abilityDetails = document.getElementById('abilityDetails');
    if (abilityDetails) {
      abilityDetails.innerHTML = '';

      if (abilityData.chartData && abilityData.chartData.labels) {
        abilityData.chartData.labels.forEach((label, index) => {
          const mastery = abilityData.chartData.datasets[0].data[index];
          const detailCard = document.createElement('div');
          detailCard.className = 'bg-gray-700 rounded-lg p-3';
          detailCard.innerHTML = `
            <div class="flex justify-between items-center mb-1">
              <span class="font-medium">${label}</span>
              <span class="font-bold">${mastery}%</span>
            </div>
            <div class="w-full bg-gray-600 rounded-full h-2">
              <div class="bg-green-500 h-2 rounded-full" style="width: ${mastery}%"></div>
            </div>
          `;
          abilityDetails.appendChild(detailCard);
        });
        console.log('Ability details generated successfully');
      } else {
        console.error('Chart data or labels not found');
      }
    } else {
      console.error('Ability details container not found');
    }

    // 创建雷达图
    try {
      new Chart(ctx, {
        type: 'radar',
        data: abilityData.chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              angleLines: {
                color: 'rgba(255, 255, 255, 0.1)'
              },
              grid: {
                color: 'rgba(255, 255, 255, 0.1)'
              },
              pointLabels: {
                color: 'rgba(255, 255, 255, 0.8)'
              },
              ticks: {
                color: 'rgba(255, 255, 255, 0.5)',
                backdropColor: 'transparent'
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                color: 'rgba(255, 255, 255, 0.8)'
              }
            },
            tooltip: {
              enabled: true,
              backgroundColor: 'rgba(0, 0, 0, 0.85)',
              titleColor: 'white',
              bodyColor: 'white',
              borderColor: 'rgba(255, 255, 255, 0.2)',
              borderWidth: 1,
              padding: 12,
              cornerRadius: 6,
              boxPadding: 6,
              usePointStyle: true,
              mode: 'nearest',
              intersect: true,
              displayColors: false,
              callbacks: {
                title: function (context) {
                  const domainName = context[0]?.label || '';
                  return domainName;
                },
                label: function (context) {
                  const domainName = context.label;
                  const domainDetails = window.domainDetails && window.domainDetails[domainName];
                  const mastery = context.parsed.r || 0;

                  const lines = [];
                  lines.push(`掌握程度: ${mastery}%`);

                  if (domainDetails) {
                    lines.push(`总题目数: ${domainDetails.totalProblems || 0}`);
                    lines.push(`已通过: ${domainDetails.passedProblems || 0}`);

                    if (domainDetails.secondaryNodeMastery && Object.keys(domainDetails.secondaryNodeMastery).length > 0) {
                      lines.push('');
                      lines.push('二级节点掌握度:');
                      for (const [nodeName, nodeMastery] of Object.entries(domainDetails.secondaryNodeMastery)) {
                        lines.push(`${nodeName}: ${nodeMastery}%`);
                      }
                    }
                  }

                  return lines;
                }
              }
            }
          }
        }
      });
      console.log('Chart created successfully');
    } catch (chartError) {
      console.error('Error creating chart:', chartError);
    }
  } catch (error) {
    console.error('Error initializing ability chart:', error);
  }
}

// 初始化页面
function init() {
  console.log('Initializing ability map module...');

  try {
    setupBackButton();

    // 检查必要的全局变量是否存在
    const checkDependencies = () => {
      console.log('Checking dependencies...');
      console.log('window.treeData:', typeof window.treeData, window.treeData);
      console.log('window.problemSets:', typeof window.problemSets, window.problemSets);
      console.log('window.passedProblems:', typeof window.passedProblems, window.passedProblems);

      if (typeof window.treeData !== 'undefined' &&
        typeof window.problemSets !== 'undefined') {
        console.log('All dependencies found, initializing ability chart');
        initAbilityChart();
      } else {
        console.log('Waiting for dependencies...');
        setTimeout(checkDependencies, 100);
      }
    };

    checkDependencies();
  } catch (error) {
    console.error('Error during initialization:', error);
  }
}

// 在浏览器环境中，将模块导出到全局作用域
if (typeof window !== 'undefined') {
  window.abilityMap = window.abilityMap || {};
  window.abilityMap.setupBackButton = setupBackButton;
  window.abilityMap.generateAbilityData = generateAbilityData;
  window.abilityMap.generateAbilityMapData = generateAbilityMapData;
  window.abilityMap.initAbilityChart = initAbilityChart;
  window.abilityMap.init = init;

  // 保持对abilityCalculator的支持，确保与其他模块兼容
  window.abilityCalculator = window.abilityCalculator || {};
  window.abilityCalculator.buildTagMastery = buildTagMastery;
  window.abilityCalculator.calculateDomainMastery = calculateDomainMastery;
  window.abilityCalculator.calculateOverallMastery = calculateOverallMastery;
  window.abilityCalculator.generateAbilityData = generateAbilityData;
}

// 在Node.js环境中，使用CommonJS导出
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    buildTagMastery,
    calculateDomainMastery,
    calculateOverallMastery,
    generateAbilityData,
    setupBackButton,
    generateAbilityMapData,
    initAbilityChart,
    init
  };
}