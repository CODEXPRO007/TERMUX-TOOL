<?php
declare(strict_types=1);
require_once __DIR__ . '/../config.php';
require_once __DIR__ . '/../includes/db.php';
require_once __DIR__ . '/../includes/functions.php';
require_once __DIR__ . '/../includes/payments.php';

header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true) ?: [];
$orderNo   = $input['order_no'] ?? '';
$paymentId = $input['payment_id'] ?? '';
$signature = $input['signature'] ?? '';

$order = q("SELECT * FROM orders WHERE order_no=? LIMIT 1", [$orderNo])->fetch();
if (!$order) { http_response_code(404); echo json_encode(['ok'=>false,'msg'=>'Order not found']); exit; }

$g = gateway($order['payment_method']);
if (!$g || $g['code'] !== 'razorpay') { echo json_encode(['ok'=>false,'msg'=>'Not a Razorpay order']); exit; }

$cfg = gateway_config($g);
$secret = $cfg['key_secret'] ?? '';
$expected = hash_hmac('sha256', $orderNo . '|' . $paymentId, $secret);

if (!hash_equals($expected, $signature)) {
    q("UPDATE orders SET payment_status='failed' WHERE id=?", [$order['id']]);
    echo json_encode(['ok'=>false,'msg'=>'Signature mismatch']); exit;
}

q("UPDATE orders SET payment_status='paid', payment_ref=?, order_status='processing' WHERE id=?",
  [$paymentId, $order['id']]);

echo json_encode(['ok'=>true,'order_no'=>$orderNo]);