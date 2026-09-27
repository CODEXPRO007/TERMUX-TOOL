<?php
declare(strict_types=1);

/**
 * Payment gateway abstraction.
 * Each gateway is a row in `payment_gateways` with JSON `config`.
 * To add a new gateway, insert a row from the admin panel — no code change.
 */

function gateways(bool $onlyEnabled = false): array {
    $sql = "SELECT * FROM payment_gateways";
    if ($onlyEnabled) $sql .= " WHERE enabled=1";
    $sql .= " ORDER BY sort_order, id";
    return q($sql)->fetchAll();
}

function gateway(string $code): ?array {
    $r = q("SELECT * FROM payment_gateways WHERE code=? LIMIT 1", [$code])->fetch();
    return $r ?: null;
}

function gateway_config(array $g): array {
    $c = json_decode($g['config'] ?? '{}', true);
    return is_array($c) ? $c : [];
}

/**
 * Create a "payment intent" for the given order.
 * Returns an array with:
 *   ['type' => 'redirect'|'instructions', 'url' => ..., 'html' => ...]
 */
function payment_begin(array $order): array {
    $g = gateway($order['payment_method']);
    if (!$g) throw new RuntimeException('Payment method not available');

    $cfg = gateway_config($g);
    $mode = $g['mode'];

    switch ($g['code']) {

        case 'cod':
            // Nothing to do; mark pending COD
            q("UPDATE orders SET payment_status='pending' WHERE id=?", [$order['id']]);
            return ['type' => 'redirect', 'url' => SITE_URL . '/order-success.php?no=' . urlencode($order['order_no'])];

        case 'razorpay':
            $key = $cfg['key_id'] ?? ''; $secret = $cfg['key_secret'] ?? '';
            if (!$key || !$secret) throw new RuntimeException('Razorpay keys not configured');
            // Create order via Razorpay Orders API
            $amount = (int)round(((float)$order['total']) * 100);
            $payload = json_encode(['amount' => $amount, 'currency' => 'INR', 'receipt' => $order['order_no']]);
            $ch = curl_init('https://api.razorpay.com/v1/orders');
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_USERPWD        => $key . ':' . $secret,
                CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
                CURLOPT_POSTFIELDS     => $payload,
                CURLOPT_TIMEOUT        => 20,
            ]);
            $resp = curl_exec($ch);
            $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
            if ($code !== 200) throw new RuntimeException('Razorpay order create failed: ' . $resp);
            $rz = json_decode((string)$resp, true);
            return ['type' => 'razorpay', 'order' => $rz, 'key' => $key];

        case 'cashfree':
            $appId = $cfg['app_id'] ?? ''; $sec = $cfg['secret_key'] ?? '';
            if (!$appId || !$sec) throw new RuntimeException('Cashfree keys not configured');
            $base = $mode === 'live' ? 'https://api.cashfree.com/pg' : 'https://sandbox.cashfree.com/pg';
            $payload = json_encode([
                'order_id'       => $order['order_no'],
                'order_amount'   => (float)$order['total'],
                'order_currency' => 'INR',
                'customer_details' => [
                    'customer_id'    => 'CUST_' . $order['id'],
                    'customer_name'  => $order['customer_name'],
                    'customer_email' => $order['email'] ?: 'noreply@example.com',
                    'customer_phone' => preg_replace('/\D/', '', $order['phone'] ?: '9999999999'),
                ],
                'order_meta' => [
                    'return_url' => SITE_URL . '/order-success.php?no=' . urlencode($order['order_no']),
                ],
            ]);
            $ch = curl_init($base . '/orders');
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POST           => true,
                CURLOPT_HTTPHEADER     => [
                    'Content-Type: application/json',
                    'x-api-version: 2023-08-01',
                    'x-client-id: ' . $appId,
                    'x-client-secret: ' . $sec,
                ],
                CURLOPT_POSTFIELDS     => $payload,
                CURLOPT_TIMEOUT        => 20,
            ]);
            $resp = curl_exec($ch);
            $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
            if ($code < 200 || $code >= 300) throw new RuntimeException('Cashfree order failed: ' . $resp);
            $cf = json_decode((string)$resp, true);
            $link = $cf['payment_session_id'] ?? null;
            // Cashfree requires JS SDK; we redirect to a bridge page
            return ['type' => 'cashfree', 'session' => $link, 'order' => $cf];

        case 'upi_manual':
            return ['type' => 'instructions', 'html' => upi_instructions($cfg, $order)];

        case 'crypto':
            return ['type' => 'instructions', 'html' => crypto_instructions($cfg, $order)];

        default:
            throw new RuntimeException('Unknown payment gateway: ' . $g['code']);
    }
}

function upi_instructions(array $cfg, array $order): string {
    $upi   = $cfg['upi_id'] ?? '';
    $payee = $cfg['payee_name'] ?? setting('site_name');
    $amt   = number_format((float)$order['total'], 2, '.', '');
    $note  = urlencode('Order ' . $order['order_no']);
    $upiLink = "upi://pay?pa={$upi}&pn=" . urlencode($payee) . "&am={$amt}&tn={$note}&cu=INR";

    return '<div class="pay-box">'
         . '<h3>Pay via UPI</h3>'
         . '<p>Scan the QR or tap the link below, then enter your UTR / reference number to confirm.</p>'
         . '<p><a class="btn primary" href="' . e($upiLink) . '">Open UPI App</a></p>'
         . '<p class="mono">UPI ID: <b>' . e($upi) . '</b><br>Amount: <b>' . money((float)$order['total']) . '</b><br>Note: <b>' . e($order['order_no']) . '</b></p>'
         . '<form method="post" action="' . SITE_URL . '/order-success.php">'
         . '<input type="hidden" name="order_no" value="' . e($order['order_no']) . '">'
         . '<input type="hidden" name="csrf" value="' . csrf_token() . '">'
         . '<label>UTR / Reference</label>'
         . '<input name="utr" required minlength="6" placeholder="e.g. 123456789012">'
         . '<button class="btn primary">I have paid</button>'
         . '</form>'
         . '</div>';
}

function crypto_instructions(array $cfg, array $order): string {
    $btc  = $cfg['wallet_btc'] ?? '';
    $eth  = $cfg['wallet_eth'] ?? '';
    $usdt = $cfg['wallet_usdt'] ?? '';
    return '<div class="pay-box">'
         . '<h3>Pay via Crypto</h3>'
         . '<p>Send the equivalent to any wallet below. Then submit your transaction hash.</p>'
         . '<p class="mono">BTC: <b>' . e($btc) . '</b><br>ETH: <b>' . e($eth) . '</b><br>USDT (TRC20): <b>' . e($usdt) . '</b></p>'
         . '<p>Amount: <b>' . money((float)$order['total']) . '</b></p>'
         . '<form method="post" action="' . SITE_URL . '/order-success.php">'
         . '<input type="hidden" name="order_no" value="' . e($order['order_no']) . '">'
         . '<input type="hidden" name="csrf" value="' . csrf_token() . '">'
         . '<label>Transaction hash</label>'
         . '<input name="txhash" required minlength="10" placeholder="0x… or BTC txid">'
         . '<button class="btn primary">Submit transaction</button>'
         . '</form>'
         . '</div>';
}