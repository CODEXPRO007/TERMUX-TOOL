<?php
declare(strict_types=1);

function e(?string $s): string { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }

function setting(string $k, string $default = ''): string {
    static $cache = null;
    if ($cache === null) {
        $cache = [];
        foreach (q("SELECT k,v FROM settings")->fetchAll() as $r) $cache[$r['k']] = $r['v'];
    }
    return $cache[$k] ?? $default;
}

function money(float $n): string {
    return setting('currency_symbol', '₹') . number_format($n, 2);
}

function slugify(string $s): string {
    $s = preg_replace('~[^\pL\d]+~u', '-', $s);
    $s = trim(iconv('UTF-8', 'ASCII//TRANSLIT', $s) ?: $s, '-');
    $s = strtolower(preg_replace('~[^-\w]+~', '', $s));
    return $s ?: 'item-' . substr(md5((string)microtime(true)), 0, 6);
}

function order_no(): string {
    return 'SS-' . date('ymd') . '-' . strtoupper(substr(bin2hex(random_bytes(3)), 0, 6));
}

function cart(): array {
    if (!isset($_SESSION['cart']) || !is_array($_SESSION['cart'])) $_SESSION['cart'] = [];
    return $_SESSION['cart'];
}

function cart_set(array $c): void { $_SESSION['cart'] = $c; }

function cart_add(int $pid, int $qty = 1): void {
    $c = cart();
    $c[$pid] = ($c[$pid] ?? 0) + max(1, $qty);
    cart_set($c);
}

function cart_remove(int $pid): void {
    $c = cart(); unset($c[$pid]); cart_set($c);
}

function cart_update(int $pid, int $qty): void {
    $c = cart();
    if ($qty <= 0) unset($c[$pid]); else $c[$pid] = min($qty, 99);
    cart_set($c);
}

function cart_items(): array {
    $c = cart();
    if (!$c) return ['items' => [], 'subtotal' => 0.0, 'shipping' => 0.0, 'total' => 0.0];
    $ids = array_keys($c);
    $in  = implode(',', array_fill(0, count($ids), '?'));
    $rows = q("SELECT * FROM products WHERE id IN ($in) AND active=1", $ids)->fetchAll();
    $items = []; $sub = 0.0;
    foreach ($rows as $r) {
        $qty = (int)$c[$r['id']];
        $line = $qty * (float)$r['price'];
        $sub += $line;
        $items[] = ['product' => $r, 'qty' => $qty, 'line' => $line];
    }
    $ship = 0.0;
    $flat = (float)setting('shipping_flat', '99');
    $freeAbove = (float)setting('free_shipping_above', '2000');
    if ($sub > 0 && $sub < $freeAbove) $ship = $flat;
    return ['items' => $items, 'subtotal' => $sub, 'shipping' => $ship, 'total' => $sub + $ship];
}

function redirect(string $url): void { header('Location: ' . $url); exit; }

function csrf_token(): string {
    if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(16));
    return $_SESSION['csrf'];
}

function csrf_check(?string $t): bool {
    return !empty($_SESSION['csrf']) && is_string($t) && hash_equals($_SESSION['csrf'], $t);
}

function flash(?string $msg = null, string $type = 'info') {
    if ($msg !== null) { $_SESSION['flash'] = ['msg' => $msg, 'type' => $type]; return null; }
    $f = $_SESSION['flash'] ?? null; unset($_SESSION['flash']); return $f;
}