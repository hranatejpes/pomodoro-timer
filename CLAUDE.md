# Claude Development Context

This document provides context for Claude Code about this pomodoro timer project.

## Project Overview

This is a console-based Pomodoro timer application written in Python 3. The application helps users manage their work and break sessions using the Pomodoro technique.

## Architecture

### Main Components

- `PomodoroTimer` class: Core timer functionality and argument parsing
- Cross-platform notification system
- ANSI color support for terminal output
- Command-line argument parsing for flexible usage

### Key Features Implemented

1. **Timer Modes**:
   - Work sessions (default: 60 minutes, red color)
   - Break sessions (default: 10 minutes, green color)

2. **Usage Patterns**:
   - Single session mode (`pomo work` or `pomo break`)
   - Infinite cycle mode (`pomo`)
   - Custom duration cycles (`pomo work 30 break 5`)

3. **Operation Modes**:
   - Manual mode (default): User presses Enter to continue
   - Automatic mode: Sessions switch automatically after completion

4. **User Interface**:
   - Color-coded output (red for work, green for break)
   - Console clearing between sessions for clean interface
   - Real-time countdown display
   - Cross-platform notifications

## Code Structure

### Color System
- Uses ANSI escape codes for terminal colors
- Red + Bold for work mode
- Green + Bold for break mode
- Proper color reset after each colored text

### Notification System
- macOS: `osascript` for native notifications
- Linux: `notify-send` command
- Windows: PowerShell message boxes
- Fallback: Console output

### Argument Parsing
- Custom argument parsing (not using argparse for main logic)
- Supports various command patterns
- Handles `auto` parameter anywhere in arguments

## Development Notes

### Recent Changes
1. Added ANSI color support for better visual distinction
2. Implemented console clearing between sessions
3. Enhanced notification messages
4. Improved argument parsing flexibility

### Technical Decisions
- Used `os.system()` for cross-platform console clearing
- Implemented custom color methods for consistent styling
- Chose manual argument parsing for flexibility with parameter order

### Dependencies
- Standard library only (no external dependencies)
- Cross-platform compatibility maintained

## Usage Examples for Development

When testing or extending this application:

```bash
# Test basic functionality
python3 pomo.py work 1 break 1

# Test automatic mode
python3 pomo.py work 1 break 1 auto

# Test single sessions
python3 pomo.py work
python3 pomo.py break
```

## Future Enhancement Ideas

- Configuration file support
- Sound notifications
- Session statistics tracking
- Multiple timer presets
- Integration with productivity apps

## Maintenance Notes

- Keep cross-platform compatibility in mind
- Test notifications on different operating systems
- Ensure ANSI colors work across different terminals
- Maintain backward compatibility with existing usage patterns