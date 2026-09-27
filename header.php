<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/includes/db.php';
require_once __DIR__ . '/includes/functions.php';
require_once __DIR__ . '/includes/payments.php';

$siteName = setting('site_name', 'SmartStore');
$tagline  = setting('site_tagline', '');
$cc       = count(cart());
$page     = $page ?? 'home';
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0b0f1a">
<title><?= e($pageTitle ?? $siteName) ?></title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css">
</head>
<body>

<header class="top">
  <div class="wrap top-inner">
    <a class="brand" href="<?= SITE_URL ?>/">
      <span class="brand-mark">◈</span>
      <span class="brand-text"><b><?= e($siteName) ?></b><small><?= e($tagline) ?></small></span>
    </a>
    <form class="search" action="<?= SITE_URL ?>/index.php" method="get">
      <input name="q" placeholder="Search products…" value="<?= e($_GET['q'] ?? '') ?>">
      <button aria-label="Search">⌕</button>
    </form>
    <nav class="nav">
      <a href="<?= SITE_URL ?>/index.php">Shop</a>
      <a href="<?= SITE_URL ?>/track-order.php">Track</a>
      <a href="<?= SITE_URL ?>/contact.php">Contact</a>
      <a class="cart-btn" href="<?= SITE_URL ?>/cart.php">Cart <b><?= $cc ?></b></a>
    </nav>
  </div>
</header>

<?php if ($f = flash()): ?>
  <div class="toast <?= e($f['type']) ?>"><?= e($f['msg']) ?></div>
<?php endif; ?>

<main class="page">