
from config import config
import os

class Colors:
    def __init__(self):
        self.update_colors()
    
    def update_colors(self):
        """Update colors based on current theme"""
        if config.dark_mode:
            # Dark theme colors
            self.RESET = '\033[0m'
            self.BOLD = '\033[1m'
            self.RED = '\033[91m'
            self.GREEN = '\033[92m'
            self.YELLOW = '\033[93m'
            self.BLUE = '\033[94m'
            self.PURPLE = '\033[95m'
            self.CYAN = '\033[96m'
            self.WHITE = '\033[97m'
            self.GRAY = '\033[90m'
            
            # Background colors for dark theme
            self.BG_BLACK = '\033[40m'
            self.BG_GRAY = '\033[100m'
            
            # Theme specific
            self.PRIMARY = self.CYAN
            self.SECONDARY = self.YELLOW
            self.SUCCESS = self.GREEN
            self.ERROR = self.RED
            self.INFO = self.BLUE
            self.WARNING = self.YELLOW
            self.ACCENT = self.PURPLE
        else:
            # Light theme colors (darker colors for better visibility on light backgrounds)
            self.RESET = '\033[0m'
            self.BOLD = '\033[1m'
            self.RED = '\033[31m'
            self.GREEN = '\033[32m'
            self.YELLOW = '\033[33m'
            self.BLUE = '\033[34m'
            self.PURPLE = '\033[35m'
            self.CYAN = '\033[36m'
            self.WHITE = '\033[37m'
            self.GRAY = '\033[90m'
            
            # Background colors for light theme
            self.BG_WHITE = '\033[47m'
            self.BG_LIGHT_GRAY = '\033[107m'
            
            # Theme specific
            self.PRIMARY = self.BLUE
            self.SECONDARY = self.PURPLE
            self.SUCCESS = self.GREEN
            self.ERROR = self.RED
            self.INFO = self.CYAN
            self.WARNING = self.YELLOW
            self.ACCENT = self.PURPLE

    def clear_screen(self):
        """Clear screen with appropriate background"""
        os.system('cls' if os.name == 'nt' else 'clear')
        if not config.dark_mode:
            # Set light background for light theme
            print(self.BG_WHITE + " " * 80 + self.RESET)
            os.system('cls' if os.name == 'nt' else 'clear')

# Global colors instance
colors = Colors()

def print_colored(text, color=None, bold=False):
    """Print colored text"""
    if color is None:
        color = colors.PRIMARY
    
    style = colors.BOLD if bold else ''
    print(f"{style}{color}{text}{colors.RESET}")

def print_banner():
    """Print themed banner"""
    colors.clear_screen()
    theme_indicator = "🌙 DARK" if config.dark_mode else "☀️ LIGHT"
    
    banner = f"""
{colors.PRIMARY}{colors.BOLD}
                        BlackEye Python
{colors.RESET}
{colors.SECONDARY}Original Shell Program Created By thelinuxchoice
Link to Original: https://github.com/thelinuxchoice/blackeye
{colors.RESET}

{colors.WARNING}Differences:
    - This is written in Python
    - Uses Serveo with A Custom Sub-Domain
    - Dark/Light Mode Support
{colors.RESET}

{colors.ERROR}{colors.BOLD}                        :: DISCLAIMER ::
{colors.RESET}
{colors.ERROR}I nor the original developers take any responsibility for actions caused
by using this program. Any misuse or damage caused by BlackEye is on the
users behalf. Use for EDUCATIONAL PURPOSES!
{colors.RESET}

{colors.INFO}Current Theme: {theme_indicator}{colors.RESET}
{colors.GRAY}Press 'T' at any time to toggle theme{colors.RESET}
    """
    print(banner)
