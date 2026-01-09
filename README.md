# 🎬 AI电影引擎

全流程AI电影制作平台 - 从创意到成片的智能化解决方案

## 📖 项目简介

AI电影引擎是一个创新的Web应用，利用最新的AI技术，帮助创作者完成从剧本创作、分镜头设计、视频生成、智能剪辑到最终渲染的完整电影制作流程。

### 核心功能
- 🤖 **AI剧本创作**: 智能生成和优化剧本
- 🎨 **角色场景设计**: AI辅助角色和场景概念设计
- 🎥 **AI视频生成**: 集成主流AI视频生成模型
- ✂️ **智能剪辑**: 自动剪辑和时间轴编辑
- 🎵 **音频制作**: AI配音、音效和背景音乐
- 🎬 **后期特效**: 智能调色、特效和字幕

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/dycomic123-blip/doyos-.git
cd doyos-

# 启动智能开发助手
cd dev-assistant
pip install -r requirements.txt
python assistant.py
```

详细教程请查看 [快速入门指南](QUICKSTART.md)

## 📚 文档导航

| 文档 | 说明 | 适合 |
|------|------|------|
| [快速入门](QUICKSTART.md) | 30分钟上手指南 | 所有人 |
| [项目概览](docs/PROJECT_OVERVIEW.md) | 功能详解、技术栈、MVP规划 | 开发者 |
| [开发路线图](docs/ROADMAP.md) | 详细的开发计划和时间线 | 项目管理 |
| [开发检查清单](DEV_CHECKLIST.md) | 通用软件开发流程清单 | 开发者 |
| [智能助手](dev-assistant/README.md) | AI开发助手系统说明 | 开发者 |
| [iPhone集成](dev-assistant/IPHONE_INTEGRATION.md) | 任务同步到iPhone | iOS用户 |

## 🤖 智能开发助手

本项目配备了一个智能开发助手，帮助你：
- 📋 规划和跟踪开发任务
- 🗺️ 查看详细的开发路线图
- 💡 获取AI驱动的开发建议
- 📱 同步任务到iPhone日历和提醒
- 📊 生成进度报告

```bash
cd dev-assistant
python assistant.py
```

## 💻 技术栈

### 前端
- **框架**: Next.js 14+ (React)
- **样式**: Tailwind CSS + Shadcn/ui
- **状态管理**: Zustand
- **视频处理**: Video.js

### 后端
- **框架**: FastAPI (Python) 或 Express (Node.js)
- **数据库**: PostgreSQL + Redis
- **存储**: AWS S3 / MinIO
- **任务队列**: Celery / Bull

### AI集成
- **大语言模型**: OpenAI GPT-4 / Claude
- **图像生成**: Stable Diffusion / DALL-E 3
- **视频生成**: Runway ML / Pika Labs
- **音频生成**: ElevenLabs / AudioCraft

## 🎯 开发阶段

### MVP第一阶段 (2-3个月)
- ✅ 用户认证系统
- ✅ 项目管理
- ✅ 剧本编辑器
- ✅ AI剧本生成

### MVP第二阶段 (2-3个月)
- ⏳ AI视频生成
- ⏳ 基础视频剪辑
- ⏳ 时间轴编辑器

### MVP第三阶段 (3-4个月)
- ⏳ AI配音
- ⏳ 音效和音乐
- ⏳ 批量渲染系统

## 📊 项目进度

当前阶段: **规划与准备**
完成度: **5%**

查看详细进度：
```bash
cd dev-assistant
python assistant.py progress
```

## 🛠️ 开发环境要求

### 必需
- Node.js 18+
- Python 3.9+
- PostgreSQL 14+
- Git

### 推荐
- Docker Desktop
- VS Code
- Postman

## 📱 iPhone集成

将开发任务同步到iPhone日历和提醒事项：

### 方式1: iCloud CalDAV (推荐)
```bash
python assistant.py configure
# 选择"iCloud日历"并输入Apple ID
```

### 方式2: Apple快捷指令
创建快捷指令连接本地API，支持Siri语音控制

### 方式3: 导出.ics文件
```bash
python assistant.py export-ics
# AirDrop到iPhone导入
```

详细配置请查看 [iPhone集成指南](dev-assistant/IPHONE_INTEGRATION.md)

## 🤝 贡献指南

欢迎贡献！请查看：
1. [开发检查清单](DEV_CHECKLIST.md) - 代码规范和质量标准
2. [开发路线图](docs/ROADMAP.md) - 了解项目规划
3. 创建Issue或Pull Request

## 📝 许可证

MIT License

## 🔗 相关资源

- [Next.js文档](https://nextjs.org/docs)
- [FastAPI文档](https://fastapi.tiangolo.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Runway ML](https://runwayml.com/)

## 📧 联系方式

如有问题或建议，欢迎：
- 创建Issue
- 发送邮件

---

**开始你的AI电影创作之旅！ 🎬**