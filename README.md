# Simple Python Keylogger

A lightweight keylogger application built with Python that records keyboard inputs to text files.

## Description

This keylogger uses the `pynput` library to capture keyboard input events and logs them to text files with timestamps. The application creates a new log file each time it runs, making it easy to track keyboard activity across different sessions.

## Features

- Records all keyboard inputs including alphanumeric characters and special keys
- Creates timestamped log files for easy organization
- Handles special keys (space, enter, tab) with appropriate formatting
- Lightweight with minimal dependencies

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/keylogger.git
cd keylogger
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  
# On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the keylogger with:
```bash
python keylogger.py
```

The application will create a `keylog` directory (if it doesn't exist) and begin recording all keyboard inputs to a timestamped text file (e.g., `keylog_2025-03-20 17-04-12.txt`).

To stop the keylogger, press `Ctrl+C` in the terminal where it's running.

## Output

Keystrokes are saved to text files in the `keylog` directory. Special keys are formatted as follows:
- Space: Recorded as a space character
- Enter: Recorded as a new line
- Tab: Recorded as a tab character
- Other special keys: Recorded as `[key_name]` (e.g., `[ctrl]`, `[shift]`)

## Disclaimer

This tool is for educational purposes only. Using a keylogger to record someone's keystrokes without their knowledge or consent may be illegal in your jurisdiction and is an invasion of privacy. Always:

1. Inform users that their keystrokes are being recorded
2. Obtain explicit consent before recording keystrokes
3. Respect privacy and use this tool responsibly

I am not responsible for any misuse of this tool. Use at your own risk.