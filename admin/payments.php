<?php
require_once __DIR__ . '/_auth.php';
admin_require();

$msg = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $act = $_POST['act'] ?? '';
    if ($act === 'save') {
        $id = (int)($_POST['id'] ?? 0);
        $name = trim($_POST['name'] ?? '');
        $desc = trim($_POST['description'] ?? '');
        $enabled = isset($_POST['enabled']) ? 1 : 0;
        $mode = ($_POST['mode'] ?? 'sandbox') === 'live' ? 'live' : 'sandbox';
        $sort = (int)($_POST['sort_order'] ?? 0);

        // Config JSON from dynamic fields (prefix cfg_)
        $cfg = [];
        foreach ($_POST as $k => $v) {
            if (strpos($k, 'cfg_') === 0) {
                $cfg[substr($k, 4)] = is_string($v) ? trim($v) : $v;
            }
        }
        $cfgJson = json_encode($cfg);

        if ($id > 0) {
            q("UPDATE payment_gateways SET name=?,description=?,enabled=?,mode=?,config=?,sort_order=? WHERE id=?",
              [$name,$desc,$enabled,$mode,$cfgJson,$sort,$id]);
        } else {
            $code = preg_replace('/[^a-z0-9_]/', '', strtolower($_POST['code'] ?? ''));
            if ($code === '') { $msg = 'Code required'; }
            else {
                q("INSERT INTO payment_gateways (code,name,description,enabled,mode,config,sort_order) VALUES (?,?,?,?,?,?,?)",
                  [$code,$name,$desc,$enabled,$mode,$cfgJson,$sort]);
            }
        }
        $msg = 'Saved.';
    } elseif ($act === 'delete') {
        q("DELETE FROM payment_gateways WHERE id=?", [(int)$_POST['id']]);
        $msg = 'Deleted.';
    }
}

$edit = null;
if (!empty($_GET['edit'])) {
    $edit = q("SELECT * FROM payment_gateways WHERE id=?", [(int)$_GET['edit']])->fetch();
}
$list = q("SELECT * FROM payment_gateways ORDER BY sort_order, id")->fetchAll();

// Preset config fields per known gateway
function fields_for(string $code): array {
    switch ($code) {
        case 'razorpay':   return [['key_id','Key ID'], ['key_secret','Key Secret']];
        case 'cashfree':   return [['app_id','App ID'], ['secret_key','Secret Key']];
        case 'upi_manual': return [['upi_id','UPI ID'], ['payee_name','Payee Name']];
        case 'crypto':     return [['wallet_btc','BTC Wallet'], ['wallet_eth','ETH Wallet'], ['wallet_usdt','USDT TRC20']];
        default:           return [['key','Key'], ['secret','Secret']];
    }
}
?>
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Payment Gateways · Admin</title><link rel="stylesheet" href="<?= SITE_URL ?>/assets/style.css"></head><body>
<div class="admin-shell">
  <?php require __DIR__ . '/_nav.php'; ?>
  <main class="admin-main">
    <h1>Payment Gateways</h1>
    <?php if ($msg): ?><div class="ok"><?= e($msg) ?></div><?php endif; ?>

    <form method="post" class="form-card">
      <input type="hidden" name="act" value="save">
      <input type="hidden" name="id" value="<?= (int)($edit['id'] ?? 0) ?>">
      <h2><?= $edit ? 'Edit gateway' : 'Add gateway' ?></h2>

      <?php if (!$edit): ?>
        <label>Code (a-z, 0-9, _)<input name="code" required pattern="[a-z0-9_]+"></label>
      <?php else: ?>
        <p class="mono">Code: <b><?= e($edit['code']) ?></b></p>
      <?php endif; ?>

      <label>Display name<input name="name" required value="<?= e($edit['name'] ?? '') ?>"></label>
      <label>Description<input name="description" value="<?= e($edit['description'] ?? '') ?>"></label>

      <div class="row2">
        <label>Mode
          <select name="mode">
            <option value="sandbox" <?= ($edit['mode']??'sandbox')==='sandbox'?'selected':'' ?>>Sandbox</option>
            <option value="live" <?= ($edit['mode']??'')==='live'?'selected':'' ?>>Live</option>
          </select>
        </label>
        <label>Sort order<input name="sort_order" type="number" value="<?= (int)($edit['sort_order'] ?? 0) ?>"></label>
      </div>

      <label class="chk"><input type="checkbox" name="enabled" <?= ($edit['enabled']??0) ? 'checked' : '' ?>> Enabled</label>

      <h3>Config</h3>
      <?php
      $fields = fields_for($edit['code'] ?? 'generic');
      $cfg = $edit ? json_decode($edit['config'] ?? '{}', true) : [];
      foreach ($fields as $f):
      ?>
        <label><?= e($f[1]) ?><input name="cfg_<?= e($f[0]) ?>" value="<?= e($cfg[$f[0]] ?? '') ?>"></label>
      <?php endforeach; ?>

      <button class="btn primary">Save</button>
      <?php if ($edit): ?><a class="btn" href="payments.php">Cancel</a><?php endif; ?>
    </form>

    <table class="table">
      <thead><tr><th>#</th><th>Code</th><th>Name</th><th>Mode</th><th>Enabled</th><th>Sort</th><th></th></tr></thead>
      <tbody>
      <?php foreach ($list as $r): ?>
        <tr>
          <td><?= (int)$r['id'] ?></td>
          <td class="mono"><?= e($r['code']) ?></td>
          <td><?= e($r['name']) ?></td>
          <td><?= e($r['mode']) ?></td>
          <td><?= $r['enabled'] ? 'Yes' : 'No' ?></td>
          <td><?= (int)$r['sort_order'] ?></td>
          <td>
            <a class="btn sm" href="payments.php?edit=<?= (int)$r['id'] ?>">Edit</a>
            <form method="post" style="display:inline" onsubmit="return confirm('Delete this gateway?')">
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