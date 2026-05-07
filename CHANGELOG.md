# Changelog

All notable changes to this project are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### In Progress
- Page load speed optimisation (target: <3s)
- Image optimisation
- Final security audit
- Go-live sign-off

---

## [0.6.0] — 2026-05 — Phase 6: Polish & Launch

### Added
- `django.contrib.sitemaps` — auto-generated sitemap at `/sitemap.xml` covering all pages, services, and industries
- `robots.txt` served via Django `TemplateView` — blocks `/admin/`, includes sitemap URL
- Content Security Policy (CSP) middleware — restricts script/style/font/image sources in production
- Per-page Open Graph tags (`og:title`, `og:description`, `og:url`) on all 7 page templates
- Dynamic content system — all website copy editable from Django admin with no developer involvement:
  - `SiteSettings` singleton model with 40+ editable fields
  - 11 proxy model admin sections under a collapsible "Site Settings" sidebar group
  - About page: banner, counters, intro and body texts
  - Services / Industries pages: banner headline and subtext
  - Contact page: Google Maps embed URL
  - Footer CTA: headline, body, button text
- GitHub repository polish: `README.md`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, PR template, issue templates, `CHANGELOG.md`

### Fixed
- Alpine.js admin broken — added `'unsafe-eval'` to CSP `script-src` (Alpine uses `new AsyncFunction()`)
- Font Awesome icons invisible sitewide — added Luminos CDN domain and `data:` to CSP `font-src`
- About page services grid hardcoded — replaced 6 duplicate cards with dynamic `{% for service in services %}` loop
- Contact page info cards hardcoded — wired to `{{ company.address }}`, `{{ company.phone }}`, `{{ company.email }}`
- Services list page dead space (750px) — removed empty `large-image-area-bg-service-page` jarallax div

### Security
- HSTS, `X-Frame-Options: DENY`, `X-Content-Type-Options`, `Referrer-Policy` all confirmed active in production
- `DEBUG = False` enforced via environment variable
- Secure cookies (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`) active in production

---

## [0.5.0] — 2026-05 — Phase 5: Admin & CMS

### Added
- `django-unfold` — replaces Django's default admin with a branded, Tailwind-based UI
- Custom Unfold dashboard with live stats: services count, industries count, enquiry breakdown, recent 6 enquiries
- `SiteSettings` singleton model — company identity, address, social media URLs (foundation layer)
- Context processor `company_info` — passes `SiteSettings` as `{{ company }}` to all templates
- Dynamic footer — services, industries, social icons, company info all from database
- Services admin overhaul:
  - Edit/Delete action buttons in list view
  - Side-by-side field layout (name + tagline, order + active)
  - Slug and timestamps in collapsed "Advanced" section
  - Bulk activate/deactivate actions
- Industries admin — same improvements as services
- Contact enquiries admin:
  - All client fields readonly (status is the only editable field)
  - Auto-marks enquiry as "Read" when opened
  - Coloured status badges (red=New, blue=Read, green=Replied)
  - Bulk actions: mark read / unread / replied
  - No "Add" button (enquiries come from the website only)
- Unfold navigation sidebar with custom groups: Dashboard, Website Content, Site Settings, Enquiries, Administration

### Fixed
- `changelist_view` redirect for `SiteSettings` — admin users land directly on the edit form

---

## [0.4.0] — 2026-04 — Phase 4: Contact System

### Added
- `apps/contact/` — `ContactEnquiry` model with 10 fields (name, email, phone, company, service, message, IP, status, timestamps)
- Contact form (`ModelForm`) with full validation
- Email notifications — on submission: alert to `info@bjptechnologies.co.tz` + confirmation to submitter
- Contact success page at `/contact/success/`
- Rate limiting on form submission (anti-spam)
- Contact enquiry admin with `list_display`, status filter, and search

---

## [0.3.0] — 2026-03 — Phase 3: Content Pages

### Added
- `apps/main/` — Home page and About page
- `apps/services/` — `Service` model, services list (`/services/`) and detail pages (`/services/<slug>/`)
- `apps/industries/` — `Industry` model, industries list (`/industries/`) and detail pages (`/industries/<slug>/`)
- All 7 IT service lines seeded via fixtures
- All 6 industry verticals seeded via fixtures
- Animated hero section with WOW.js scroll-reveal and floating particles
- Animated counters (counter-up.js) on home and about pages
- Jarallax parallax effects on page banners
- Full mobile responsiveness across all pages

---

## [0.2.0] — 2026-03 — Phase 2: Core Foundation

### Added
- `apps/core/` — base templates, context processor, utility functions
- `core/base.html` with all template blocks defined
- `core/navbar.html` — BJP branded, responsive mobile menu, scroll-effect
- `core/footer.html` — contact details, service/industry links, social icons
- BJP brand CSS system — CSS custom properties (navy, blue, cyan, white, grey palette)
- Google Fonts: Outfit, DM Serif Display, Space Mono
- `static/js/main.js` — scroll-to-top, navbar scroll effect, mobile menu
- BJP logo SVG and horizontal transparent PNG
- Global 404 and 500 error pages

---

## [0.1.0] — 2026-03 — Phase 1: Infrastructure & Hosting

### Added
- Django project scaffold with `config/settings/` (base, development, production, CI)
- `passenger_wsgi.py` — cPanel Phusion Passenger entry point
- MySQL database configuration with `utf8mb4` charset
- `requirements.txt` and `requirements-dev.txt`
- `.env.example` — environment variable template
- `.gitignore` — excludes `.env`, `__pycache__`, `public/`, `venv/`
- `pytest.ini` and `pyproject.toml` — ruff + black configuration
- GitHub Actions `deploy.yml` — test + deploy pipeline (SSH to cPanel on push to `main`)
- `SESSION_LOG.md` — persistent session tracking for AI-assisted development
- First successful automated deploy to `bjptechnologies.co.tz`

---

[Unreleased]: https://github.com/MussaJabir/bjp-technologies-web/compare/main...HEAD
[0.6.0]: https://github.com/MussaJabir/bjp-technologies-web/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/MussaJabir/bjp-technologies-web/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/MussaJabir/bjp-technologies-web/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/MussaJabir/bjp-technologies-web/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/MussaJabir/bjp-technologies-web/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/MussaJabir/bjp-technologies-web/releases/tag/v0.1.0
