<?php
require_once __DIR__ . '/_auth.php';
unset($_SESSION['admin_id']);
redirect(SITE_URL . '/admin/login.php');