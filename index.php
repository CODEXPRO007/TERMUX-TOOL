<?php
$page = 'home'; $pageTitle = 'SmartStore — Premium Products';
require __DIR__ . '/header.php';

$q = trim($_GET['q'] ?? '');
if ($q !== '') {
    $rows = q("SELECT * FROM products WHERE active=1 AND (name LIKE ? OR description LIKE ?) ORDER BY id DESC",
              ["%$q%", "%$q%"])->fetchAll();
} else {
    $rows = q("SELECT * FROM products WHERE active=1 ORDER BY id DESC LIMIT 24")->fetchAll();
}
?>

<section class="hero">
  <div class="wrap">
    <h1>Shop smarter.<br><span>Live faster.</span></h1>
    <p>Curated products, honest prices, real-time order tracking. Pay with UPI, cards, crypto — your choice.</p>
    <a class="btn primary" href="#catalog">Browse catalog</a>
  </div>
</section>

<section class="wrap" id="catalog">
  <div class="sec-head">
    <h2><?= $q !== '' ? 'Results for "' . e($q) . '"' : 'Featured products' ?></h2>
    <span class="muted"><?= count($rows) ?> items</span>
  </div>
  <div class="grid">
    <?php foreach ($rows as $r): ?>
      <article class="card">
        <a class="card-img" href="<?= SITE_URL ?>/product.php?slug=<?= e($r['slug']) ?>">
          <?php if (!empty($r['image']) && file_exists(UPLOAD_DIR . '/' . $r['image'])): ?>
            <img src="<?= UPLOAD_URL . '/' . e($r['image']) ?>" alt="<?= e($r['name']) ?>">
          <?php else: ?>
            <span class="ph">◈</span>
          <?php endif; ?>
        </a>
        <div class="card-body">
          <h3><a href="<?= SITE_URL ?>/product.php?slug=<?= e($r['slug']) ?>"><?= e($r['name']) ?></a></h3>
          <div class="price"><?= money((float)$r['price']) ?></div>
          <form method="post" action="<?= SITE_URL ?>/api/cart.php">
            <input type="hidden" name="action" value="add">
            <input type="hidden" name="id" value="<?= (int)$r['id'] ?>">
            <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
            <button class="btn">Add to cart</button>
          </form>
        </div>
      </article>
    <?php endforeach; ?>
    <?php if (!$rows): ?>
      <p class="muted">No products found.</p>
    <?php endif; ?>
  </div>
</section>

<?php require __DIR__ . '/footer.php'; ?>