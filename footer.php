</main>

<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <h4>About <?= e($siteName) ?></h4>
      <ul>
        <li><a href="<?= SITE_URL ?>/page.php?slug=about">About Us</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=careers">Careers</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=press">Press</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=blog">Blog</a></li>
      </ul>
    </div>
    <div>
      <h4>Customer Service</h4>
      <ul>
        <li><a href="<?= SITE_URL ?>/page.php?slug=help">Help Center</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=returns">Returns</a></li>
        <li><a href="<?= SITE_URL ?>/track-order.php">Track Order</a></li>
        <li><a href="<?= SITE_URL ?>/contact.php">Contact Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Policy</h4>
      <ul>
        <li><a href="<?= SITE_URL ?>/page.php?slug=privacy">Privacy Policy</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=terms">Terms of Use</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=return-policy">Return Policy</a></li>
        <li><a href="<?= SITE_URL ?>/page.php?slug=security">Security</a></li>
      </ul>
    </div>
    <div>
      <h4>Connect With Us</h4>
      <ul>
        <li><a href="#" rel="noopener">Facebook</a></li>
        <li><a href="#" rel="noopener">Twitter</a></li>
        <li><a href="#" rel="noopener">Instagram</a></li>
        <li><a href="#" rel="noopener">YouTube</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <?= e(setting('footer_note', '© 2024 SmartStore. All rights reserved.')) ?>
  </div>
</footer>

</body>
</html>