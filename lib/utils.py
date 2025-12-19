import random
import string

class PasswordGenerator:
    """
    Generates potential passwords based on common patterns and random strings.
    """
    def __init__(self):
        self.common_words = [
            "password", "123456", "insta", "hack", "love", "baby", "cool",
            "master", "super", "secret", "admin", "football", "dragon"
        ]

    def generate_random(self):
        """Generates a completely random string."""
        length = random.randint(6, 12)
        chars = string.ascii_letters + string.digits + "!@#$%"
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_pattern(self, base_word):
        """Generates a pattern based password."""
        suffix = random.randint(1, 9999)
        return f"{base_word}{suffix}"

    def get_next_attempt(self):
         # Mix of strategies
        strategy = random.random()
        if strategy < 0.3:
            return self.generate_random()
        elif strategy < 0.7:
             word = random.choice(self.common_words)
             return self.generate_pattern(word)
        else:
            return self.generate_pattern("user")

class TimeManager:
    """
    Manages the timing of the operations.
    """
    @staticmethod
    def get_random_duration_seconds():
        # 5 to 6 minutes in seconds
        return random.randint(5 * 60, 6 * 60)

    @staticmethod
    def sleep_random():
        # Fast attempts: 0.01 to 0.1 seconds
        time.sleep(random.uniform(0.01, 0.1))

import time
