<?php
$page = 'cart'; $pageTitle = 'Your Cart';
require __DIR__ . '/header.php';
$c = cart_items();
?>

<div class="wrap">
  <h1 class="pagetitle">Your Cart</h1>

  <?php if (!$c['items']): ?>
    <p class="muted">Cart is empty. <a href="<?= SITE_URL ?>/index.php">Continue shopping</a></p>
  <?php else: ?>
    <table class="table">
      <thead><tr><th>Product</th><th>Price</th><th>Qty</th><th>Subtotal</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($c['items'] as $it):
        $p = $it['product']; ?>
        <tr>
          <td><?= e($p['name']) ?></td>
          <td><?= money((float)$p['price']) ?></td>
          <td>
            <form method="post" action="<?= SITE_URL ?>/api/cart.php" class="qty-form">
              <input type="hidden" name="action" value="update">
              <input type="hidden" name="id" value="<?= (int)$p['id'] ?>">
              <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
              <input type="number" name="qty" value="<?= (int)$it['qty'] ?>" min="0" max="99">
              <button class="btn sm">Update</button>
            </form>
          </td>
          <td><?= money((float)$it['line']) ?></td>
          <td>
            <form method="post" action="<?= SITE_URL ?>/api/cart.php">
              <input type="hidden" name="action" value="remove">
              <input type="hidden" name="id" value="<?= (int)$p['id'] ?>">
              <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
              <button class="btn sm danger">Remove</button>
            </form>
          </td>
        </tr>
      <?php endforeach; ?>
      </tbody>
    </table>

    <div class="totals">
      <div><span>Subtotal</span><b><?= money($c['subtotal']) ?></b></div>
      <div><span>Shipping</span><b><?= $c['shipping'] > 0 ? money($c['shipping']) : 'Free' ?></b></div>
      <div class="grand"><span>Total</span><b><?= money($c['total']) ?></b></div>
      <a class="btn primary block" href="<?= SITE_URL ?>/checkout.php">Checkout</a>
    </div>
  <?php endif; ?>
</div>

<?php require __DIR__ . '/footer.php'; ?>