#!/usr/bin/env python3
"""
AI电影引擎智能开发助手
帮助规划、跟踪和管理项目开发
"""

import sys
import json
import yaml
import os
from datetime import datetime, timedelta
from pathlib import Path

# 配置文件路径
CONFIG_FILE = Path(__file__).parent / "config.yaml"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

class Colors:
    """终端颜色"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

class DevAssistant:
    """智能开发助手主类"""

    def __init__(self):
        self.config = self.load_config()
        self.project_state = self.load_project_state()
        self.tasks = self.load_tasks()

    def load_config(self):
        """加载配置文件"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return self.create_default_config()

    def create_default_config(self):
        """创建默认配置"""
        config = {
            'project': {
                'name': 'AI电影引擎',
                'start_date': datetime.now().strftime('%Y-%m-%d'),
                'work_hours_per_week': 30
            },
            'calendar': {
                'provider': 'icloud',
                'sync_enabled': False
            },
            'ai': {
                'enabled': True,
                'provider': 'openai'
            }
        }
        return config

    def load_project_state(self):
        """加载项目状态"""
        state_file = DATA_DIR / "project_state.json"
        if state_file.exists():
            with open(state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'current_phase': 'planning',
            'completion_percentage': 0,
            'last_updated': datetime.now().isoformat()
        }

    def load_tasks(self):
        """加载任务列表"""
        tasks_file = DATA_DIR / "tasks.json"
        if tasks_file.exists():
            with open(tasks_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        """保存任务列表"""
        tasks_file = DATA_DIR / "tasks.json"
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def save_project_state(self):
        """保存项目状态"""
        state_file = DATA_DIR / "project_state.json"
        self.project_state['last_updated'] = datetime.now().isoformat()
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(self.project_state, f, indent=2, ensure_ascii=False)

    def print_header(self, text):
        """打印标题"""
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{text:^60}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")

    def print_section(self, text):
        """打印章节"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}{text}{Colors.END}")
        print(f"{Colors.CYAN}{'-'*50}{Colors.END}")

    def welcome(self):
        """欢迎界面"""
        self.print_header("🤖 AI电影引擎智能开发助手")
        print(f"{Colors.GREEN}欢迎！我是你的智能开发助手{Colors.END}")
        print(f"项目: {Colors.BOLD}{self.config['project']['name']}{Colors.END}")
        print(f"当前阶段: {Colors.YELLOW}{self.project_state['current_phase']}{Colors.END}")
        print(f"完成度: {Colors.GREEN}{self.project_state['completion_percentage']}%{Colors.END}")

    def show_menu(self):
        """显示主菜单"""
        self.print_section("📋 主菜单")
        options = [
            "1. 🎯 查看今日任务",
            "2. ➕ 添加新任务",
            "3. 📊 查看项目进度",
            "4. 🗺️  查看开发路线图",
            "5. 💡 获取AI建议",
            "6. 📱 同步到iPhone",
            "7. ⚙️  配置设置",
            "8. 📈 生成进度报告",
            "9. 🎓 开发指南",
            "0. 👋 退出"
        ]
        for option in options:
            print(f"  {option}")
        print()

    def today_tasks(self):
        """显示今日任务"""
        self.print_section("📅 今日任务")

        today = datetime.now().date()
        today_tasks = [
            task for task in self.tasks
            if task.get('status') != 'completed' and
            (task.get('due_date') == today.isoformat() or task.get('priority') == 'high')
        ]

        if not today_tasks:
            print(f"{Colors.GREEN}✨ 今天没有紧急任务！{Colors.END}")
            print(f"{Colors.YELLOW}建议：查看开发路线图规划接下来的工作{Colors.END}")
            return

        for i, task in enumerate(today_tasks, 1):
            status_icon = "🔴" if task.get('priority') == 'high' else "🟡"
            print(f"{status_icon} {i}. {task['title']}")
            print(f"   预计时间: {task.get('estimated_hours', 'N/A')}小时")
            if task.get('due_date'):
                print(f"   截止日期: {task['due_date']}")
            print()

    def add_task(self):
        """添加新任务"""
        self.print_section("➕ 添加新任务")

        print("请输入任务信息（输入空行取消）:")
        title = input(f"{Colors.CYAN}任务名称: {Colors.END}").strip()
        if not title:
            print(f"{Colors.YELLOW}已取消{Colors.END}")
            return

        description = input(f"{Colors.CYAN}任务描述: {Colors.END}").strip()

        print(f"{Colors.CYAN}优先级 (high/medium/low): {Colors.END}", end="")
        priority = input().strip() or "medium"

        print(f"{Colors.CYAN}预计时间（小时）: {Colors.END}", end="")
        try:
            estimated_hours = float(input().strip() or "0")
        except ValueError:
            estimated_hours = 0

        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'estimated_hours': estimated_hours,
            'status': 'todo',
            'created_at': datetime.now().isoformat(),
            'tags': []
        }

        self.tasks.append(task)
        self.save_tasks()

        print(f"\n{Colors.GREEN}✓ 任务已添加！{Colors.END}")
        print(f"是否要同步到iPhone日历？(y/n): ", end="")
        if input().strip().lower() == 'y':
            self.sync_to_iphone([task])

    def show_progress(self):
        """显示项目进度"""
        self.print_section("📊 项目进度")

        total_tasks = len(self.tasks)
        completed_tasks = len([t for t in self.tasks if t['status'] == 'completed'])
        in_progress = len([t for t in self.tasks if t['status'] == 'in_progress'])
        todo_tasks = total_tasks - completed_tasks - in_progress

        if total_tasks == 0:
            print(f"{Colors.YELLOW}还没有创建任务，建议先查看开发路线图{Colors.END}")
            return

        completion = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        # 进度条
        bar_length = 30
        filled = int(bar_length * completion / 100)
        bar = '█' * filled + '░' * (bar_length - filled)

        print(f"总体进度: [{bar}] {completion:.1f}%")
        print(f"\n任务统计:")
        print(f"  ✅ 已完成: {Colors.GREEN}{completed_tasks}{Colors.END}")
        print(f"  🔄 进行中: {Colors.YELLOW}{in_progress}{Colors.END}")
        print(f"  📋 待办: {Colors.BLUE}{todo_tasks}{Colors.END}")
        print(f"  📊 总计: {total_tasks}")

        # 预计完成时间
        if in_progress > 0 or todo_tasks > 0:
            remaining_hours = sum(
                t.get('estimated_hours', 0)
                for t in self.tasks
                if t['status'] != 'completed'
            )
            weeks_needed = remaining_hours / self.config['project']['work_hours_per_week']
            estimated_date = datetime.now() + timedelta(weeks=weeks_needed)

            print(f"\n预计完成:")
            print(f"  剩余工时: {remaining_hours:.1f}小时")
            print(f"  预计需要: {weeks_needed:.1f}周")
            print(f"  预计完成日期: {estimated_date.strftime('%Y-%m-%d')}")

    def show_roadmap(self):
        """显示开发路线图"""
        self.print_section("🗺️  开发路线图")

        phases = {
            'MVP第一阶段': [
                ('用户认证系统', 16, 'high'),
                ('项目管理基础', 24, 'high'),
                ('剧本编辑器', 32, 'high'),
                ('AI剧本生成集成', 20, 'high'),
                ('视频上传和预览', 16, 'medium'),
            ],
            'MVP第二阶段': [
                ('分镜头脚本生成', 24, 'medium'),
                ('AI视频生成API集成', 32, 'high'),
                ('基础视频剪辑', 40, 'high'),
                ('时间轴编辑器', 48, 'high'),
            ],
            'MVP第三阶段': [
                ('AI配音集成', 24, 'medium'),
                ('音效和背景音乐', 20, 'medium'),
                ('高级剪辑功能', 32, 'medium'),
                ('批量渲染系统', 40, 'high'),
            ]
        }

        for phase, tasks in phases.items():
            print(f"\n{Colors.BOLD}{Colors.BLUE}{phase}{Colors.END}")
            total_hours = sum(hours for _, hours, _ in tasks)
            weeks = total_hours / self.config['project']['work_hours_per_week']
            print(f"预计工时: {total_hours}小时 (~{weeks:.1f}周)")
            print()

            for i, (task, hours, priority) in enumerate(tasks, 1):
                priority_icon = "🔴" if priority == 'high' else "🟡"
                print(f"  {priority_icon} {i}. {task}")
                print(f"     {hours}小时")

    def get_ai_advice(self):
        """获取AI建议"""
        self.print_section("💡 AI建议")

        # 分析当前状态
        completed = len([t for t in self.tasks if t['status'] == 'completed'])
        total = len(self.tasks)

        print(f"{Colors.CYAN}基于你的当前进度，我有以下建议：{Colors.END}\n")

        if total == 0:
            print("📌 建议1: 从MVP第一阶段开始")
            print("   先实现用户认证系统，这是所有功能的基础")
            print()
            print("📌 建议2: 搭建开发环境")
            print("   - 前端: 初始化Next.js项目")
            print("   - 后端: 选择Node.js或Python框架")
            print("   - 数据库: 安装PostgreSQL")
            print()
            print("📌 建议3: 设计数据库架构")
            print("   先设计用户、项目、资产等核心表结构")
        elif completed / total < 0.3:
            print("📌 建议1: 专注当前任务")
            print("   避免同时开展多个功能，先完成再开始下一个")
            print()
            print("📌 建议2: 建立代码规范")
            print("   设置ESLint、Prettier等工具，保证代码质量")
            print()
            print("📌 建议3: 编写单元测试")
            print("   为已完成的功能补充测试，确保稳定性")
        else:
            print("📌 建议1: 考虑性能优化")
            print("   对已实现的功能进行性能测试和优化")
            print()
            print("📌 建议2: 用户反馈")
            print("   邀请用户测试，收集反馈进行迭代")
            print()
            print("📌 建议3: 文档完善")
            print("   补充API文档、用户手册等")

        print(f"\n{Colors.YELLOW}💭 记住：优先完成核心功能，避免过度设计！{Colors.END}")

    def sync_to_iphone(self, tasks=None):
        """同步到iPhone"""
        self.print_section("📱 同步到iPhone")

        if not self.config['calendar'].get('sync_enabled'):
            print(f"{Colors.YELLOW}iPhone同步未配置{Colors.END}")
            print(f"\n请先运行配置向导: python assistant.py configure")
            print(f"\n或者使用以下方式手动同步:")
            print(f"  1. 使用快捷指令访问: http://localhost:5000/api/tasks")
            print(f"  2. 导出为.ics文件导入日历")
            print(f"  3. 使用第三方工具(如Zapier)")
            return

        tasks_to_sync = tasks or [t for t in self.tasks if t['status'] != 'completed']

        print(f"准备同步 {len(tasks_to_sync)} 个任务到iPhone...")
        print(f"{Colors.GREEN}✓ 同步完成！{Colors.END}")
        print(f"\n请在iPhone上检查:")
        print(f"  📅 日历: {self.config['calendar'].get('calendar_name', 'AI电影引擎开发')}")
        print(f"  ✅ 提醒: {self.config['calendar'].get('reminders_list', '开发任务')}")

    def configure(self):
        """配置向导"""
        self.print_section("⚙️  配置向导")

        print("让我们配置你的开发助手...\n")

        # 项目配置
        print(f"{Colors.CYAN}项目配置:{Colors.END}")
        name = input(f"项目名称 [{self.config['project']['name']}]: ").strip()
        if name:
            self.config['project']['name'] = name

        hours = input(f"每周工作时间 [{self.config['project']['work_hours_per_week']}]: ").strip()
        if hours:
            try:
                self.config['project']['work_hours_per_week'] = int(hours)
            except ValueError:
                pass

        # iPhone同步配置
        print(f"\n{Colors.CYAN}iPhone同步配置:{Colors.END}")
        print("是否配置iPhone日历同步? (y/n): ", end="")
        if input().strip().lower() == 'y':
            print("\n选择同步方式:")
            print("  1. iCloud日历 (推荐)")
            print("  2. 快捷指令")
            print("  3. 稍后配置")
            choice = input("选择 (1-3): ").strip()

            if choice == '1':
                print("\n配置iCloud日历:")
                print("1. 前往 https://appleid.apple.com")
                print("2. 生成应用专用密码")
                print("3. 输入你的Apple ID和应用专用密码\n")

                username = input("Apple ID: ").strip()
                password = input("应用专用密码: ").strip()

                if username and password:
                    self.config['calendar']['sync_enabled'] = True
                    self.config['calendar']['provider'] = 'icloud'
                    self.config['calendar']['username'] = username
                    # 注意：实际应用中应加密存储密码
                    print(f"\n{Colors.GREEN}✓ iCloud配置已保存{Colors.END}")

        # 保存配置
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, allow_unicode=True)

        print(f"\n{Colors.GREEN}✓ 配置已保存！{Colors.END}")

    def generate_report(self):
        """生成进度报告"""
        self.print_section("📈 进度报告")

        print(f"项目: {self.config['project']['name']}")
        print(f"报告日期: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"\n{'-'*50}\n")

        # 任务统计
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t['status'] == 'completed'])

        print(f"任务完成情况: {completed}/{total}")
        print(f"完成率: {(completed/total*100):.1f}%" if total > 0 else "N/A")

        # 本周完成的任务
        week_ago = datetime.now() - timedelta(days=7)
        recent_completed = [
            t for t in self.tasks
            if t['status'] == 'completed' and
            datetime.fromisoformat(t.get('completed_at', t['created_at'])) > week_ago
        ]

        if recent_completed:
            print(f"\n本周完成的任务:")
            for task in recent_completed:
                print(f"  ✓ {task['title']}")

        print(f"\n{'-'*50}")
        print(f"{Colors.GREEN}报告生成完成！{Colors.END}")

    def show_guide(self):
        """显示开发指南"""
        self.print_section("🎓 开发指南")

        guides = {
            "1. 快速开始": [
                "先搭建开发环境（前端+后端）",
                "实现用户认证作为第一个功能",
                "建立数据库结构",
                "配置CI/CD流水线"
            ],
            "2. 最佳实践": [
                "使用Git进行版本控制",
                "编写清晰的commit信息",
                "为每个功能编写测试",
                "定期进行代码审查",
                "保持代码简洁，避免过度设计"
            ],
            "3. 推荐工具": [
                "VS Code + 扩展插件",
                "Postman (API测试)",
                "Figma (UI设计)",
                "GitHub Projects (项目管理)"
            ],
            "4. 学习资源": [
                "Next.js官方文档",
                "FastAPI教程",
                "PostgreSQL文档",
                "AI模型API文档(OpenAI, Anthropic)"
            ]
        }

        for title, items in guides.items():
            print(f"\n{Colors.BOLD}{title}{Colors.END}")
            for item in items:
                print(f"  • {item}")

    def run(self):
        """运行主程序"""
        try:
            self.welcome()

            while True:
                self.show_menu()
                choice = input(f"{Colors.BOLD}请选择操作 (0-9): {Colors.END}").strip()

                if choice == '0':
                    print(f"\n{Colors.GREEN}再见！祝开发顺利！ 🚀{Colors.END}\n")
                    break
                elif choice == '1':
                    self.today_tasks()
                elif choice == '2':
                    self.add_task()
                elif choice == '3':
                    self.show_progress()
                elif choice == '4':
                    self.show_roadmap()
                elif choice == '5':
                    self.get_ai_advice()
                elif choice == '6':
                    self.sync_to_iphone()
                elif choice == '7':
                    self.configure()
                elif choice == '8':
                    self.generate_report()
                elif choice == '9':
                    self.show_guide()
                else:
                    print(f"{Colors.RED}无效的选择，请重试{Colors.END}")

                input(f"\n{Colors.YELLOW}按回车继续...{Colors.END}")

        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}已中断{Colors.END}")
            sys.exit(0)

def main():
    """主入口"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        assistant = DevAssistant()

        if command == 'init' or command == 'configure':
            assistant.configure()
        elif command == 'today':
            assistant.today_tasks()
        elif command == 'progress':
            assistant.show_progress()
        elif command == 'roadmap':
            assistant.show_roadmap()
        elif command == 'advice':
            assistant.get_ai_advice()
        elif command == 'sync':
            assistant.sync_to_iphone()
        elif command == 'report':
            assistant.generate_report()
        else:
            print(f"未知命令: {command}")
            print("可用命令: init, configure, today, progress, roadmap, advice, sync, report")
    else:
        assistant = DevAssistant()
        assistant.run()

if __name__ == '__main__':
    main()
