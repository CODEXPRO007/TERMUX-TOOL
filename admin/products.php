<?php
require_once __DIR__ . '/_auth.php';
admin_require();

$cats = q("SELECT * FROM categories ORDER BY name")->fetchAll();
$msg = '';

// Handle create / update / delete
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $act = $_POST['act'] ?? '';
    if ($act === 'save') {
        $id = (int)($_POST['id'] ?? 0);
        $name = trim($_POST['name'] ?? '');
        $desc = trim($_POST['description'] ?? '');
        $price = (float)($_POST['price'] ?? 0);
        $stock = (int)($_POST['stock'] ?? 0);
        $cat = (int)($_POST['category_id'] ?? 0) ?: null;
        $active = isset($_POST['active']) ? 1 : 0;
        $slug = slugify($name);

        // Optional image upload
        $image = null;
        if (!empty($_FILES['image']['tmp_name']) && is_uploaded_file($_FILES['image']['tmp_name'])) {
            if (!is_dir(UPLOAD_DIR)) @mkdir(UPLOAD_DIR, 0775, true);
            $ext = strtolower(pathinfo($_FILES['image']['name'], PATHINFO_EXTENSION));
            if (in_array($ext, ['jpg','jpeg','png','webp','gif'], true)) {
                $image = 'p_' . time() . '_' . bin2hex(random_bytes(4)) . '.' . $ext;
                move_uploaded_file($_FILES['image']['tmp_name'], UPLOAD_DIR . '/' . $image);
            }
        }

        if ($id > 0) {
            if ($image) q("UPDATE products SET name=?,slug=?,description=?,price=?,stock=?,category_id=?,active=?,image=? WHERE id=?",
                          [$name,$slug,$desc,$price,$stock,$cat,$active,$image,$id]);
            else       q("UPDATE products SET name=?,slug=?,description=?,price=?,stock=?,category_id=?,active=? WHERE id=?",
                          [$name,$slug,$desc,$price,$stock,$cat,$active,$id]);
        } else {
            q("INSERT INTO products (name,slug,description,price,stock,category_id,active,image) VALUES (?,?,?,?,?,?,?,?)",
              [$name,$slug,$desc,$price,$stock,$cat,$active,$image]);
        }
        $msg = 'Saved.';
    } elseif ($act === 'delete') {
        q("DELETE FROM products WHERE id=?", [(int)$_POST['id']]);
        $msg = 'Deleted.';
    }
}

$edit = null;
if (!empty($_GET['edit'])) {
    $edit = q("SELECT * FROM products WHERE id=?", [(int)$_GET['edit']])->fetch();
}
$list = q("SELECT p.*, c.name cname FROM products p LEFT JOIN categories c ON c.id=p.category_id ORDER BY p.id DESC")->fetchAll();
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Products · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Products</h1>
    <?php if ($msg): ?><div class="ok"><?= e($msg) ?></div><?php endif; ?>

    <form method="post" enctype="multipart/form-data" class="form-card">
      <input type="hidden" name="act" value="save">
      <input type="hidden" name="id" value="<?= (int)($edit['id'] ?? 0) ?>">
      <h2><?= $edit ? 'Edit product' : 'New product' ?></h2>
      <label>Name<input name="name" required value="<?= e($edit['name'] ?? '') ?>"></label>
      <label>Description<textarea name="description" rows="4"><?= e($edit['description'] ?? '') ?></textarea></label>
      <div class="row2">
        <label>Price<input name="price" type="number" step="0.01" required value="<?= e($edit['price'] ?? '') ?>"></label>
        <label>Stock<input name="stock" type="number" value="<?= e($edit['stock'] ?? 0) ?>"></label>
      </div>
      <label>Category
        <select name="category_id">
          <option value="">—</option>
          <?php foreach ($cats as $c): ?>
            <option value="<?= (int)$c['id'] ?>" <?= ($edit['category_id'] ?? 0) == $c['id'] ? 'selected' : '' ?>><?= e($c['name']) ?></option>
          <?php endforeach; ?>
        </select>
      </label>
      <label>Image<input type="file" name="image" accept="image/*"></label>
      <label class="chk"><input type="checkbox" name="active" <?= (!$edit || $edit['active']) ? 'checked' : '' ?>> Active</label>
      <button class="btn primary">Save</button>
      <?php if ($edit): ?><a class="btn" href="products.php">Cancel</a><?php endif; ?>
    </form>

    <table class="table">
      <thead><tr><th>#</th><th>Name</th><th>Price</th><th>Stock</th><th>Active</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($list as $r): ?>
        <tr>
          <td><?= (int)$r['id'] ?></td>
          <td><?= e($r['name']) ?> <small class="muted"><?= e($r['cname'] ?? '') ?></small></td>
          <td><?= money((float)$r['price']) ?></td>
          <td><?= (int)$r['stock'] ?></td>
          <td><?= $r['active'] ? 'Yes' : 'No' ?></td>
          <td>
            <a class="btn sm" href="products.php?edit=<?= (int)$r['id'] ?>">Edit</a>
            <form method="post" style="display:inline" onsubmit="return confirm('Delete this product?')">
              <input type="hidden" name="act" value="delete">
              <input type="hidden" name="id" value="<?= (int)$r['id'] ?>">
              <button class="btn sm danger">Delete</button>
            </form>
          </td>
        </tr>
      <?php endforeach; ?>
      </tbody>
    </table>
  </main>
</div>
</body></html>