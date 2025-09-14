# Security Measures for LibraryProject

This document outlines the security measures implemented in the `LibraryProject` Django application to protect against common vulnerabilities such as Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and SQL injection.

---

## 1. Django Settings

### Debugging
- **DEBUG = False**  
  Debug mode is disabled in production to prevent sensitive information from being exposed in error pages.

### Allowed Hosts
- **ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']**  
  Limits which hosts can serve the application, preventing HTTP Host header attacks.

### Browser Protections
- **SECURE_BROWSER_XSS_FILTER = True**  
  Enables the browser’s built-in XSS filter.
- **SECURE_CONTENT_TYPE_NOSNIFF = True**  
  Prevents the browser from interpreting files as a different MIME type.
- **X_FRAME_OPTIONS = 'DENY'**  
  Prevents clickjacking by disallowing the site to be loaded in an iframe.

### Cookies
- **CSRF_COOKIE_SECURE = True**  
  Ensures CSRF cookies are only sent over HTTPS.
- **SESSION_COOKIE_SECURE = True**  
  Ensures session cookies are only sent over HTTPS.

### HSTS (HTTP Strict Transport Security)
- **SECURE_HSTS_SECONDS = 3600**  
  Enforces HTTPS connections for 1 hour (extend for production).  
- **SECURE_HSTS_INCLUDE_SUBDOMAINS = True**  
  Applies HSTS policy to all subdomains.  
- **SECURE_HSTS_PRELOAD = True**  
  Allows inclusion in browser preload lists for stronger HTTPS enforcement.

---

## 2. CSRF Protection

- All forms include `{% csrf_token %}` in templates.  
- Django automatically validates CSRF tokens on POST requests.  
- Example: `form_example.html` includes `{% csrf_token %}` to prevent CSRF attacks.

---

## 3. Input Validation & ORM Usage

- **BookForm (ModelForm)** validates and sanitizes user input before saving.  
- Views use **Django ORM filters (`.filter`, `.get`, `.create`)** instead of raw SQL queries.  
- This ensures protection against **SQL injection attacks**.  

Example (safe search):
```python
results = Book.objects.filter(
    Q(title__icontains=query) | Q(author__icontains=query)
)
