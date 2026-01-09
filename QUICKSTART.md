# 🚀 快速入门指南

欢迎！这个指南将帮助你在30分钟内开始使用智能开发助手。

## 📦 第一步：安装依赖

```bash
# 进入项目目录
cd /home/user/doyos-

# 安装Python依赖
cd dev-assistant
pip install -r requirements.txt
```

## 🎯 第二步：启动智能助手

```bash
# 运行助手
python assistant.py
```

你将看到欢迎界面和主菜单：

```
============================================================
              🤖 AI电影引擎智能开发助手
============================================================

欢迎！我是你的智能开发助手
项目: AI电影引擎
当前阶段: planning
完成度: 0%

📋 主菜单
--------------------------------------------------
  1. 🎯 查看今日任务
  2. ➕ 添加新任务
  3. 📊 查看项目进度
  4. 🗺️  查看开发路线图
  5. 💡 获取AI建议
  6. 📱 同步到iPhone
  7. ⚙️  配置设置
  8. 📈 生成进度报告
  9. 🎓 开发指南
  0. 👋 退出

请选择操作 (0-9):
```

## 🗺️ 第三步：查看开发路线图

输入 `4` 查看完整的开发路线图，了解项目的各个阶段和任务。

```
请选择操作 (0-9): 4
```

你将看到：
- MVP第一阶段：用户认证、项目管理、剧本编辑器
- MVP第二阶段：AI视频生成、视频剪辑
- MVP第三阶段：音频功能、渲染系统

每个功能都有详细的工时估算和具体任务分解。

## ➕ 第四步：添加你的第一个任务

输入 `2` 添加任务：

```
请选择操作 (0-9): 2

➕ 添加新任务
--------------------------------------------------
任务名称: 搭建Next.js前端项目
任务描述: 初始化Next.js 14，配置TypeScript和Tailwind CSS
优先级 (high/medium/low): high
预计时间（小时）: 4

✓ 任务已添加！
是否要同步到iPhone日历？(y/n): n
```

## 💡 第五步：获取AI建议

输入 `5` 获取针对你当前进度的开发建议：

```
请选择操作 (0-9): 5

💡 AI建议
--------------------------------------------------
基于你的当前进度，我有以下建议：

📌 建议1: 从MVP第一阶段开始
   先实现用户认证系统，这是所有功能的基础

📌 建议2: 搭建开发环境
   - 前端: 初始化Next.js项目
   - 后端: 选择Node.js或Python框架
   - 数据库: 安装PostgreSQL

📌 建议3: 设计数据库架构
   先设计用户、项目、资产等核心表结构

💭 记住：优先完成核心功能，避免过度设计！
```

## 📱 第六步：配置iPhone同步（可选）

如果你想将任务同步到iPhone日历和提醒，输入 `7` 进行配置：

```
请选择操作 (0-9): 7

⚙️  配置向导
--------------------------------------------------
项目名称 [AI电影引擎]:
每周工作时间 [30]:

是否配置iPhone日历同步? (y/n): y

选择同步方式:
  1. iCloud日历 (推荐)
  2. 快捷指令
  3. 稍后配置
```

详细的iPhone集成指南请查看：`dev-assistant/IPHONE_INTEGRATION.md`

## 📖 项目文档结构

```
doyos-/
├── README.md                          # 项目说明
├── DEV_CHECKLIST.md                   # 通用开发检查清单
├── QUICKSTART.md                      # 本文档
├── docs/
│   ├── PROJECT_OVERVIEW.md            # 项目概览（必读！）
│   └── ROADMAP.md                     # 详细开发路线图
├── dev-assistant/
│   ├── README.md                      # 助手系统说明
│   ├── IPHONE_INTEGRATION.md          # iPhone集成指南
│   ├── assistant.py                   # 主程序
│   ├── config.yaml                    # 配置文件
│   └── requirements.txt               # Python依赖
└── src/
    ├── frontend/                      # 前端代码（待创建）
    ├── backend/                       # 后端代码（待创建）
    └── ai-engine/                     # AI引擎（待创建）
```

## 📚 必读文档

### 1. 项目概览 (10分钟)
```bash
cat docs/PROJECT_OVERVIEW.md
```

了解：
- 🎬 项目愿景和核心功能
- 💡 推荐的技术栈
- 🎯 MVP功能划分
- 📊 商业模式

### 2. 开发路线图 (15分钟)
```bash
cat docs/ROADMAP.md
```

了解：
- 📅 详细的时间规划
- 📋 每周任务分解
- 🎯 里程碑设置
- 💡 成功建议

### 3. 开发助手系统 (5分钟)
```bash
cat dev-assistant/README.md
```

了解：
- 🤖 助手功能详解
- 🏗️ 系统架构
- 📱 iPhone集成方案
- 🛠️ 使用技巧

## 🎯 接下来做什么？

### 初学者路径
1. ✅ 阅读 `docs/PROJECT_OVERVIEW.md` 了解项目全貌
2. ✅ 阅读 `docs/ROADMAP.md` 了解开发计划
3. ✅ 搭建开发环境（安装Node.js、Python、PostgreSQL）
4. ✅ 开始第一个任务：初始化前端项目

### 推荐的第一周任务
```
Week 1 目标：搭建开发环境

□ Day 1-2: 环境搭建
  - 安装所有必要工具
  - 配置VS Code
  - 创建GitHub仓库

□ Day 3-4: 前端初始化
  - 创建Next.js项目
  - 配置TypeScript
  - 设置UI库

□ Day 5-6: 后端初始化
  - 创建FastAPI项目
  - 配置数据库连接
  - 设计初始表结构

□ Day 7: 学习和规划
  - 学习相关技术文档
  - 规划下周任务
  - 生成周报
```

## 💻 命令行快捷方式

除了交互模式，你也可以直接使用命令：

```bash
# 查看今日任务
python assistant.py today

# 查看项目进度
python assistant.py progress

# 查看路线图
python assistant.py roadmap

# 获取AI建议
python assistant.py advice

# 同步到iPhone
python assistant.py sync

# 生成进度报告
python assistant.py report

# 配置助手
python assistant.py configure
```

## 🔧 环境要求

### 必需
- Python 3.9+
- Node.js 18+ (用于前端开发)
- Git

### 推荐
- PostgreSQL 14+ (数据库)
- Docker Desktop (容器化)
- VS Code (编辑器)

### 可选
- Redis (缓存)
- FFmpeg (视频处理)

## 📱 iPhone集成选项

选择最适合你的方式：

| 方式 | 配置时间 | 功能 | 推荐指数 |
|------|---------|------|---------|
| 🥇 iCloud CalDAV | 10分钟 | 完整同步 | ⭐⭐⭐⭐⭐ |
| 🥈 快捷指令 | 15分钟 | 灵活自定义 | ⭐⭐⭐⭐ |
| 🥉 手动导出.ics | 2分钟 | 基础功能 | ⭐⭐⭐ |

详细配置请参考：`dev-assistant/IPHONE_INTEGRATION.md`

## 🆘 遇到问题？

### 常见问题

**Q: 助手无法启动**
```bash
# 确保依赖已安装
pip install -r requirements.txt

# 检查Python版本
python --version  # 应该是 3.9+
```

**Q: 找不到某个模块**
```bash
# 重新安装依赖
pip install -r requirements.txt --upgrade
```

**Q: 配置文件错误**
```bash
# 删除配置文件，重新配置
rm dev-assistant/config.yaml
python assistant.py configure
```

### 获取帮助

1. 查看详细文档：`dev-assistant/README.md`
2. 查看iPhone集成指南：`dev-assistant/IPHONE_INTEGRATION.md`
3. 查看开发路线图：`docs/ROADMAP.md`

## 🎉 准备好了吗？

现在你已经准备好开始开发了！

```bash
# 启动智能助手
python assistant.py

# 或查看今日建议
python assistant.py advice
```

**记住**：
- 💡 从小处着手，逐步迭代
- 📝 经常使用助手跟踪进度
- 🎯 专注于核心功能
- 🚀 完成比完美更重要

**祝你开发顺利！ 🎬**

---

**下一步建议**：
1. 运行 `python assistant.py` 启动助手
2. 选择 "4. 查看开发路线图"
3. 选择 "2. 添加新任务" 开始规划
4. 阅读 `docs/PROJECT_OVERVIEW.md` 了解项目详情
