<?php
$page = 'success'; $pageTitle = 'Order Confirmed';
require __DIR__ . '/header.php';

$no = $_GET['no'] ?? ($_POST['order_no'] ?? '');
$order = q("SELECT * FROM orders WHERE order_no=? LIMIT 1", [$no])->fetch();

// Manual verification paths (UPI / Crypto)
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $order) {
    if (!csrf_check($_POST['csrf'] ?? '')) {
        flash('Invalid session', 'err');
    } else {
        $ref = trim($_POST['utr'] ?? $_POST['txhash'] ?? '');
        if ($ref !== '') {
            q("UPDATE orders SET payment_ref=?, payment_status='paid', order_status='processing' WHERE id=?",
              [$ref, $order['id']]);
            flash('Payment reference saved. We will verify shortly.', 'ok');
            $order = q("SELECT * FROM orders WHERE id=?", [$order['id']])->fetch();
        }
    }
}
?>

<div class="wrap success">
  <?php if (!$order): ?>
    <h1 class="pagetitle">Order not found</h1>
    <p class="muted">Check the order number or <a href="<?= SITE_URL ?>/track-order.php">track your order</a>.</p>
  <?php else: ?>
    <div class="success-box">
      <div class="success-ico">✓</div>
      <h1>Thank you, <?= e($order['customer_name']) ?>!</h1>
      <p class="muted">Your order <b class="mono"><?= e($order['order_no']) ?></b> has been placed.</p>
      <ul class="summary">
        <li><span>Total</span><b><?= money((float)$order['total']) ?></b></li>
        <li><span>Payment</span><b><?= e($order['payment_method']) ?> · <?= e($order['payment_status']) ?></b></li>
        <li><span>Order status</span><b><?= e($order['order_status']) ?></b></li>
        <?php if ($order['payment_ref']): ?>
          <li><span>Reference</span><b class="mono"><?= e($order['payment_ref']) ?></b></li>
        <?php endif; ?>
      </ul>
      <p><a class="btn primary" href="<?= SITE_URL ?>/track-order.php?no=<?= e($order['order_no']) ?>">Track order</a>
         <a class="btn" href="<?= SITE_URL ?>/">Continue shopping</a></p>
    </div>
  <?php endif; ?>
</div>

<?php require __DIR__ . '/footer.php'; ?>