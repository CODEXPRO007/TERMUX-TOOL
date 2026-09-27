<?php
$page = 'contact'; $pageTitle = 'Contact Us';
require __DIR__ . '/header.php';

$sent = false;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_check($_POST['csrf'] ?? '')) {
        flash('Session expired.', 'err');
    } else {
        $name = trim($_POST['name'] ?? '');
        $email= trim($_POST['email'] ?? '');
        $msg  = trim($_POST['message'] ?? '');
        if ($name && $email && $msg) {
            @mail(setting('contact_email', 'support@smartstore.local'),
                  "Contact from $name",
                  "From: $email\n\n$msg",
                  "From: $email");
            $sent = true;
        } else {
            flash('All fields required.', 'err');
        }
    }
}
?>

<div class="wrap contact">
  <h1 class="pagetitle">Contact Us</h1>

  <div class="contact-grid">
    <div class="contact-info">
      <h3>Business details</h3>
      <p class="mono">
        Legal name: <b><?= e(setting('site_name')) ?></b><br>
        Email: <b><?= e(setting('contact_email')) ?></b><br>
        Phone: <b><?= e(setting('contact_phone')) ?></b><br>
        Address: <b>Registered business address</b>
      </p>
      <p>For order issues, include your order number. We reply within 24–48 hours on business days.</p>
    </div>

    <form method="post" class="contact-form">
      <input type="hidden" name="csrf" value="<?= csrf_token() ?>">
      <?php if ($sent): ?><div class="ok">Thanks — we received your message.</div><?php endif; ?>
      <label>Name<input name="name" required></label>
      <label>Email<input type="email" name="email" required></label>
      <label>Message<textarea name="message" rows="5" required></textarea></label>
      <button class="btn primary">Send message</button>
    </form>
  </div>

  <section class="verify">
    <h2>Razorpay merchant verification</h2>
    <p>This page is publicly reachable so Razorpay's underwriting team can verify our business contact details and refund/return policy. Refund and cancellation policy are linked in the footer.</p>
    <ul>
      <li>Business contact email: <b><?= e(setting('contact_email')) ?></b></li>
      <li>Business contact phone: <b><?= e(setting('contact_phone')) ?></b></li>
      <li>Refund policy: <a href="<?= SITE_URL ?>/page.php?slug=return-policy">Return Policy</a></li>
      <li>Terms: <a href="<?= SITE_URL ?>/page.php?slug=terms">Terms of Use</a></li>
      <li>Privacy: <a href="<?= SITE_URL ?>/page.php?slug=privacy">Privacy Policy</a></li>
    </ul>
  </section>
</div>

<?php require __DIR__ . '/footer.php'; ?>