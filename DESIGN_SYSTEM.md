# T-Pet 设计规范 (Design System)

> 版本: 1.0.0
> 更新日期: 2026-04-25
> 目标: 打造「克制、专注、无干扰」的编程学习 UI

---

## 1. 总体设计原则

### 核心价值观

| 原则 | 说明 | 优先级 |
|-----|------|-------|
| **内容优先** | 代码和内容是主角，UI 是配角 | P0 |
| **功能优先** | 每个 UI 元素必须有明确功能价值 | P0 |
| **克制装饰** | 宁可缺少装饰，也不能喧宾夺主 | P0 |
| **信息层级** | 代码 > 解释 > 操作 > 美化 | P1 |

### 设计哲学

```
「如果一个元素被移除后不影响功能，这个元素就应该被移除」
```

### 禁止行为（硬规则）

- ❌ 任何页面禁止使用 emoji 作为 UI 元素
- ❌ 禁止使用超过 2 种颜色的渐变
- ❌ 禁止使用 `shadow-lg` 及以上的阴影
- ❌ 禁止使用 `rounded-2xl` 及以上的圆角
- ❌ 禁止在代码展示区域使用背景色块

---

## 2. 颜色系统

### 设计目标

**完全适配 VSCode 暗色主题，使用 VSCode 内置变量确保一致性**

### 主色板

```css
:root {
  /* === 主色调 (Primary) === */
  /* 强调色 - 仅用于关键操作和选中状态 */
  --color-primary: var(--vscode-focusBorder);           /* #007acc 蓝色 */
  --color-primary-hover: var(--vscode-toolbar-hoverBackground);

  /* === 功能色 (Functional) === */
  --color-success: #4ec9b0;    /* 通过/正确 - 绿色 */
  --color-warning: #dcdcaa;    /* 警告 - 黄色 */
  --color-error: #f14c4c;      /* 错误/失败 - 红色 */
  --color-info: #3794ff;      /* 信息提示 - 蓝色 */

  /* === 文字色 (Text) === */
  --color-text-primary: var(--vscode-foreground);      /* #d4d4d4 主要文字 */
  --color-text-secondary: var(--vscode-descriptionForeground); /* 次要文字 */
  --color-text-muted: var(--vscode-disabledForeground); /* 禁用/弱化文字 */

  /* === 背景色 (Background) === */
  --color-bg-primary: var(--vscode-editor-background);   /* #1e1e1e 主背景 */
  --color-bg-secondary: var(--vscode-sideBar-background); /* #252526 次要背景 */
  --color-bg-tertiary: var(--vscode-input-background);    /* #3c3c3c 输入框背景 */
  --color-bg-hover: var(--vscode-toolbar-hoverBackground);/* #2a2d2e 悬停背景 */

  /* === 边框色 (Border) === */
  --color-border: var(--vscode-border);                  /* #454545 默认边框 */
  --color-border-light: var(--vscode-contrastBorder);    /* 分割线 */
}
```

### 难度等级配色

```css
/* 题目难度 - 仅使用低饱和度颜色 */
--difficulty-easy-bg: rgba(78, 201, 176, 0.15);
--difficulty-easy-text: #4ec9b0;

--difficulty-medium-bg: rgba(220, 220, 170, 0.15);
--difficulty-medium-text: #dcdcaa;

--difficulty-hard-bg: rgba(241, 76, 76, 0.15);
--difficulty-hard-text: #f14c4c;
```

### 禁止事项

- ❌ 禁止硬编码颜色值（#4F46E5 等）用于主要 UI
- ❌ 禁止使用高饱和度颜色作为背景
- ❌ 禁止使用纯白色 (#fff) 作为文字背景

---

## 3. 字体规范

### 字体栈

```css
:root {
  /* === UI 字体 === */
  --font-ui: var(--vscode-font-family);
  --font-ui-size: 13px;
  --font-ui-line-height: 1.5;

  /* === 代码字体 === */
  --font-code: var(--vscode-editor-font-family);
  --font-code-size: var(--vscode-editor-font-size);

  /* === 字号层级 === */
  --text-xs: 11px;      /* 辅助说明、标签 */
  --text-sm: 12px;      /* 次要信息、元数据 */
  --text-base: 13px;    /* 正文、默认大小 */
  --text-lg: 14px;      /* 标题、小标题 */
  --text-xl: 16px;      /* 页面标题 */
  --text-2xl: 18px;     /* 不推荐使用 */

  /* === 字重 === */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
}
```

### 使用场景

| 场景 | 字体 | 字号 | 字重 |
|-----|------|------|------|
| 代码展示 | var(--font-code) | var(--font-code-size) | normal |
| 正文内容 | var(--font-ui) | var(--text-base) | normal |
| 按钮文字 | var(--font-ui) | var(--text-sm) | var(--font-medium) |
| 标题 h1 | var(--font-ui) | var(--text-xl) | var(--font-semibold) |
| 标题 h2 | var(--font-ui) | var(--text-lg) | var(--font-medium) |
| 辅助说明 | var(--font-ui) | var(--text-sm) | normal |
| 标签/徽章 | var(--font-ui) | var(--text-xs) | var(--font-medium) |

---

## 4. 间距系统

### Spacing Scale

**基于 4px 网格系统**

```css
:root {
  --space-0: 0;
  --space-1: 4px;   /* 紧凑间距 */
  --space-2: 8px;   /* 标准元素内间距 */
  --space-3: 12px;  /* 组件内间距 */
  --space-4: 16px;  /* 组件间间距 */
  --space-5: 20px;  /* 区块内间距 */
  --space-6: 24px;  /* 区块间间距 */
  --space-8: 32px;  /* 页面级间距（慎用） */
  --space-10: 40px; /* 页面级间距（不推荐） */
}
```

### 典型使用场景

| 场景 | 间距 | 说明 |
|-----|------|------|
| 按钮内 padding | `--space-2` 水平, `--space-1` 垂直 | 紧凑 |
| 输入框 padding | `--space-2` | - |
| 卡片内边距 | `--space-3` 或 `--space-4` | - |
| 列表项 padding | `--space-3` 垂直, `--space-4` 水平 | - |
| 区块间间距 | `--space-4` | - |
| 页面边距 | `--space-4` | 保持一致 |

### 内边距规则

```css
/* ✅ 正确：统一内边距 */
.card {
  padding: var(--space-3);
}

/* ❌ 错误：混合使用不同间距 */
.card {
  padding: 12px 16px 10px 8px; /* 禁止 */
}
```

---

## 5. 圆角规范

### 核心规则

**仅允许 2 种圆角值，严格限制使用**

```css
:root {
  /* === 圆角系统 === */
  --radius-none: 0;           /* 默认 */
  --radius-sm: 2px;           /* 按钮、输入框 */
  --radius-md: 4px;           /* 卡片、面板 */

  /* === 禁止使用 === */
  /* --radius-lg: 6px;   允许但慎用 */
  /* --radius-xl: 8px;   禁止 */
  /* --radius-2xl: 12px; 禁止 */
  /* --radius-full: 9999px; 禁止 */
}
```

### 使用场景

| 元素 | 圆角 | 说明 |
|-----|------|------|
| 按钮 | `--radius-sm` | 2px |
| 输入框 | `--radius-sm` | 2px |
| 下拉框 | `--radius-sm` | 2px |
| 卡片/面板 | `--radius-md` | 4px |
| 头像 | `--radius-md` | 仅此场景可用 4px |
| Badge/标签 | `--radius-none` | 禁止圆角 |

### 禁用示例

```css
/* ❌ 禁止 */
.rounded-xl { border-radius: 12px; }
.rounded-2xl { border-radius: 16px; }
.rounded-full { border-radius: 9999px; }

/* ✅ 正确 */
.btn { border-radius: var(--radius-sm); }
.card { border-radius: var(--radius-md); }
```

---

## 6. 组件规范

### 6.1 按钮 (Button)

#### 类型定义

```css
:root {
  /* === 按钮变量 === */
  --btn-height: 26px;
  --btn-padding-x: var(--space-3);
  --btn-font-size: var(--text-sm);
  --btn-radius: var(--radius-sm);
}
```

#### 按钮类型

```css
/* 主按钮 - 仅用于主要操作，每个页面最多 1-2 个 */
.btn-primary {
  background: var(--color-primary);
  color: #fff;
  border: none;
  border-radius: var(--btn-radius);
  padding: var(--space-1) var(--btn-padding-x);
  font-size: var(--btn-font-size);
  font-weight: var(--font-medium);
  cursor: pointer;
  transition: background 0.15s ease;
}

.btn-primary:hover {
  background: var(--color-primary-hover);
}

/* 次要按钮 - 用于一般操作 */
.btn-secondary {
  background: var(--color-bg-tertiary);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--btn-radius);
  padding: var(--space-1) var(--btn-padding-x);
  font-size: var(--btn-font-size);
  cursor: pointer;
}

.btn-secondary:hover {
  background: var(--color-bg-hover);
}

/* 幽灵按钮 - 用于次要操作、工具栏 */
.btn-ghost {
  background: transparent;
  color: var(--color-text-primary);
  border: none;
  border-radius: var(--btn-radius);
  padding: var(--space-1);
  font-size: var(--btn-font-size);
}

.btn-ghost:hover {
  background: var(--color-bg-hover);
}

/* 危险按钮 - 用于删除等危险操作 */
.btn-danger {
  background: transparent;
  color: var(--color-error);
  border: 1px solid var(--color-error);
  border-radius: var(--btn-radius);
  padding: var(--space-1) var(--btn-padding-x);
  font-size: var(--btn-font-size);
}

.btn-danger:hover {
  background: rgba(241, 76, 76, 0.1);
}
```

#### 按钮使用原则

- ✅ 页面主操作使用 `btn-primary`
- ✅ 次要操作使用 `btn-secondary` 或 `btn-ghost`
- ✅ 工具栏使用 `btn-ghost`
- ❌ 避免连续使用超过 3 个 `btn-primary`
- ❌ 避免在同一行混合使用 `btn-primary` 和 `btn-secondary`

---

### 6.2 卡片 (Card)

```css
.card {
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-3);
}

/* 卡片悬停效果 - 仅在可交互时使用 */
.card-interactive:hover {
  border-color: var(--color-primary);
  cursor: pointer;
}

/* 卡片标题 */
.card-title {
  font-size: var(--text-lg);
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
  margin-bottom: var(--space-2);
}
```

#### 卡片使用原则

- ✅ 信息展示使用卡片
- ✅ 可点击项使用 `card-interactive`
- ❌ 禁止在卡片内使用阴影
- ❌ 禁止在卡片内使用渐变背景

---

### 6.3 输入框 (Input)

```css
.input {
  background: var(--color-bg-tertiary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-1) var(--space-2);
  font-size: var(--text-base);
  font-family: var(--font-ui);
  color: var(--color-text-primary);
  outline: none;
  width: 100%;
}

.input:focus {
  border-color: var(--color-primary);
}

.input::placeholder {
  color: var(--color-text-muted);
}

/* 文本域 */
.textarea {
  min-height: 80px;
  resize: vertical;
}
```

#### 输入框使用原则

- ✅ 占位符文字使用 `--color-text-muted`
- ✅ 输入框宽度 100%
- ✅ 相关输入框垂直间距 `--space-3`
- ❌ 禁止在输入框内使用 `rounded-lg` 等大圆角

---

### 6.4 代码块 (Code Block)

```css
.code-block {
  background: var(--color-bg-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-3);
  font-family: var(--font-code);
  font-size: var(--font-code-size);
  color: var(--color-text-primary);
  overflow-x: auto;
  line-height: 1.6;
}

/* 行内代码 */
.code-inline {
  background: var(--color-bg-tertiary);
  border-radius: 2px;
  padding: 0 var(--space-1);
  font-family: var(--font-code);
  font-size: 0.9em;
}
```

#### 代码块使用原则

- ✅ 代码块背景使用主背景色
- ✅ 代码块无圆角或仅 2px 圆角
- ✅ 使用等宽字体
- ❌ 禁止在代码块内使用彩色背景
- ❌ 禁止在代码块内使用 emoji

---

### 6.5 提示信息 (Info / Warning / Error)

```css
/* 提示容器 - 无圆角 */
.alert {
  padding: var(--space-2) var(--space-3);
  border-left: 3px solid;
  font-size: var(--text-sm);
}

/* 信息提示 */
.alert-info {
  background: rgba(55, 148, 255, 0.1);
  border-color: var(--color-info);
  color: var(--color-text-primary);
}

/* 警告提示 */
.alert-warning {
  background: rgba(220, 220, 170, 0.1);
  border-color: var(--color-warning);
  color: var(--color-text-primary);
}

/* 错误提示 */
.alert-error {
  background: rgba(241, 76, 76, 0.1);
  border-color: var(--color-error);
  color: var(--color-text-primary);
}

/* 成功提示 */
.alert-success {
  background: rgba(78, 201, 176, 0.1);
  border-color: var(--color-success);
  color: var(--color-text-primary);
}
```

#### 提示信息使用原则

- ✅ 使用左侧边框样式，无圆角
- ✅ 每种类型仅显示 1 个
- ❌ 禁止使用图标
- ❌ 禁止使用大块背景色

---

### 6.6 列表 (List)

```css
.list {
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.list-item {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.list-item:last-child {
  border-bottom: none;
}

.list-item:hover {
  background: var(--color-bg-hover);
}
```

#### 列表使用原则

- ✅ 列表项之间使用分割线
- ✅ 悬停状态使用 `var(--color-bg-hover)`
- ❌ 禁止在列表项间添加间距

---

## 7. 禁用项（非常重要）

### 硬性禁止规则

| 禁止项 | 违规示例 | 替代方案 |
|-------|---------|---------|
| **Emoji** | ✅ ❌ 🔥 💡 🎯 | 使用文字或简单图标 |
| **大面积渐变** | `bg-gradient-to-r from-blue-500 to-purple-500` | 纯色或 2 色点渐变 |
| **大圆角** | `rounded-xl`, `rounded-2xl`, `rounded-full` | `rounded-sm` (2px) 或 `rounded-md` (4px) |
| **过度阴影** | `shadow-lg`, `shadow-xl`, `shadow-2xl` | `shadow-sm` 或无阴影 |
| **高饱和色** | `#ff0000`, `#00ff00` | VSCode 变量色 |
| **纯白背景** | `background: #fff` | `var(--color-bg-secondary)` |
| **复杂边框** | `border-2 border-blue-500` | `border` (1px) |

### Tailwind 禁用类

```
❌ rounded-2xl, rounded-3xl, rounded-full
❌ shadow-lg, shadow-xl, shadow-2xl
❌ bg-gradient-to-*, from-*, to-*
❌ text-2xl, text-3xl, text-4xl (仅允许 xs/sm/base/lg)
❌ p-6, p-8, p-10 (超过 space-4)
❌ m-6, m-8, m-10
❌ ring-*, outline-2
```

---

## 8. VSCode 插件适配原则

### 核心策略

**最大程度复用 VSCode 原生样式，减少自定义**

### 配色适配

```css
/* ✅ 正确：使用 VSCode 变量 */
body {
  background: var(--vscode-editor-background);
  color: var(--vscode-foreground);
  font-family: var(--vscode-font-family);
}

/* ❌ 错误：硬编码颜色 */
body {
  background: #1e1e1e;
  color: #d4d4d4;
}
```

### 优先使用的 VSCode 变量

```css
/* 背景 */
--vscode-editor-background
--vscode-sideBar-background
--vscode-panel-background
--vscode-input-background

/* 文字 */
--vscode-foreground
--vscode-descriptionForeground
--vscode-disabledForeground

/* 边框 */
--vscode-border
--vscode-focusBorder

/* 按钮 */
--vscode-button-background
--vscode-button-foreground
--vscode-button-secondaryBackground

/* 工具栏 */
--vscode-toolbar-hoverBackground
```

### 交互行为适配

```css
/* 焦点样式 - 必须使用 VSCode 焦点边框 */
*:focus {
  outline-color: var(--vscode-focusBorder) !important;
}

/* 悬停样式 - 使用 VSCode 工具栏悬停色 */
.interactive:hover {
  background: var(--vscode-toolbar-hoverBackground);
}
```

### Webview 字体加载

```javascript
// 在 Webview 中获取 VSCode 字体
const vscode = acquireVsCodeApi();

// 字体自动继承 VSCode 设置
// 确保 CSS 使用 var(--vscode-font-family)
```

### 响应式策略

**保持简洁，不做复杂响应式**

- 最大宽度: 1000px
- 容器内边距: `--space-4`
- 移动端: 简单堆叠布局

---

## 9. 文件结构建议

```
media/
├── styles/
│   ├── variables.css      # CSS 变量定义
│   ├── base.css           # 重置样式
│   ├── button.css         # 按钮组件
│   ├── card.css           # 卡片组件
│   ├── input.css          # 输入框组件
│   ├── alert.css          # 提示组件
│   └── list.css           # 列表组件
├── components/            # 如果需要原生组件封装
│   └── ...
└── pages/                # 页面级样式（尽量简化）
    ├── menu.css
    ├── calendar.css
    └── ...
```

### CSS 文件引用顺序

```html
<head>
  <link href="vscode.css" rel="stylesheet">  <!-- VSCode 变量优先 -->
  <link href="styles/variables.css" rel="stylesheet">
  <link href="styles/base.css" rel="stylesheet">
  <link href="styles/button.css" rel="stylesheet">
  <!-- 页面特定样式 -->
</head>
```

---

## 10. 速查表

### 颜色变量

| 变量 | 用途 |
|-----|------|
| `--color-primary` | 主要操作 |
| `--color-success` | 成功/通过 |
| `--color-warning` | 警告 |
| `--color-error` | 错误/危险 |
| `--color-bg-primary` | 主背景 |
| `--color-bg-secondary` | 次背景 |
| `--color-bg-tertiary` | 输入框背景 |
| `--color-text-primary` | 主要文字 |
| `--color-text-secondary` | 次要文字 |

### 间距速查

| 变量 | 像素 |
|-----|------|
| `--space-1` | 4px |
| `--space-2` | 8px |
| `--space-3` | 12px |
| `--space-4` | 16px |

### 圆角速查

| 变量 | 像素 | 用途 |
|-----|------|------|
| `--radius-none` | 0 | 默认 |
| `--radius-sm` | 2px | 按钮/输入框 |
| `--radius-md` | 4px | 卡片 |

### 字号速查

| 变量 | 像素 | 用途 |
|-----|------|------|
| `--text-xs` | 11px | 标签 |
| `--text-sm` | 12px | 次要信息 |
| `--text-base` | 13px | 正文 |
| `--text-lg` | 14px | 小标题 |
| `--text-xl` | 16px | 页面标题 |

---

## 附录：迁移检查清单

当修改现有文件时，逐项检查：

- [ ] 是否使用了 CSS 变量而非硬编码颜色
- [ ] 是否使用了规定的 spacing 值
- [ ] 是否使用了规定的 border-radius
- [ ] 是否移除了所有 emoji
- [ ] 是否移除了所有渐变背景
- [ ] 是否移除了所有超过 `--radius-md` 的圆角
- [ ] 是否移除了所有 `shadow-lg` 及以上阴影
- [ ] 是否遵循了组件规范

---

> 设计规范由 AI 辅助制定，基于 VSCode/GitHub/Linear 的设计语言。
> 最后更新: 2026-04-25
