<?php
require_once __DIR__ . '/_auth.php';
admin_require();

$msg = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $slug = trim($_POST['slug'] ?? '');
    $title = trim($_POST['title'] ?? '');
    $content = (string)($_POST['content'] ?? '');
    if ($slug && $title) {
        q("INSERT INTO pages (slug,title,content) VALUES (?,?,?) ON DUPLICATE KEY UPDATE title=VALUES(title), content=VALUES(content)",
          [$slug,$title,$content]);
        $msg = 'Saved.';
    }
}

$edit = null;
if (!empty($_GET['edit'])) {
    $edit = q("SELECT * FROM pages WHERE slug=?", [$_GET['edit']])->fetch();
}
$list = q("SELECT slug,title,updated_at FROM pages ORDER BY slug")->fetchAll();
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pages · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Pages</h1>
    <?php if ($msg): ?><div class="ok"><?= e($msg) ?></div><?php endif; ?>

    <form method="post" class="form-card">
      <h2><?= $edit ? 'Edit page' : 'New page' ?></h2>
      <label>Slug<input name="slug" required value="<?= e($edit['slug'] ?? '') ?>" <?= $edit?'readonly':'' ?>></label>
      <label>Title<input name="title" required value="<?= e($edit['title'] ?? '') ?>"></label>
      <label>Content (HTML allowed)<textarea name="content" rows="10"><?= e($edit['content'] ?? '') ?></textarea></label>
      <button class="btn primary">Save</button>
      <?php if ($edit): ?><a class="btn" href="pages.php">Cancel</a><?php endif; ?>
    </form>

    <table class="table">
      <thead><tr><th>Slug</th><th>Title</th><th>Updated</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($list as $r): ?>
        <tr>
          <td class="mono"><?= e($r['slug']) ?></td>
          <td><?= e($r['title']) ?></td>
          <td><?= e($r['updated_at']) ?></td>
          <td><a class="btn sm" href="pages.php?edit=<?= e($r['slug']) ?>">Edit</a></td>
        </tr>
      <?php endforeach; ?>
      </tbody>
    </table>
  </main>
</div>
</body></html>