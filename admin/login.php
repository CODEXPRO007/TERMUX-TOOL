<?php
require_once __DIR__ . '/_auth.php';

$err = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email'] ?? '');
    $pass  = (string)($_POST['password'] ?? '');
    $u = q("SELECT * FROM users WHERE email=? AND role='admin' LIMIT 1", [$email])->fetch();
    if ($u && password_verify($pass, $u['password'])) {
        $_SESSION['admin_id'] = (int)$u['id'];
        redirect(SITE_URL . '/admin/index.php');
    }
    $err = 'Invalid credentials.';
}
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin Login · <?= e(setting('site_name')) ?></title>
<link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-login">
  <form method="post">
    <h1>Admin Login</h1>
    <?php if ($err): ?><div class="err"><?= e($err) ?></div><?php endif; ?>
    <label>Email<input type="email" name="email" required autofocus></label>
    <label>Password<input type="password" name="password" required></label>
    <button class="btn primary block">Sign in</button>
    <p class="muted">Default: admin@smartstore.local / admin123</p>
  </form>
</div>
</body></html>