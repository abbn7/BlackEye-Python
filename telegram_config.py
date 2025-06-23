
# إعدادات بوت Telegram
TELEGRAM_BOT_TOKEN = "5984403789:AAG0N8ThL71h4mIxPuIb4F863OyZurWBM8A"
TELEGRAM_CHAT_ID = "5322402925"  # تم تعيينه

def set_chat_id(chat_id):
    """Set the Telegram chat ID"""
    global TELEGRAM_CHAT_ID
    TELEGRAM_CHAT_ID = chat_id

def get_bot_token():
    """Get the bot token"""
    return TELEGRAM_BOT_TOKEN

def get_chat_id():
    """Get the chat ID"""
    return TELEGRAM_CHAT_ID
