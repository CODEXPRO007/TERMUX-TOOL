<?php /* included from checkout.php with $result, $order */ ?>
<!DOCTYPE html><html><head>
<meta charset="utf-8"><title>Processing payment…</title>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<style>body{background:#0b0f1a;color:#eef2f8;font-family:system-ui;display:grid;place-items:center;height:100vh;margin:0}</style>
</head><body>
<div>Opening secure Razorpay checkout…</div>
<script>
var rzp = new Razorpay({
  key: <?= json_encode($result['key']) ?>,
  order_id: <?= json_encode($result['order']['id']) ?>,
  name: <?= json_encode(setting('site_name')) ?>,
  description: <?= json_encode('Order ' . $order['order_no']) ?>,
  prefill: {
    name: <?= json_encode($order['customer_name']) ?>,
    email: <?= json_encode($order['email']) ?>,
    contact: <?= json_encode($order['phone']) ?>
  },
  theme: { color: '#ff3d00' },
  handler: function (res) {
    fetch('<?= SITE_URL ?>/api/create-order.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        order_no: <?= json_encode($order['order_no']) ?>,
        payment_id: res.razorpay_payment_id,
        signature: res.razorpay_signature
      })
    }).then(r => r.json()).then(j => {
      window.location = '<?= SITE_URL ?>/order-success.php?no=' + encodeURIComponent(<?= json_encode($order['order_no']) ?>);
    }).catch(() => {
      window.location = '<?= SITE_URL ?>/order-success.php?no=' + encodeURIComponent(<?= json_encode($order['order_no']) ?>);
    });
  }
});
rzp.open();
</script>
</body></html>


Kaha add karna hai 