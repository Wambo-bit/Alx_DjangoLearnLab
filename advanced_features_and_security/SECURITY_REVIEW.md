# Security Review

The following measures were implemented:

- **HTTPS Enforcement**
  - `SECURE_SSL_REDIRECT` forces HTTPS.
  - `SECURE_HSTS_*` ensures browsers always use HTTPS.

- **Secure Cookies**
  - `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` restrict cookies to HTTPS only.

- **Clickjacking Protection**
  - `X_FRAME_OPTIONS = "DENY"` prevents site from being embedded in iframes.

- **XSS & MIME Protection**
  - `SECURE_BROWSER_XSS_FILTER` and `SECURE_CONTENT_TYPE_NOSNIFF` enabled.

## Improvements for Production
- Add real SSL/TLS certificates via Let's Encrypt or another CA.
- Regularly audit dependencies (`pip-audit`).
- Enable Content Security Policy (CSP) to further mitigate XSS risks.

