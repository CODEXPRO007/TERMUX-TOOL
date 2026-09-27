<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/includes/db.php';
require_once __DIR__ . '/includes/functions.php';

$slug = $_GET['slug'] ?? '';
$p = q("SELECT * FROM products WHERE slug=? AND active=1 LIMIT 1", [$slug])->fetch();
if (!$p) { http_response_code(404); include __DIR__ . '/404.php'; exit; }

$pageTitle = $p['name'] . ' — ' . setting('site_name');
$page = 'product';
require __DIR__ . '/header.php';
?>

<div class="wrap product">
  <div class="product-img">
    <?php if (!empty($p['image']) && file_exists(UPLOAD_DIR . '/' . $p['image'])): ?>
      <img src="<?= UPLOAD_URL . '/' . e($p['image']) ?>" alt="<?= e($p['name']) ?>">
    <?php else: ?>
      <span class="ph big">◈</span>
    <?php endif; ?>
  </div>
  <div class="product-info">
    <h1><?= e($p['name']) ?></h1>
    <div class="price big"><?= money((float)$p['price']) ?></div>
    <p class="muted">In stock: <?= (int)$p['stock'] ?></p>
    <p><?= nl2br(e($p['description'])) ?></p>
    <form method="post" action="<?= SITE_URL ?>/api/cart.php" class="buy-row">
      <input type="hidden" name="action" value="add">
      <input type="hidden" name="id" value="<?= (int)$p['id'] ?>">
      <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
      <input type="number" name="qty" value="1" min="1" max="99" class="qty">
      <button class="btn primary">Add to cart</button>
      <a class="btn" href="<?= SITE_URL ?>/cart.php">Go to cart</a>
    </form>
  </div>
</div>

<?php require __DIR__ . '/footer.php'; ?>