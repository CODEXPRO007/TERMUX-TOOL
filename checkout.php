<?php
$page = 'checkout'; $pageTitle = 'Checkout';
require __DIR__ . '/header.php';

$c = cart_items();
if (!$c['items']) { flash('Your cart is empty.', 'err'); redirect(SITE_URL . '/cart.php'); }

$gw = gateways(true);
if (!$gw) { $gw = []; }

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_check($_POST['csrf'] ?? '')) { flash('Invalid session.', 'err'); redirect(SITE_URL . '/checkout.php'); }

    $name  = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $phone = trim($_POST['phone'] ?? '');
    $addr  = trim($_POST['address'] ?? '');
    $method= trim($_POST['method'] ?? '');

    $err = [];
    if ($name === '') $err[] = 'Name required';
    if ($phone === '' || strlen(preg_replace('/\D/','',$phone)) < 10) $err[] = 'Valid phone required';
    if ($addr === '') $err[] = 'Address required';
    if (!gateway($method) || !gateway($method)['enabled']) $err[] = 'Invalid payment method';

    if ($err) {
        foreach ($err as $x) flash($x, 'err');
    } else {
        $no = order_no();
        $pdo = db(); $pdo->beginTransaction();
        try {
            q("INSERT INTO orders (order_no,customer_name,email,phone,address,subtotal,shipping,total,payment_method,payment_status,order_status)
               VALUES (?,?,?,?,?,?,?,?,?,'pending','placed')",
              [$no,$name,$email,$phone,$addr,$c['subtotal'],$c['shipping'],$c['total'],$method]);
            $oid = (int)$pdo->lastInsertId();
            foreach ($c['items'] as $it) {
                q("INSERT INTO order_items (order_id,product_id,name,price,qty) VALUES (?,?,?,?,?)",
                  [$oid,$it['product']['id'],$it['product']['name'],$it['product']['price'],$it['qty']]);
            }
            $pdo->commit();
        } catch (Throwable $ex) {
            $pdo->rollBack();
            flash('Order failed: ' . $ex->getMessage(), 'err');
            redirect(SITE_URL . '/checkout.php');
        }

        cart_set([]); // clear cart

        try {
            $result = payment_begin(['id'=>$oid,'order_no'=>$no,'total'=>$c['total'],
                                     'customer_name'=>$name,'email'=>$email,'phone'=>$phone,
                                     'payment_method'=>$method]);

            if ($result['type'] === 'redirect') redirect($result['url']);
            if ($result['type'] === 'razorpay') {
                include __DIR__ . '/pay-razorpay.php';
                exit;
            }
            if ($result['type'] === 'cashfree') {
                include __DIR__ . '/pay-cashfree.php';
                exit;
            }
            if ($result['type'] === 'instructions') {
                echo '<div class="wrap"><h1 class="pagetitle">Complete Payment</h1>';
                echo $result['html'];
                echo '</div>';
                require __DIR__ . '/footer.php';
                exit;
            }
        } catch (Throwable $ex) {
            flash('Payment init failed: ' . $ex->getMessage(), 'err');
            redirect(SITE_URL . '/order-success.php?no=' . urlencode($no));
        }
    }
}
?>

<div class="wrap checkout">
  <h1 class="pagetitle">Checkout</h1>
  <div class="checkout-grid">
    <form method="post" class="checkout-form">
      <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
      <h2>Shipping details</h2>
      <label>Full name<input name="name" required value="<?= e($_POST['name'] ?? '') ?>"></label>
      <label>Email<input type="email" name="email" value="<?= e($_POST['email'] ?? '') ?>"></label>
      <label>Phone<input name="phone" required value="<?= e($_POST['phone'] ?? '') ?>"></label>
      <label>Address<textarea name="address" required rows="3"><?= e($_POST['address'] ?? '') ?></textarea></label>

      <h2>Payment method</h2>
      <?php if (!$gw): ?>
        <p class="muted">No payment methods configured yet.</p>
      <?php else: ?>
        <div class="methods">
          <?php foreach ($gw as $i => $g): ?>
            <label class="method">
              <input type="radio" name="method" value="<?= e($g['code']) ?>" <?= $i===0?'checked':'' ?>>
              <span>
                <b><?= e($g['name']) ?></b>
                <small><?= e($g['description']) ?></small>
              </span>
            </label>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>

      <button class="btn primary block" <?= !$gw?'disabled':'' ?>>Place order · <?= money($c['total']) ?></button>
    </form>

    <aside class="checkout-summary">
      <h2>Order summary</h2>
      <?php foreach ($c['items'] as $it): ?>
        <div class="row"><span><?= e($it['product']['name']) ?> × <?= (int)$it['qty'] ?></span><b><?= money((float)$it['line']) ?></b></div>
      <?php endforeach; ?>
      <div class="row"><span>Subtotal</span><b><?= money($c['subtotal']) ?></b></div>
      <div class="row"><span>Shipping</span><b><?= $c['shipping']>0?money($c['shipping']):'Free' ?></b></div>
      <div class="row grand"><span>Total</span><b><?= money($c['total']) ?></b></div>
    </aside>
  </div>
</div>

<?php require __DIR__ . '/footer.php'; ?>