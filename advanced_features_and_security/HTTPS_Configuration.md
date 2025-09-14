# HTTPS Configuration for Django Application

## Overview

This document outlines the configuration changes made to enhance security through HTTPS implementation in our Django application.

## Django Security Settings

The following security settings have been implemented in `settings.py`:

### HTTPS Redirect Configuration

- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP requests to HTTPS
- `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`: Properly handles HTTPS when behind a proxy
- `SECURE_HSTS_SECONDS = 31536000`: Sets HSTS policy for one year
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Includes all subdomains in HSTS policy
- `SECURE_HSTS_PRELOAD = True`: Allows preloading in browser HSTS lists

### Secure Cookie Configuration

- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only sent over HTTPS
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are only sent over HTTPS
- `SESSION_COOKIE_HTTPONLY = True`: Prevents JavaScript access to session cookies
- `CSRF_COOKIE_HTTPONLY = True`: Prevents JavaScript access to CSRF cookies

### Additional Security Headers

- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks by disallowing framing
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filtering
- `SECURE_REFERRER_POLICY = 'same-origin'`: Restricts referrer information to same origin

## Environment Variables

These settings can be configured through environment variables in `.env` file:

```
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
```

## Web Server Configuration for HTTPS

### Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect all HTTP requests to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL certificate configuration
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    # Strong SSL settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305';
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # HSTS header (already set in Django, but good to have here too)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # Django application configuration
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files
    location /static/ {
        alias /path/to/your/static/files/;
    }

    # Media files
    location /media/ {
        alias /path/to/your/media/files/;
    }
}
```

### Apache Configuration Example

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    # Redirect all HTTP traffic to HTTPS
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /path/to/certificate.crt
    SSLCertificateKeyFile /path/to/private.key

    # Modern SSL configuration
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLHonorCipherOrder on
    SSLCompression off
    SSLSessionTickets off

    # HSTS header
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"

    # Django application configuration
    WSGIDaemonProcess yourdomain python-path=/path/to/your/project
    WSGIProcessGroup yourdomain
    WSGIScriptAlias / /path/to/your/project/LibraryProject/wsgi.py

    <Directory /path/to/your/project/LibraryProject>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    # Static files
    Alias /static/ /path/to/your/static/files/
    <Directory /path/to/your/static/files/>
        Require all granted
    </Directory>

    # Media files
    Alias /media/ /path/to/your/media/files/
    <Directory /path/to/your/media/files/>
        Require all granted
    </Directory>
</VirtualHost>
```

## SSL Certificate Acquisition

For production environments, use a trusted certificate authority such as Let's Encrypt to obtain free SSL certificates.

### Let's Encrypt with Certbot

```bash
# For Nginx
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# For Apache
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d yourdomain.com -d www.yourdomain.com
```

## Security Review

### Implemented Security Measures

1. **HTTPS Enforcement**: All traffic is redirected to HTTPS, ensuring encrypted data transmission.
2. **HSTS Implementation**: Browsers are instructed to always use HTTPS, even for first-time visitors.
3. **Secure Cookies**: Session and CSRF cookies are only transmitted over secure connections.
4. **Protection Headers**: Headers are set to prevent clickjacking, content sniffing, and XSS attacks.
5. **Environment Variable Configuration**: Security settings can be easily configured via environment variables.

### Areas for Future Improvement

1. **Certificate Rotation**: Implement automated certificate renewal and rotation.
2. **Content Security Policy**: Consider implementing a more restrictive CSP.
3. **Security Monitoring**: Set up logging and monitoring for security-related events.
4. **Two-Factor Authentication**: Consider implementing 2FA for sensitive operations.
5. **Regular Security Audits**: Schedule regular security reviews and penetration testing.

## Development Considerations

For local development environments where HTTPS might not be configured:

1. Create a `settings_local.py` file with development-specific settings:
   ```python
   DEBUG = True
   ALLOWED_HOSTS = ['localhost', '127.0.0.1']
   SECURE_SSL_REDIRECT = False
   SESSION_COOKIE_SECURE = False
   CSRF_COOKIE_SECURE = False
   ```

2. In your main `settings.py`, add:
   ```python
   try:
       from .settings_local import *
   except ImportError:
       pass
   ```

This approach allows secure settings in production while maintaining a convenient development environment.
