# BJP Technologies (T) Limited — Corporate Website

[![CI](https://github.com/MussaJabir/bjp-technologies-web/actions/workflows/deploy.yml/badge.svg)](https://github.com/MussaJabir/bjp-technologies-web/actions/workflows/deploy.yml)
[![Python](https://img.shields.io/badge/python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-6.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/mysql-8.0-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: ruff](https://img.shields.io/badge/linting-ruff-FCC21B?logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff)
[![License: Proprietary](https://img.shields.io/badge/license-proprietary-red.svg)](#license)

**Live site:** [bjptechnologies.co.tz](https://bjptechnologies.co.tz)

Professional corporate website and service platform for BJP Technologies (T) Limited — Tanzania's trusted IT partner delivering secure, scalable technology solutions to businesses across East Africa.

---

## Features

- **Dynamic content management** — all website content editable from Django admin with no developer involvement
- **Service & industry showcase** — 7 IT service lines and 6 industry verticals, fully managed from admin
- **Contact enquiry system** — form submissions saved to database, email notifications sent on receipt
- **Admin dashboard** — Unfold-powered admin with live stats, recent enquiries, and per-section site settings
- **SEO ready** — sitemap, robots.txt, per-page Open Graph tags, structured meta descriptions
- **Security hardened** — HSTS, CSP headers, CSRF protection, X-Frame-Options, secure cookies
- **Automated deployment** — GitHub Actions CI/CD pipeline deploys to cPanel on push to `main`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Django 6.x |
| Database | MySQL 8 / MariaDB (`utf8mb4`) |
| Admin UI | django-unfold |
| Static files | WhiteNoise + collectstatic |
| CSS | Bootstrap 5 + BJP brand variables |
| JS | Vanilla JS (WOW.js, counter-up, jarallax) |
| Server | cPanel + Phusion Passenger (WSGI) |
| CI/CD | GitHub Actions |

---

## Project Structure

```
bjp-technologies-web/
├── apps/
│   ├── core/          # Base templates, SiteSettings, context processors, middleware
│   ├── main/          # Home and About pages
│   ├── services/      # Service model, list and detail pages
│   ├── industries/    # Industry model, list and detail pages
│   └── contact/       # ContactEnquiry model, form, email notifications
├── config/
│   └── settings/
│       ├── base.py        # Shared settings
│       ├── development.py # Local overrides
│       └── production.py  # Production settings
├── static/            # CSS, JS, images
├── templates/         # Global templates (404, 500, robots.txt)
├── docs/              # Deployment and database documentation
└── passenger_wsgi.py  # cPanel Passenger entry point
```

---

## Local Setup

### Prerequisites
- Python 3.11+
- MySQL 8 or MariaDB
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/MussaJabir/bjp-technologies-web.git
cd bjp-technologies-web

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt -r requirements-dev.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your local database credentials and secret key

# 5. Create the database
mysql -u root -p -e "CREATE DATABASE bjp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 6. Run migrations
python manage.py migrate

# 7. Load initial data (services and industries)
python manage.py loaddata apps/services/fixtures/services.json
python manage.py loaddata apps/industries/fixtures/industries.json

# 8. Create a superuser
python manage.py createsuperuser

# 9. Collect static files
python manage.py collectstatic

# 10. Start the development server
python manage.py runserver
```

Visit `http://localhost:8000` for the site and `http://localhost:8000/admin/` for the admin panel.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your values:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `DEBUG` | Debug mode (`True` for dev, `False` for prod) | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `bjptechnologies.co.tz` |
| `DB_NAME` | Database name | `bjp_db` |
| `DB_USER` | Database user | `bjp_user` |
| `DB_PASS` | Database password | `your-password` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `3306` |
| `EMAIL_HOST` | SMTP host | `smtp.gmail.com` |
| `EMAIL_HOST_USER` | SMTP username | `info@bjptechnologies.co.tz` |
| `EMAIL_HOST_PASSWORD` | SMTP app password | `your-app-password` |
| `CONTACT_EMAIL` | Enquiry recipient address | `info@bjptechnologies.co.tz` |

---

## Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific app
pytest apps/contact/

# Run with coverage report
pytest --cov=apps --cov-report=term-missing
```

---

## Code Quality

```bash
# Lint
ruff check .

# Format
black .

# Format check only (CI mode)
black --check .
```

Both `ruff` and `black` are enforced in CI — PRs that fail linting will not be merged.

---

## Content Management

All website content is editable from the Django admin panel (`/admin/`) under **Site Settings**:

| Section | What you can edit |
|---|---|
| Company Identity | Name, tagline, email, phone |
| Address | Office address, postal, domain |
| Social Media | Facebook, Twitter, LinkedIn, YouTube URLs |
| Hero Section | Home page banner headline, subtext, CTA buttons |
| Stats Counters | Home page animated counters (4 pairs) |
| About Strip | Home page "Who We Are" section |
| About Page | Banner, counters, intro and body text |
| Services Page | Banner headline and subtext |
| Industries Page | Banner headline and subtext |
| Contact Page | Google Maps embed URL |
| Footer CTA | Call-to-action banner above footer |

Services and industries are also fully managed from admin — name, description, icon, order, active status.

---

## Deployment

Deployment is automated via GitHub Actions on push to `main`. The pipeline:
1. Runs `ruff check .` and `black --check .`
2. Runs `pytest` against a MySQL test database
3. SSH deploys to cPanel — pulls, installs requirements, migrates, collects static, restarts Passenger

See [`docs/deployment.md`](docs/deployment.md) for manual deployment steps and cPanel configuration details.

---

## Branching Workflow

```
main      ← production only, protected
develop   ← integration branch
feature/* ← new features
fix/*     ← bug fixes
hotfix/*  ← emergency production fixes
chore/*   ← non-code changes
docs/*    ← documentation
```

All PRs target `develop` first. `develop → main` requires a review. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for full workflow.

---

## Security

To report a security vulnerability, please follow the process in [`SECURITY.md`](SECURITY.md). Do not open a public GitHub issue for security concerns.

---

## License

Copyright © 2024–2026 BJP Technologies (T) Limited. All rights reserved.

This codebase is proprietary. Unauthorised copying, modification, distribution, or use of this software, in whole or in part, is strictly prohibited without written permission from BJP Technologies (T) Limited.

Contact: [info@bjptechnologies.co.tz](mailto:info@bjptechnologies.co.tz)
