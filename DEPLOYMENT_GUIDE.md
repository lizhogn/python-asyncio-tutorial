# Docsify 部署指南

## 🎉 恭喜！你的 Asyncio 学习项目文档已经准备就绪

现在你可以通过以下方式访问和部署你的文档：

## 📖 本地预览

docsify 服务器已经在后台运行，你可以通过以下地址访问：

```
http://localhost:3000
```

### 手动启动服务器

如果服务器没有运行，可以使用以下命令启动：

```bash
# 安装 docsify-cli（如果未安装）
npm install -g docsify-cli

# 启动服务器
docsify serve docs
```

## ✨ 功能特性

### 代码高亮
- ✅ 支持 Python、JavaScript、Bash、JSON、HTML、CSS 等多种语言
- ✅ 使用 Prism.js 提供专业的代码高亮
- ✅ 暗色主题，保护眼睛
- ✅ 自动语言检测

### 其他功能
- ✅ 侧边栏导航
- ✅ 搜索功能
- ✅ 响应式设计
- ✅ 中文界面

## 🚀 部署到 GitHub Pages

### 步骤 1: 创建 GitHub 仓库

1. 在 GitHub 上创建一个新的仓库
2. 仓库名称建议：`asyncio-learning` 或 `python-asyncio-tutorial`

### 步骤 2: 推送代码到 GitHub

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: Asyncio learning project with docsify"

# 添加远程仓库（替换为你的仓库 URL）
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 推送到 GitHub
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 进入你的 GitHub 仓库
2. 点击 "Settings" 标签
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分选择 "Deploy from a branch"
5. 在 "Branch" 下拉菜单中选择 "main"
6. 在 "Folder" 下拉菜单中选择 "/docs"
7. 点击 "Save"

### 步骤 4: 访问你的网站

几分钟后，你的文档网站将在以下地址可用：

```
https://你的用户名.github.io/你的仓库名/
```

## 📁 项目结构

```
learning_ays/
├── docs/                          # Docsify 文档目录
│   ├── index.html                 # Docsify 入口文件（包含代码高亮配置）
│   ├── _sidebar.md                # 侧边栏导航
│   ├── README.md                  # 首页
│   ├── LEARNING_GUIDE.md          # 学习指南
│   ├── test-highlight.md          # 代码高亮测试页面
│   ├── 01_basics/                 # 基础概念
│   │   ├── 01_what_is_async.md
│   │   ├── 02_coroutines.md
│   │   └── 03_event_loop.md
│   ├── 02_core_components/        # 核心组件
│   │   └── 01_tasks.md
│   ├── 04_practical_examples/     # 实际应用
│   │   └── 01_async_web_requests.md
│   ├── exercises/                 # 练习
│   │   ├── 01_basic_exercises.md
│   │   └── 01_basic_exercises_solutions.md
│   └── requirements.txt           # 依赖说明
├── 01_basics/                     # 原始 Python 示例
├── 02_core_components/
├── 04_practical_examples/
├── exercises/
├── requirements.txt
├── README.md
├── LEARNING_GUIDE.md
└── DEPLOYMENT_GUIDE.md
```

## 🔧 自定义配置

### 修改网站标题

编辑 `docs/index.html` 中的 `name` 字段：

```javascript
window.$docsify = {
  name: '你的项目名称',
  // ... 其他配置
}
```

### 添加 GitHub 链接

在 `docs/index.html` 中添加仓库链接：

```javascript
window.$docsify = {
  name: 'Asyncio 学习项目',
  repo: 'https://github.com/你的用户名/你的仓库名',
  // ... 其他配置
}
```

### 自定义主题

docsify 支持多种主题，你可以在 `docs/index.html` 中修改：

```html
<!-- 默认主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">

<!-- 暗色主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/dark.css">

<!-- 其他主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/buble.css">
```

### 代码高亮主题

当前使用的是 `prism-tomorrow` 主题（暗色），你可以更换为其他主题：

```html
<!-- 当前主题：暗色 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css">

<!-- 其他可选主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css">
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-okaidia.min.css">
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-solarizedlight.min.css">
```

## 📝 添加新内容

### 添加新的学习模块

1. 在 `docs/` 目录下创建新的文件夹
2. 添加对应的 `.md` 文件
3. 在 `docs/_sidebar.md` 中添加导航链接

### 更新现有内容

直接编辑对应的 `.md` 文件，docsify 会自动重新加载。

### 代码高亮使用

在 markdown 文件中使用代码高亮：

```markdown
```python
async def hello_world():
    print("Hello, World!")
```

```javascript
function greet() {
    console.log("Hello, World!");
}
```

```bash
echo "Hello, World!"
```
```

## 🌟 高级功能

### 添加数学公式

如果需要数学公式支持，可以在 `docs/index.html` 中添加：

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/mathjax.min.js"></script>
```

### 添加图表

如果需要图表支持，可以添加 Mermaid：

```html
<script src="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: true });
</script>
```

### 添加复制代码按钮

可以在 `docs/index.html` 中添加复制代码功能：

```html
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code@2"></script>
```

## 🐛 常见问题

### Q: 页面显示空白怎么办？
A: 检查浏览器控制台是否有错误，确保所有文件路径正确。

### Q: 侧边栏不显示怎么办？
A: 确保 `_sidebar.md` 文件存在且格式正确。

### Q: 代码高亮不工作怎么办？
A: 确保在代码块中正确指定了语言，例如 ```python。

### Q: 本地预览正常，但 GitHub Pages 不工作怎么办？
A: 检查 GitHub Pages 设置，确保选择了正确的分支和文件夹。

### Q: 代码高亮主题不显示怎么办？
A: 检查网络连接，确保能访问 CDN 资源。

## 🎯 下一步

1. **测试代码高亮**：访问 `http://localhost:3000/test-highlight.md` 查看效果
2. **部署到 GitHub Pages**：按照上述步骤部署你的文档
3. **分享链接**：将你的文档链接分享给其他人
4. **持续更新**：根据需要添加新的学习内容
5. **收集反馈**：邀请其他人使用并提供反馈

恭喜你成功创建了一个完整的 Asyncio 学习项目文档，包含专业的代码高亮功能！🎉 