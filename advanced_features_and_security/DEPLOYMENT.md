# Deployment & HTTPS Configuration

This project is configured with HTTPS and secure redirect settings in `settings.py`.

## Local Development
- `DEBUG = True` disables HTTPS redirect so the Django dev server runs without SSL.
- Cookies and HSTS are not enforced locally.

## Production Deployment
1. Set `DEBUG = False` in `settings.py`.
2. Configure `ALLOWED_HOSTS` with your domain name.
3. Deploy behind a web server (e.g., Nginx/Apache) with SSL/TLS enabled.
4. Install a valid SSL certificate (e.g., via Certbot with Let's Encrypt).
5. Django will automatically:
   - Redirect HTTP → HTTPS (`SECURE_SSL_REDIRECT`).
   - Enforce HSTS (`SECURE_HSTS_SECONDS`).
   - Secure cookies with HTTPS only (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
   - Add security headers (`X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, etc.).

## Testing
- Verified headers using browser developer tools.
- Verified that insecure cookies are not sent over HTTP.

