import os
import sys
import time
try:
    from colorama import init, Fore, Style
    from art import tprint
    init()
except ImportError:
    # Fallback if libraries aren't installed yet
    class Fore:
        MAGENTA = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'
    def tprint(text):
        print(text)

class Color:
    HEADER = Fore.MAGENTA
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    RED = Fore.RED
    ENDC = Fore.RESET
    BOLD = Style.BRIGHT

class Display:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_banner():
        print(Color.GREEN)
        tprint("Insta-Hack")
        print(f"""
        {Color.BLUE}>> v2.5.1 Enhanced Edition <<{Color.ENDC}
        """)

    @staticmethod
    def log(message, level="INFO"):
        prefix = "[*]"
        color = Color.BLUE
        if level == "SUCCESS":
            prefix = "[+]"
            color = Color.GREEN
        elif level == "ERROR":
            prefix = "[-]"
            color = Color.FAIL
        elif level == "WARNING":
            prefix = "[!]"
            color = Color.WARNING
        
        print(f"{color}{prefix} {message}{Color.ENDC}")

    @staticmethod
    def animate_text(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

import time
