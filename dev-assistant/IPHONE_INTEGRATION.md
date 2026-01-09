# 📱 iPhone集成指南

## 概述

本指南详细说明如何将开发助手与iPhone日历和提醒同步，让你随时随地掌握开发进度。

## 🎯 集成方式对比

| 方式 | 难度 | 功能 | 推荐度 |
|------|------|------|--------|
| iCloud CalDAV | ⭐⭐ | 完整同步 | ⭐⭐⭐⭐⭐ |
| Apple快捷指令 | ⭐ | 灵活自定义 | ⭐⭐⭐⭐ |
| Zapier/IFTTT | ⭐ | 简单易用 | ⭐⭐⭐ |
| API + 手动导入 | ⭐ | 基础功能 | ⭐⭐ |

## 方案一：iCloud CalDAV同步（推荐）

### 优点
- ✅ 完全自动化，实时双向同步
- ✅ 原生支持，无需额外应用
- ✅ 支持日历和提醒事项
- ✅ 跨设备自动同步

### 配置步骤

#### 1. 生成Apple应用专用密码

1. 访问 [Apple ID账户页面](https://appleid.apple.com)
2. 登录你的Apple ID
3. 在"安全"部分找到"应用专用密码"
4. 点击"生成密码"
5. 输入标签名称（如："AI电影引擎助手"）
6. 复制生成的密码（格式：xxxx-xxxx-xxxx-xxxx）

#### 2. 配置开发助手

```bash
python assistant.py configure
```

选择"iCloud日历"选项，输入：
- Apple ID（邮箱地址）
- 应用专用密码（上一步生成的）

#### 3. 安装Python依赖

```bash
pip install caldav icalendar pytz
```

#### 4. 测试连接

```bash
python assistant.py sync
```

如果看到"✓ 同步完成"，说明配置成功！

### Python实现示例

```python
import caldav
from datetime import datetime
from icalendar import Calendar, Event

# 连接到iCloud
client = caldav.DAVClient(
    url="https://caldav.icloud.com",
    username="your_apple_id@icloud.com",
    password="xxxx-xxxx-xxxx-xxxx"
)

# 获取主日历
principal = client.principal()
calendars = principal.calendars()

# 创建或获取项目日历
project_calendar = None
for cal in calendars:
    if cal.name == "AI电影引擎开发":
        project_calendar = cal
        break

if not project_calendar:
    project_calendar = principal.make_calendar(name="AI电影引擎开发")

# 添加任务到日历
def add_task_to_calendar(task):
    cal = Calendar()
    event = Event()
    event.add('summary', task['title'])
    event.add('description', task.get('description', ''))
    event.add('dtstart', datetime.now())

    if task.get('due_date'):
        event.add('dtend', datetime.fromisoformat(task['due_date']))

    cal.add_component(event)
    project_calendar.save_event(cal.to_ical())
```

## 方案二：Apple快捷指令

### 优点
- ✅ 配置简单，无需密码
- ✅ 高度可自定义
- ✅ 支持Siri语音控制
- ✅ 可触发自动化

### 配置步骤

#### 1. 启动本地API服务器

```bash
cd dev-assistant
python api_server.py
```

这会在 `http://localhost:5000` 启动一个简单的API服务器。

#### 2. 创建快捷指令

在iPhone上打开"快捷指令"App：

##### 快捷指令1：查看今日任务

1. 点击"+"创建新快捷指令
2. 添加动作："获取URL内容"
   - URL: `http://YOUR_IP:5000/api/tasks/today`
   - 方法: GET
3. 添加动作："显示结果"
4. 命名为"今日开发任务"

##### 快捷指令2：添加任务

1. 创建新快捷指令
2. 添加动作："提问"
   - 提示: "输入任务名称"
3. 添加动作："获取URL内容"
   - URL: `http://YOUR_IP:5000/api/tasks`
   - 方法: POST
   - 请求体: JSON
   ```json
   {
     "title": "提问结果",
     "priority": "medium"
   }
   ```
4. 添加动作："显示通知"
   - 文本: "任务已添加"

##### 快捷指令3：同步到日历

1. 创建新快捷指令
2. 添加动作："获取URL内容"
   - URL: `http://YOUR_IP:5000/api/tasks/pending`
3. 添加动作："重复每一项"
4. 在重复中添加：
   - "添加新事件"
   - 日历: 选择你的日历
   - 标题: "重复项目.title"
   - 备注: "重复项目.description"

#### 3. 配置Siri快捷指令

在快捷指令详情页面：
1. 点击"添加到Siri"
2. 录制语音命令，例如：
   - "我的开发任务"
   - "添加开发任务"
   - "同步开发计划"

#### 4. 使用示例

```
"嘿Siri，我的开发任务"
→ 显示今天的任务列表

"嘿Siri，添加开发任务"
→ 提示输入任务名称，自动添加

"嘿Siri，同步开发计划"
→ 将所有待办任务同步到日历
```

### API服务器代码

创建文件 `dev-assistant/api_server.py`：

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# 加载任务数据
def load_tasks():
    try:
        with open('data/tasks.json', 'r') as f:
            return json.load(f)
    except:
        return []

@app.route('/api/tasks/today', methods=['GET'])
def get_today_tasks():
    tasks = load_tasks()
    today_tasks = [t for t in tasks if t['status'] != 'completed']
    return jsonify(today_tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    task = request.json
    tasks = load_tasks()
    task['id'] = len(tasks) + 1
    tasks.append(task)

    with open('data/tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)

    return jsonify({'success': True, 'task': task})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## 方案三：Zapier自动化

### 配置步骤

1. 注册 [Zapier账户](https://zapier.com)
2. 创建新Zap

#### Trigger（触发器）
- 选择"Webhooks by Zapier"
- 选择"Catch Hook"
- 复制Webhook URL

#### Action（动作）
- 选择"Apple Calendar"
- 选择"Create Event"
- 映射字段：
  - Calendar: 选择目标日历
  - Event Title: webhook.title
  - Start Date: webhook.due_date
  - Description: webhook.description

#### 配置助手
在 `config.yaml` 中：
```yaml
integrations:
  zapier:
    enabled: true
    webhook_url: "YOUR_ZAPIER_WEBHOOK_URL"
```

## 方案四：导出.ics文件手动导入

### 最简单的方式

```bash
# 导出任务为日历文件
python assistant.py export-ics

# 生成文件：tasks.ics
```

然后：
1. 发送 `tasks.ics` 到iPhone（邮件/AirDrop）
2. 在iPhone上打开文件
3. 选择导入到日历

### Python导出代码

```python
from icalendar import Calendar, Event, Todo
from datetime import datetime

def export_tasks_to_ics(tasks, filename='tasks.ics'):
    cal = Calendar()
    cal.add('prodid', '-//AI电影引擎开发助手///')
    cal.add('version', '2.0')

    for task in tasks:
        if task['status'] == 'completed':
            continue

        todo = Todo()
        todo.add('summary', task['title'])
        todo.add('description', task.get('description', ''))
        todo.add('priority', 5 if task.get('priority') == 'high' else 9)

        if task.get('due_date'):
            todo.add('due', datetime.fromisoformat(task['due_date']))

        cal.add_component(todo)

    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

    print(f"已导出到 {filename}")
```

## 🔔 iPhone提醒事项集成

### 使用Reminders API（需要Mac）

如果你有Mac，可以使用以下AppleScript同步提醒：

```applescript
tell application "Reminders"
    tell list "开发任务"
        make new reminder with properties {name:"实现用户认证", body:"预计16小时", due date:(current date) + 7 * days}
    end tell
end tell
```

通过Python调用：

```python
import subprocess

def add_reminder(title, body, due_days=7):
    script = f'''
    tell application "Reminders"
        tell list "开发任务"
            make new reminder with properties {{name:"{title}", body:"{body}", due date:(current date) + {due_days} * days}}
        end tell
    end tell
    '''
    subprocess.run(['osascript', '-e', script])
```

## 📊 同步策略建议

### 实时同步
适合：重度使用者
```yaml
sync_interval: 60  # 每分钟同步一次
```

### 定时同步
适合：大多数用户
```yaml
sync_interval: 300  # 每5分钟同步一次
```

### 手动同步
适合：偶尔查看
```bash
python assistant.py sync
```

## 🔒 安全建议

1. **不要提交密码到Git**
   ```bash
   echo "config.yaml" >> .gitignore
   ```

2. **使用环境变量**
   ```bash
   export APPLE_ID="your_email@icloud.com"
   export APPLE_APP_PASSWORD="xxxx-xxxx-xxxx-xxxx"
   ```

3. **定期更换应用专用密码**

4. **仅在可信网络使用**

## 🎯 最佳实践

### 日历组织
- **日历1**: "开发任务" - 实际编码任务
- **日历2**: "会议和截止日期" - 重要里程碑
- **日历3**: "学习计划" - 学习新技术的时间

### 提醒设置
- 高优先级任务：提前1天提醒
- 中优先级任务：提前3天提醒
- 截止日期：提前7天、3天、1天各提醒一次

### 命名规范
```
[MVP1] 实现用户认证 - 16h
[MVP2] AI视频生成集成 - 32h
[BUG] 修复登录问题 - 2h
[DOCS] 编写API文档 - 4h
```

## 🆘 故障排除

### 问题1：无法连接到iCloud
```
错误: Unauthorized

解决：
1. 确认使用应用专用密码，不是Apple ID密码
2. 检查网络连接
3. 验证Apple ID拼写正确
```

### 问题2：快捷指令无法访问API
```
错误: 无法连接到服务器

解决：
1. 确保API服务器正在运行
2. iPhone和电脑在同一WiFi
3. 检查防火墙设置
4. 使用电脑的局域网IP，不是localhost
```

### 问题3：任务重复同步
```
解决：
1. 检查任务是否有唯一ID
2. 清除日历，重新同步
3. 调整sync_interval避免太频繁
```

## 📱 推荐工作流

### 早晨（9:00）
1. Siri: "我的开发任务"
2. 查看今日任务
3. 规划优先级

### 开发中
1. 完成任务后在助手中标记
2. 自动同步到iPhone
3. 日历自动更新

### 晚上（18:00）
1. 查看进度报告
2. 规划明天任务
3. 同步到iPhone日历

### 每周回顾
1. 生成周报
2. 调整下周计划
3. 同步里程碑到日历

---

**下一步**: 选择一个集成方案开始配置！

推荐：先尝试方案四（导出.ics），熟悉后升级到方案二（快捷指令）或方案一（CalDAV）。
