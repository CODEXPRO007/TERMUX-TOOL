<?php
require_once __DIR__ . '/../config.php';
require_once __DIR__ . '/../includes/db.php';
require_once __DIR__ . '/../includes/functions.php';

$raw = file_get_contents('php://input');
$data = json_decode($raw, true) ?: [];

// Cashfree format: data.order.order_id, data.payment.payment_status
$orderId = $data['data']['order']['order_id'] ?? ($data['order_id'] ?? '');
$status  = $data['data']['payment']['payment_status'] ?? ($data['status'] ?? '');

if ($orderId && in_array(strtoupper($status), ['SUCCESS','PAID','CAPTURED'], true)) {
    q("UPDATE orders SET payment_status='paid', order_status='processing' WHERE order_no=?", [$orderId]);
}
http_response_code(200);
echo 'ok';