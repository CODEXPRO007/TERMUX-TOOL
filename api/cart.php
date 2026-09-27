<?php
require_once __DIR__ . '/../config.php';
require_once __DIR__ . '/../includes/db.php';
require_once __DIR__ . '/../includes/functions.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { redirect(SITE_URL . '/'); }
if (!csrf_check($_POST['csrf'] ?? '')) { flash('Session expired', 'err'); redirect(SITE_URL . '/cart.php'); }

$act = $_POST['action'] ?? '';
$id  = (int)($_POST['id'] ?? 0);

if ($act === 'add' && $id > 0) {
    // confirm product exists
    $exists = q("SELECT id FROM products WHERE id=? AND active=1", [$id])->fetch();
    if ($exists) {
        $qty = max(1, (int)($_POST['qty'] ?? 1));
        cart_add($id, $qty);
        flash('Added to cart.', 'ok');
    } else {
        flash('Product unavailable.', 'err');
    }
} elseif ($act === 'remove' && $id > 0) {
    cart_remove($id); flash('Removed.', 'ok');
} elseif ($act === 'update' && $id > 0) {
    cart_update($id, (int)($_POST['qty'] ?? 0)); flash('Cart updated.', 'ok');
}

$back = $_SERVER['HTTP_REFERER'] ?? (SITE_URL . '/cart.php');
redirect($back);