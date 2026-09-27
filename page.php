<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/includes/db.php';
require_once __DIR__ . '/includes/functions.php';

$slug = $_GET['slug'] ?? 'about';
$p = q("SELECT * FROM pages WHERE slug=? LIMIT 1", [$slug])->fetch();
if (!$p) { http_response_code(404); $p = ['title' => 'Page not found', 'content' => '']; }

$pageTitle = $p['title'] . ' — ' . setting('site_name');
$page = 'page';
require __DIR__ . '/header.php';
?>

<div class="wrap policy">
  <h1 class="pagetitle"><?= e($p['title']) ?></h1>
  <div class="policy-body"><?= $p['content'] ?></div>
</div>

<?php require __DIR__ . '/footer.php'; ?>