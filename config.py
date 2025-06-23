
import json
import os

CONFIG_FILE = "settings.json"

class Config:
    def __init__(self):
        self.dark_mode = True
        self.load_config()
    
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    self.dark_mode = data.get('dark_mode', True)
            except:
                pass
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump({
                    'dark_mode': self.dark_mode
                }, f, indent=2)
        except:
            pass
    
    def toggle_dark_mode(self):
        """Toggle dark mode setting"""
        self.dark_mode = not self.dark_mode
        self.save_config()
        return self.dark_mode

# Global config instance
config = Config()
