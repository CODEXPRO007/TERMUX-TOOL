<?php
require_once __DIR__ . '/_auth.php';
$me = admin_require();

$totalOrders = (int)q("SELECT COUNT(*) c FROM orders")->fetch()['c'];
$totalRevenue = (float)(q("SELECT COALESCE(SUM(total),0) s FROM orders WHERE payment_status='paid'")->fetch()['s']);
$pending = (int)q("SELECT COUNT(*) c FROM orders WHERE order_status='placed'")->fetch()['c'];
$products = (int)q("SELECT COUNT(*) c FROM products WHERE active=1")->fetch()['c'];
$recent = q("SELECT * FROM orders ORDER BY id DESC LIMIT 10")->fetchAll();
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Dashboard</h1>
    <div class="cards">
      <div class="stat"><div class="k">Orders</div><div class="v"><?= $totalOrders ?></div></div>
      <div class="stat"><div class="k">Revenue (paid)</div><div class="v"><?= money($totalRevenue) ?></div></div>
      <div class="stat"><div class="k">Pending</div><div class="v"><?= $pending ?></div></div>
      <div class="stat"><div class="k">Products</div><div class="v"><?= $products ?></div></div>
    </div>
    <h2>Recent orders</h2>
    <table class="table">
      <thead><tr><th>Order</th><th>Customer</th><th>Total</th><th>Payment</th><th>Status</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($recent as $r): ?>
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