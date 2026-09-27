<?php
// ─────────────────────────────────────────────
//  SmartStore — main config
// ─────────────────────────────────────────────
declare(strict_types=1);

define('DB_HOST', '127.0.0.1');
define('DB_NAME', 'smartstore');
define('DB_USER', 'root');
define('DB_PASS', '');

define('SITE_URL', 'http://localhost/smartstore');   // no trailing slash
define('UPLOAD_DIR', __DIR__ . '/uploads');
define('UPLOAD_URL', SITE_URL . '/uploads');

// Security
define('APP_SECRET', 'CHANGE_THIS_TO_A_LONG_RANDOM_STRING_1234567890');
define('ADMIN_COOKIE', 'ss_admin');

// Timezone
date_default_timezone_set('Asia/Kolkata');

// Error reporting — turn off display in production
ini_set('display_errors', '1');
error_reporting(E_ALL);

// Session
if (session_status() !== PHP_SESSION_ACTIVE) {
    session_name('ss_sid');
    session_start();
}