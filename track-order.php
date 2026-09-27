<?php
$page = 'track'; $pageTitle = 'Track Order';
require __DIR__ . '/header.php';

$no = trim($_GET['no'] ?? $_POST['no'] ?? '');
$order = null; $items = [];
if ($no !== '') {
    $order = q("SELECT * FROM orders WHERE order_no=? LIMIT 1", [$no])->fetch();
    if ($order) $items = q("SELECT * FROM order_items WHERE order_id=?", [$order['id']])->fetchAll();
}
?>

<div class="wrap">
  <h1 class="pagetitle">Track your order</h1>
  <form method="get" class="track-form">
    <input name="no" placeholder="Enter order number e.g. SS-240101-ABCDEF" value="<?= e($no) ?>" required>
    <button class="btn primary">Track</button>
  </form>

  <?php if ($no !== '' && !$order): ?>
    <p class="muted">No order found for that number.</p>
  <?php elseif ($order): ?>
    <div class="track-box">
      <h2><?= e($order['order_no']) ?></h2>
      <div class="stages">
        <?php
        $stages = ['placed','processing','shipped','delivered'];
        $cur = array_search($order['order_status'], $stages, true);
        foreach ($stages as $i => $s):
          $cls = $i <= $cur ? 'done' : '';
        ?>
          <div class="stage <?= $cls ?>"><span class="dot"></span><b><?= ucfirst($s) ?></b></div>
        <?php endforeach; ?>
      </div>
      <ul class="summary">
        <li><span>Placed on</span><b><?= e($order['created_at']) ?></b></li>
        <li><span>Payment</span><b><?= e($order['payment_method']) ?> · <?= e($order['payment_status']) ?></b></li>
        <li><span>Total</span><b><?= money((float)$order['total']) ?></b></li>
      </ul>
      <h3>Items</h3>
      <ul class="items">
        <?php foreach ($items as $it): ?>
          <li><?= e($it['name']) ?> × <?= (int)$it['qty'] ?> — <?= money((float)$it['price'] * (int)$it['qty']) ?></li>
        <?php endforeach; ?>
      </ul>
    </div>
  <?php endif; ?>
</div>

<?php require __DIR__ . '/footer.php'; ?>