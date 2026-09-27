<?php
require_once __DIR__ . '/../config.php';
require_once __DIR__ . '/../includes/db.php';
require_once __DIR__ . '/../includes/functions.php';

function admin_user(): ?array {
    if (empty($_SESSION['admin_id'])) return null;
    $u = q("SELECT * FROM users WHERE id=? AND role='admin' LIMIT 1", [$_SESSION['admin_id']])->fetch();
    return $u ?: null;
}

function admin_require(): array {
    $u = admin_user();
    if (!$u) { redirect(SITE_URL . '/admin/login.php'); }
    return $u;
}