<?php
require_once __DIR__ . '/_auth.php';
admin_require();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = (int)($_POST['id'] ?? 0);
    $ps = $_POST['payment_status'] ?? '';
    $os = $_POST['order_status'] ?? '';
    if ($id) {
        q("UPDATE orders SET payment_status=?, order_status=? WHERE id=?",
          [$ps, $os, $id]);
    }
}

$order = null; $items = [];
if (!empty($_GET['id'])) {
    $order = q("SELECT * FROM orders WHERE id=?", [(int)$_GET['id']])->fetch();
    if ($order) $items = q("SELECT * FROM order_items WHERE order_id=?", [$order['id']])->fetchAll();
}
$list = q("SELECT * FROM orders ORDER BY id DESC LIMIT 100")->fetchAll();
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Orders</h1>

    <?php if ($order): ?>
      <div class="form-card">
        <h2><?= e($order['order_no']) ?></h2>
        <p class="mono">
          <?= e($order['customer_name']) ?> · <?= e($order['phone']) ?> · <?= e($order['email']) ?><br>
          <?= nl2br(e($order['address'])) ?>
        </p>
        <ul class="summary">
          <?php foreach ($items as $it): ?>
            <li><span><?= e($it['name']) ?> × <?= (int)$it['qty'] ?></span><b><?= money((float)$it['price'] * (int)$it['qty']) ?></b></li>
          <?php endforeach; ?>
          <li><span>Subtotal</span><b><?= money((float)$order['subtotal']) ?></b></li>
          <li><span>Shipping</span><b><?= money((float)$order['shipping']) ?></b></li>
          <li><span>Total</span><b><?= money((float)$order['total']) ?></b></li>
        </ul>

        <form method="post">
          <input type="hidden" name="id" value="<?= (int)$order['id'] ?>">
          <label>Payment status
            <select name="payment_status">
              <?php foreach (['pending','paid','failed','refunded'] as $s): ?>
                <option value="<?= $s ?>" <?= $order['payment_status']===$s?'selected':'' ?>><?= $s ?></option>
              <?php endforeach; ?>
            </select>
          </label>
          <label>Order status
            <select name="order_status">
              <?php foreach (['placed','processing','shipped','delivered','cancelled'] as $s): ?>
                <option value="<?= $s ?>" <?= $order['order_status']===$s?'selected':'' ?>><?= $s ?></option>
              <?php endforeach; ?>
            </select>
          </label>
          <button class="btn primary">Update</button>
          <a class="btn" href="orders.php">Back</a>
        </form>
      </div>
    <?php endif; ?>

    <table class="table">
      <thead><tr><th>Order</th><th>Customer</th><th>Total</th><th>Pay</th><th>Order</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($list as $r): ?>
        <tr>
          <td class="mono"><?= e($r['order_no']) ?></td>
          <td><?= e($r['customer_name']) ?></td>
          <td><?= money((float)$r['total']) ?></td>
          <td><?= e($r['payment_method']) ?> · <?= e($r['payment_status']) ?></td>
          <td><?= e($r['order_status']) ?></td>
          <td><a class="btn sm" href="orders.php?id=<?= (int)$r['id'] ?>">Open</a></td>
        </tr>
      <?php endforeach; ?>
      </tbody>
    </table>
  </main>
</div>
</body></html>