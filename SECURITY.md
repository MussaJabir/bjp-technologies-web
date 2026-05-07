# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| Production (`main` branch) | ✅ |
| Development (`develop` branch) | ⚠️ Best effort |

---

## Reporting a Vulnerability

BJP Technologies (T) Limited takes security seriously. If you discover a vulnerability in this project — or in the live site at [bjptechnologies.co.tz](https://bjptechnologies.co.tz) — please report it responsibly.

### How to Report

**Do not open a public GitHub issue for security vulnerabilities.**

Email us directly at **[info@bjptechnologies.co.tz](mailto:info@bjptechnologies.co.tz)** with the subject line:

```
[SECURITY] Vulnerability Report — bjp-technologies-web
```

Please include:
- A clear description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Any proof-of-concept code (if applicable)

### What to Expect

| Timeline | Action |
|---|---|
| Within 48 hours | Acknowledgement of your report |
| Within 7 days | Initial assessment and severity classification |
| Within 30 days | Patch developed and deployed (critical issues prioritised) |
| After fix | Coordinated disclosure (credit given where appropriate) |

We will keep you informed throughout the process and will not take legal action against researchers who follow this responsible disclosure policy.

---

## Scope

### In Scope
- The live website at `bjptechnologies.co.tz`
- The Django application codebase in this repository
- Authentication and session handling
- Contact form and data handling
- Admin panel access controls

### Out of Scope
- Denial of Service (DoS/DDoS) attacks
- Social engineering attacks targeting our staff
- Physical security
- Third-party services (Google Maps, CDNs)
- Issues in dependencies that have an available upstream fix

---

## Security Practices

This project follows these security practices:

- `DEBUG = False` enforced in production
- `ALLOWED_HOSTS` restricted to known domains
- HTTPS enforced via `SECURE_SSL_REDIRECT`
- HSTS enabled (`Strict-Transport-Security`)
- CSRF protection on all forms
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- Content Security Policy (CSP) headers
- No secrets committed to version control (`.env` gitignored)
- Dependency auditing via `pip-audit`

---

*BJP Technologies (T) Limited — Secure Technology. Scalable Growth.*
