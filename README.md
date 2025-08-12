# Pomodoro Timer

A simple yet feature-rich console-based Pomodoro timer application written in Python 3.

## Features

- **Two timer modes**: Work and Break sessions with distinct color coding
- **Flexible usage**: Run single sessions or continuous cycles
- **Customizable durations**: Set your own work and break intervals
- **Visual feedback**: Color-coded modes (red for work, green for break)
- **Cross-platform notifications**: Native notifications on macOS, Linux, and Windows
- **Clean interface**: Console clearing between sessions for better focus
- **Manual or automatic mode**: Choose between manual control or automatic session switching

## Installation

1. Clone this repository:
```bash
git clone git@github.com:hranatejpes/pomodoro-timer.git
cd pomodoro-timer
```

2. Make sure you have Python 3 installed:
```bash
python3 --version
```

3. Make the script executable (optional):
```bash
chmod +x pomo.py
```

## Usage

### Basic Commands

```bash
# Run infinite work/break cycle (60min work, 10min break)
python3 pomo.py

# Start single work session (60 minutes)
python3 pomo.py work

# Start single break session (10 minutes)
python3 pomo.py break
```

### Custom Durations

```bash
# Set custom durations and run cycle (30min work, 5min break)
python3 pomo.py work 30 break 5
```

### Automatic Mode

Add `auto` anywhere in your command for automatic mode switching:

```bash
# Automatic infinite cycle
python3 pomo.py auto

# Automatic cycle with custom durations
python3 pomo.py work 25 break 5 auto
```

### Examples

```bash
# Pomodoro technique (25min work, 5min break, automatic)
python3 pomo.py work 25 break 5 auto

# Extended work session (90min work, 15min break, manual)
python3 pomo.py work 90 break 15

# Quick break reminder
python3 pomo.py break 2
```

## Default Settings

- **Work session**: 60 minutes
- **Break session**: 10 minutes
- **Mode**: Manual (press Enter to continue)
- **Colors**: Red for work mode, Green for break mode

## Controls

- **Ctrl+C**: Stop the current timer
- **Enter**: Start next session (in manual mode)

## System Requirements

- Python 3.x
- Cross-platform support (macOS, Linux, Windows)

## Notifications

The app sends native notifications when sessions complete:
- **macOS**: Uses `osascript` for native notifications
- **Linux**: Uses `notify-send`
- **Windows**: Uses PowerShell for message boxes
- **Fallback**: Console notifications if system notifications fail

## License

This project is open source and available under the MIT License.