#!/usr/bin/env python3
import sys
import time
import argparse
import subprocess
import platform
import os

class PomodoroTimer:
    def __init__(self):
        self.work_duration = 60  # 1 hour default
        self.break_duration = 10  # 10 minutes default
        self.auto_mode = False
        
        # Color codes
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.BLUE = '\033[94m'
        self.YELLOW = '\033[93m'
        self.BOLD = '\033[1m'
        self.END = '\033[0m'
        
    def parse_arguments(self):
        if len(sys.argv) == 1:
            return self.run_infinite_cycle()
            
        parser = argparse.ArgumentParser(description='Pomodoro Timer', add_help=False)
        
        # Check for auto mode
        if 'auto' in sys.argv:
            self.auto_mode = True
            sys.argv.remove('auto')
        
        args = sys.argv[1:]
        
        if len(args) == 1:
            if args[0] == 'work':
                return self.run_timer('work', self.work_duration)
            elif args[0] == 'break':
                return self.run_timer('break', self.break_duration)
        
        # Parse custom durations: pomo work 30 break 5
        if len(args) >= 4 and args[0] == 'work' and args[2] == 'break':
            try:
                work_mins = int(args[1])
                break_mins = int(args[3])
                self.work_duration = work_mins
                self.break_duration = break_mins
                return self.run_cycle_with_durations(work_mins, break_mins)
            except ValueError:
                print("Invalid duration values. Please use integers.")
                sys.exit(1)
        
        print("Usage:")
        print("  pomo                    - Run infinite work/break cycle")
        print("  pomo work               - Start work timer (default duration)")
        print("  pomo break              - Start break timer (default duration)")
        print("  pomo work 30 break 5    - Set custom durations and run cycle")
        print("  Add 'auto' anywhere for automatic mode switching")
        sys.exit(1)
    
    def send_notification(self, title, message):
        system = platform.system()
        try:
            if system == "Darwin":  # macOS
                subprocess.run([
                    'osascript', '-e', 
                    f'display notification "{message}" with title "{title}"'
                ])
            elif system == "Linux":
                subprocess.run(['notify-send', title, message])
            elif system == "Windows":
                subprocess.run([
                    'powershell', '-Command',
                    f'[System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms"); '
                    f'[System.Windows.Forms.MessageBox]::Show("{message}", "{title}")'
                ])
        except:
            print(f"\n🔔 {title}: {message}")
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_mode_color(self, mode):
        if mode == 'work':
            return self.RED + self.BOLD
        else:
            return self.GREEN + self.BOLD
    
    def countdown_timer(self, minutes, mode):
        total_seconds = minutes * 60
        color = self.get_mode_color(mode)
        
        print(f"\n🍅 {color}{mode.upper()}{self.END} timer started: {minutes} minutes")
        print("Press Ctrl+C to stop\n")
        
        try:
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                timer = f"{mins:02d}:{secs:02d}"
                color = self.get_mode_color(mode)
                print(f"\r⏰ {color}{timer}{self.END} remaining", end="", flush=True)
                time.sleep(1)
                total_seconds -= 1
            
            color = self.get_mode_color(mode)
            print(f"\n\n✅ {color}{mode.upper()}{self.END} session completed!")
            
            if mode == 'work':
                self.send_notification("Pomodoro Timer", "Work session complete! Time for a break.")
            else:
                self.send_notification("Pomodoro Timer", "Break complete! Time to get back to work.")
                
        except KeyboardInterrupt:
            color = self.get_mode_color(mode)
            print(f"\n\n⏹️  {color}{mode.upper()}{self.END} timer stopped.")
            sys.exit(0)
    
    def run_timer(self, mode, duration):
        self.countdown_timer(duration, mode)
    
    def run_cycle_with_durations(self, work_mins, break_mins):
        current_mode = 'work'
        
        while True:
            if current_mode == 'work':
                self.countdown_timer(work_mins, 'work')
                current_mode = 'break'
            else:
                self.countdown_timer(break_mins, 'break')
                current_mode = 'work'
            
            if not self.auto_mode:
                next_color = self.get_mode_color(current_mode)
                input(f"\nPress Enter to start {next_color}{current_mode.upper()}{self.END} session...")
                self.clear_screen()
            else:
                next_color = self.get_mode_color(current_mode)
                print(f"\nStarting {next_color}{current_mode.upper()}{self.END} session in 3 seconds...")
                time.sleep(3)
                self.clear_screen()
    
    def run_infinite_cycle(self):
        current_mode = 'work'
        
        while True:
            if current_mode == 'work':
                self.countdown_timer(self.work_duration, 'work')
                current_mode = 'break'
            else:
                self.countdown_timer(self.break_duration, 'break')
                current_mode = 'work'
            
            if not self.auto_mode:
                next_color = self.get_mode_color(current_mode)
                input(f"\nPress Enter to start {next_color}{current_mode.upper()}{self.END} session...")
                self.clear_screen()
            else:
                next_color = self.get_mode_color(current_mode)
                print(f"\nStarting {next_color}{current_mode.upper()}{self.END} session in 3 seconds...")
                time.sleep(3)
                self.clear_screen()

def main():
    timer = PomodoroTimer()
    timer.parse_arguments()

if __name__ == "__main__":
    main()