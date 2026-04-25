# 代码助手

> 一款专为算法学习设计的 VS Code 插件，通过知识树和能力图谱辅助算法学习，提高学习效率，同时配备 AI 助教辅助学习，帮助回答问题和制定学习计划，还有可爱的 Live2D 萌宠陪伴左右，为你的算法之旅加油鼓劲！

## Features

- **知识树模块**：将算法知识点构建为树状结构，引导你系统化地学习
- **能力图谱**：自动记录你在知识树上的学习进度，并转化为可视化的能力图谱
- **智能 AI 助教**：基于你的能力图谱和学习进度，提供个性化建议与题目分析
- **Live2D 萌宠**：在学习过程中全程陪伴，点击互动即可获得随机鼓励
- **推荐题单**：根据当前学习情况智能推荐适合你的题目
- **打卡日历**：记录每日刷题进度，培养持续学习的习惯

---

## Installation

### VS Code 扩展商店安装（推荐）

1. 打开 VS Code
2. 进入扩展面板（`Ctrl+Shift+X`）
3. 搜索 `Code Assistant`
4. 点击 **Install** 安装

### GitHub 下载

本项目开源地址：

```
https://github.com/dim273/t-pet
```

---

## Usage

安装完成后，在侧边栏「资源管理器」底部会出现 `code-assistant` 面板。注册账号并登录后即可进入主界面（支持多账号切换）。

### 功能按钮说明

主界面功能入口如下：

| 按钮 | 功能 |
|------|------|
| 知识树 | 浏览算法知识点树状结构 |
| AI 助手 | 获取解题思路、学习规划等个性化建议 |
| 打卡日历 | 查看每日完成情况与连续打卡记录 |
| 推荐题单 | 基于当前进度智能推荐题目 |
| 能力图谱 | 查看个人能力雷达图与学习分析 |
| 设置 | 配置 Live2D 显示及各项参数 |

### 刷题流程

**1. 知识树导航**

- 各算法知识点以树状结构组织，完成前置节点后方可解锁后续节点
- 点击任意节点即可进入对应的题单页面

**2. 选择题目**

- 在知识树节点中点击子节点，或从推荐题单进入题列表
- 在题单中点击题目即可查看详情页（含完整题目描述）

**3. 提交判题**

- 在编辑器中完成代码后保存，点击详情页的「提交」按钮即可运行测试
- 测试通过后该题目会被自动标记为已完成

### AI 助手使用指南

**1. 基本操作**

- 点击「AI 助手」按钮进入对话界面
- 可就算法相关问题向 AI 提问
- 点击左上角 `≡` 图标可查看历史对话记录

**2. 题目分析**

- 在题目详情页点击「AI 问题分解」，可直接将该题发送给 AI 分析
- AI 不会直接给出完整答案，而是拆解问题思路，引导你自主解决

**3. API 配置**

- AI 默认使用内置测试 API，可能存在响应延迟或额度耗尽的情况
- 可在设置中更换为你自己的 API Key 以获得更稳定的服务

### Live2D 萌宠使用指南

打开侧边栏面板即可看到 Live2D 萌宠及其功能按钮。

**1. 基础配置**

- 进入「设置」→「萌宠设置」可对 Live2D 进行全面配置：
  - 启动/关闭 Live2D（默认显示于右下角）
  - 保存当前状态：调整位置和缩放后保存，下次启动自动恢复
  - 重置默认位置：当拖拽异常时一键还原
  - 自启动：开启后 VS Code 启动时 Live2D 自动加载
  - 定位锚点：设置萌宠的参照角

**2. 依赖管理**

- 插件依赖文件会在首次启动时自动生成
- 若 Live2D 无法正常显示，可尝试点击「重新生成」强制覆盖配置
- 卸载插件前请务必执行「移除操作」以恢复 VS Code 文件变更

**3. 交互功能**

- 目光跟随鼠标移动
- 点击触发随机鼓励语与动作
- 快捷访问刷题平台网站
- 切换不同模型形象
- 查看模型来源信息

### 补充功能

- **智能推荐**：根据当前学习进度动态生成个性化题单，精准提升薄弱环节
- **能力可视化**：基于刷题数据生成专属能力图谱，直观展示各方向掌握程度

---

## 注意事项

- 个别题目可能出现提交正确但未通过的情况，建议在原网站验证后，通过题目详情页上方的「标记完成」手动确认
- 内置 AI API 存在额度限制，如遇无法使用的情况，请在设置中替换为自有 API Key
- 部分 Live2D 模型可能因 VS Code 版本、操作系统或插件兼容性导致显示异常
- 请确保网络连接正常，部分功能（AI 助教、Live2D 模型加载）需要联网使用

---

## Uninstall

卸载前请依次执行以下操作：

1. 进入设置 → 移除依赖项（恢复对 VS Code 文件的修改）
2. 注销账号（清除本地用户数据）
3. 在扩展列表中卸载本插件

---

## Configuration

在 VS Code 设置中搜索 `code-assistant` 即可找到相关配置项。

### 常用配置

```jsonc
// settings.json
{
  "vscode-live2d-asoul.enabled": true  // 是否启用 Live2D 萌宠（默认: true）
}
```

### 配置方式

1. 打开 VS Code 设置（`Ctrl+,`）
2. 搜索 `code-assistant`
3. 根据需求调整各项参数

或直接编辑 `settings.json`：

```jsonc
{
  "vscode-live2d-asoul.enabled": true
}
```

---

## Technical Details

### Live2D 实现

本插件的 Live2D 功能基于 [A-SOUL-live2d](https://github.com/TheSecondAkari/vscode-live2d) 项目实现，感谢原作者的开源贡献。

核心特性：

- 基于 Pixi.js 实现高性能渲染
- 支持模型动作切换与表情变化
- 流畅的动画效果与触摸/点击交互响应
- 自适应屏幕缩放

### 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | VS Code Extension API |
| Live2D 渲染 | Pixi.js + Live2D Cubism SDK |
| 语言 | JavaScript |
| 构建工具 | webpack / vsce |

## Project Structure

```
t-pet/
├── manager/                     # 数据获取模块（LeetCode / 洛谷题目抓取）
├── media/                       # 前端界面模块
│   ├── AbilityMap/              # 能力图谱：学习进度可视化呈现
│   ├── AIAssistant/             # AI 助教：个性化建议与题目分析
│   ├── Login/                   # 用户登录注册
│   ├── TreeNode/                # 知识树：算法知识点树形展示
│   ├── ProblemList/             # 题目列表（1500+ 道算法题）
│   ├── ProblemPage/             # 单题详情页
│   ├── RecommendProblemList/    # 智能推荐题单
│   └── Menu/                    # 主菜单导航
├── out/                         # 编译输出目录
│   ├── live2dView/index.js      # 前端视图控制器与路由管理
│   └── live2dModify/            # Live2D 资源注入与修改器
├── res/                         # 静态资源
│   ├── live2d/                  # Live2D 吉祥物（模型 / 渲染引擎 / 配置）
│   ├── image/                   # 图片资源（图标、背景等）
│   ├── Problem/                 # 算法题目库（150+ 道 .md 题目）
│   ├── JudgeData/               # 判题机配置脚本
│   └── katex/                   # KaTeX 数学公式渲染库
├── saveData/data.json           # 用户本地学习记录
├── tests/                       # 单元测试
└── package.json                 # 插件配置文件
```

如有其他问题，欢迎提 Issue 反馈！

---

## Contributing

欢迎参与贡献！你可以通过以下方式帮助改进本项目：

1. **提出建议**：在 Issues 中提交功能需求或改进想法
2. **报告问题**：发现 Bug 请及时反馈，附上复现步骤
3. **提交代码**：Fork 项目并通过 Pull Request 提交改动
4. **完善文案**：帮助优化鼓励性对话等内容

---

## License

本项目基于 MIT License 开源。详见 [LICENSE](LICENSE) 文件。

---

## Acknowledgments

感谢以下开源项目与作者：

- [A-SOUL-live2d](https://github.com/TheSecondAkari/vscode-live2d) — Live2D 核心实现
- [live2d-widget](https://github.com/stevenjoezhang/live2d-widget) — Live2D 组件库
- [vscode-background](https://github.com/shalldie/vscode-background) — VS Code 背景方案参考
- [CharlesZ.vscode-live2d](https://marketplace.visualstudio.com/items?itemName=CharlesZ.vscode-live2d) — VSCode Live2D 方案
- [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) — Pixi.js Live2D 渲染器
- [pio](https://paugram.com/) — Pio 插件框架
- [journey-ad](https://github.com/journey-ad) — Pio 框架修改版

---

*Enjoy Learning!*

*让算法学习变得更有趣~*
