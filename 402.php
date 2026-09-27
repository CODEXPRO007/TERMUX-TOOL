<?php
$pageTitle = 'Not found';
$page = '404';
require __DIR__ . '/header.php';
?>
<div class="wrap" style="padding:80px 24px;text-align:center">
  <h1 class="pagetitle">404 — Page not found</h1>
  <p class="muted">That page doesn't exist. <a href="<?= SITE_URL ?>/">Back to shop</a></p>
</div>
<?php require __DIR__ . '/footer.php'; ?>