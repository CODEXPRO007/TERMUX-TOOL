<?php
require_once __DIR__ . '/_auth.php';
admin_require();

$msg = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    foreach ($_POST as $k => $v) {
        if (strpos($k, 'set_') === 0) {
            q("INSERT INTO settings (k,v) VALUES (?,?) ON DUPLICATE KEY UPDATE v=VALUES(v)",
              [substr($k, 4), (string)$v]);
        }
    }
    $msg = 'Saved.';
}
$keys = ['site_name','site_tagline','currency','currency_symbol','contact_email','contact_phone','shipping_flat','free_shipping_above','footer_note'];
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Settings · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Settings</h1>
    <?php if ($msg): ?><div class="ok"><?= e($msg) ?></div><?php endif; ?>
    <form method="post" class="form-card">
      <?php foreach ($keys as $k): ?>
        <label><?= e($k) ?><input name="set_<?= e($k) ?>" value="<?= e(setting($k)) ?>"></label>
      <?php endforeach; ?>
      <button class="btn primary">Save</button>
    </form>
  </main>
</div>
</body></html>