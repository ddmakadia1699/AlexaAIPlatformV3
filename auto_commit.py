#!/usr/bin/env python3
"""
Simple Auto-Commit Script for GitHub
Makes daily commits with realistic messages
"""

import os
import random
import subprocess
import schedule
import time
from datetime import datetime

class SimpleAutoCommit:
    def __init__(self):
        # Realistic commit messages that look professional
        self.commit_messages = [
            "feat: implement new functionality",
            "fix: resolve bug in core logic", 
            "docs: update documentation",
            "refactor: improve code structure",
            "style: fix formatting issues",
            "test: add unit tests",
            "chore: update dependencies",
            "perf: optimize performance",
            "security: enhance validation",
            "ci: update build pipeline",
            "feat: add error handling",
            "fix: memory leak issue",
            "docs: add code comments",
            "refactor: clean up utilities",
            "style: improve readability"
        ]
    
    def create_dummy_files(self):
        """Create some files to track changes"""
        os.makedirs("src", exist_ok=True)
        
        # Create a simple Python file
        with open("src/main.py", "w") as f:
            f.write('''#!/usr/bin/env python3
"""Main application file"""

def main():
    print("Hello, World!")
    return True

if __name__ == "__main__":
    main()
''')
        
        # Create a README
        with open("README.md", "w") as f:
            f.write('''# My Project

A simple project with auto-commits.

## Features
- Automated daily commits
- Clean code structure
- Easy to maintain

## Usage
```bash
python src/main.py
```
''')

    def make_small_change(self):
        """Make a small realistic change to the codebase"""
        changes = [
            self._add_comment,
            self._update_readme,
            self._add_function,
            self._update_timestamp
        ]
        
        # Pick a random change to make
        random.choice(changes)()
    
    def _add_comment(self):
        """Add a comment to the main file"""
        comments = [
            "# TODO: Add error handling",
            "# FIXME: Optimize this function", 
            "# NOTE: Consider refactoring",
            "# Enhanced for better performance",
            "# Added validation logic"
        ]
        
        with open("src/main.py", "a") as f:
            f.write(f"\n{random.choice(comments)}\n")
    
    def _update_readme(self):
        """Update README with timestamp"""
        with open("README.md", "a") as f:
            f.write(f"\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    def _add_function(self):
        """Add a simple function"""
        functions = [
            '\ndef get_version():\n    """Return version number"""\n    return "1.0.0"\n',
            '\ndef validate_input(data):\n    """Validate input data"""\n    return data is not None\n',
            '\ndef format_output(result):\n    """Format output data"""\n    return str(result)\n'
        ]
        
        with open("src/main.py", "a") as f:
            f.write(random.choice(functions))
    
    def _update_timestamp(self):
        """Add timestamp to show activity"""
        with open("activity.log", "a") as f:
            f.write(f"Activity: {datetime.now().isoformat()}\n")

    def commit_and_push(self):
        """Make a commit and push to GitHub"""
        try:
            # Initialize git if needed
            if not os.path.exists('.git'):
                subprocess.run(['git', 'init'], check=True)
                subprocess.run(['git', 'branch', '-M', 'main'], check=True)
                print("📁 Initialized Git repository")
            
            # Make a small change
            self.make_small_change()
            
            # Add all changes
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Check if there are changes
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            
            if result.stdout.strip():
                # Get random commit message
                commit_msg = random.choice(self.commit_messages)
                
                # Commit
                subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
                
                # Try to push (will fail if remote not set up)
                try:
                    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
                    print(f"✅ Successfully pushed: {commit_msg}")
                except subprocess.CalledProcessError:
                    print(f"📝 Committed locally: {commit_msg}")
                    print("💡 To push to GitHub, run: git remote add origin <your-repo-url>")
            else:
                print("ℹ️  No changes to commit")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

    def generate_dynamic_schedule(self):
        """Generate completely random weekly schedule"""
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        dynamic_schedule = {}
        
        for day in days:
            # Generate random range for each day
            # Min commits: 1-3, Max commits: 4-12
            min_commits = random.randint(1, 3)
            max_commits = random.randint(min_commits + 2, 12)
            
            dynamic_schedule[day] = {
                'min': min_commits, 
                'max': max_commits,
                'actual': random.randint(min_commits, max_commits)
            }
        
        return dynamic_schedule

    def schedule_daily_commits(self):
        """Schedule completely dynamic weekly commit pattern"""
        print("🤖 Generating dynamic weekly schedule...")
        
        # Generate random schedule for this week
        weekly_schedule = self.generate_dynamic_schedule()
        
        print("🎲 This week's random schedule:")
        
        for day, schedule_info in weekly_schedule.items():
            commits_today = schedule_info['actual']
            min_range = schedule_info['min']
            max_range = schedule_info['max']
            
            # Schedule commits at random times between 9 AM - 6 PM
            for i in range(commits_today):
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                time_str = f"{hour:02d}:{minute:02d}"
                
                # Schedule for this specific day
                getattr(schedule.every(), day).at(time_str).do(self.commit_and_push)
            
            print(f"📅 {day.capitalize()}: {commits_today} commits (range was {min_range}-{max_range})")
        
        print("\n🎯 Totally Dynamic Schedule!")
        print("✨ Every week gets completely new random ranges")
        print("📊 Each day: 1-12 possible commits")
        print("🕘 All commits between 9 AM - 6 PM")
        print("🔄 Refreshes every Sunday with new random ranges")
        print("\nPress Ctrl+C to stop")
        
        # Schedule weekly refresh to change commit counts
        schedule.every().sunday.at("23:59").do(self.refresh_weekly_schedule)
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def refresh_weekly_schedule(self):
        """Refresh the weekly schedule with completely new random ranges"""
        print("🔄 Generating brand new dynamic schedule...")
        
        # Clear all existing schedules and rebuild
        schedule.clear()
        
        # Re-add the weekly refresh job
        schedule.every().sunday.at("23:59").do(self.refresh_weekly_schedule)
        
        # Generate completely new random schedule
        weekly_schedule = self.generate_dynamic_schedule()
        
        print("🎲 New week's completely random schedule:")
        
        for day, schedule_info in weekly_schedule.items():
            commits_today = schedule_info['actual']
            min_range = schedule_info['min']
            max_range = schedule_info['max']
            
            for i in range(commits_today):
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                time_str = f"{hour:02d}:{minute:02d}"
                getattr(schedule.every(), day).at(time_str).do(self.commit_and_push)
            
            print(f"📅 {day.capitalize()}: {commits_today} commits (new range: {min_range}-{max_range})")
        
        print("✅ Totally new dynamic schedule generated!")

    def run_once(self):
        """Make one commit right now"""
        print("🚀 Making a commit...")
        self.commit_and_push()

    def run_multiple(self):
        """Make multiple commits with user-specified count"""
        try:
            count = int(input("How many commits do you want to make? (1-50): ").strip())
            
            if count < 1 or count > 50:
                print("❌ Please enter a number between 1 and 50")
                return
            
            print(f"🚀 Making {count} commits...")
            
            for i in range(count):
                print(f"📝 Commit {i+1}/{count}")
                self.commit_and_push()
                
                # Add small delay between commits (1-5 seconds) to look realistic
                if i < count - 1:  # Don't delay after last commit
                    delay = random.randint(1, 5)
                    print(f"⏳ Waiting {delay} seconds...")
                    time.sleep(delay)
            
            print(f"✅ Successfully made {count} commits!")
            
        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n⚠️ Process interrupted by user")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    auto_commit = SimpleAutoCommit()
    
    # Create initial files if they don't exist
    auto_commit.create_dummy_files()
    
    print("🎯 Simple Auto-Commit for GitHub")
    print("\nChoose an option:")
    print("1. Make one commit now")
    print("2. Make multiple commits (you choose how many)")
    print("3. Schedule totally dynamic weekly auto-commits")
    print("4. Just setup files and exit")
    
    try:
        choice = input("\nEnter choice (1, 2, 3, or 4): ").strip()
        
        if choice == "1":
            auto_commit.run_once()
        elif choice == "2":
            auto_commit.run_multiple()
        elif choice == "3":
            auto_commit.schedule_daily_commits()
        elif choice == "4":
            print("✅ Files created! You can now:")
            print("   git remote add origin <your-github-repo-url>")
            print("   python auto_commit.py")
        else:
            print("Invalid choice. Making one commit...")
            auto_commit.run_once()
            
    except KeyboardInterrupt:
        print("\n👋 Auto-commit stopped!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 