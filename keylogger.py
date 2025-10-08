"""
Educational Keylogger Simulator - Simple guaranteed version
For Keyloggers-detector deployment
"""

import os
from datetime import datetime

log_file = '/tmp/keystrokes.log'

def main():
    print("=== Simple Keylogger ===")
    print(f"Logging to: {log_file}")
    print("Type anything and press Enter. Type 'QUIT' to stop.")
    print("-" * 50)

    # Initialize log file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n=== Session started at {datetime.now()} ===\n")

    try:
        while True:
            # Get input from user
            user_input = input("Type here: ")

            if user_input.upper() == 'QUIT':
                break

            # Log the input with timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {user_input}\n")

            print(f"Logged: '{user_input}'")

    except KeyboardInterrupt:
        print("\nStopped by Ctrl+C")

    # Write shutdown message
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"=== Session ended at {datetime.now()} ===\n\n")

    print(f"\n=== Keylogger stopped ===")
    print(f"Check: cat {log_file}")

if __name__ == "__main__":
    main()
