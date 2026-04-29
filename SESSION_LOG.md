# SESSION_LOG.md — BJP Technologies (T) Limited
# technologies.bejundas.co.tz

> This file is updated by Claude Code at the end of every working session.
> It is the single source of truth for project progress, decisions, and context.
> Never delete entries. Always append new entries at the bottom.
> Committed to git at the end of every session.

---

## Project Summary

**Repo:** bjp-technologies-web
**Domain:** bjptechnologies.co.tz (primary)
**Stack:** Django 6 + MySQL + cPanel + GitHub Actions
**Current Phase:** Phase 2 — Core Foundation
**Started:** April 2026

## Phase Progress

| Phase | Name | Status |
|---|---|---|
| Phase 1 | Infrastructure & Hosting | ✅ Complete |
| Phase 2 | Core Foundation | 🔄 Current |
| Phase 3 | Content Pages | ⏳ Pending |
| Phase 4 | Contact System | ⏳ Pending |
| Phase 5 | Admin & CMS | ⏳ Pending |
| Phase 6 | Polish & Launch | ⏳ Pending |

---

## Session 1 — [DATE] [TIME EAT]

**Goal:** Project planning — CLAUDE.md, skills, agents, phases, and session tracker created.
**Branch:** N/A (pre-repo setup session)
**Status:** ✅ Complete

### What Was Done
- Discussed project architecture: Django + MySQL + cPanel + GitHub Actions
- Confirmed domain: technologies.bejundas.co.tz (Bejundas Technologies subdomain)
- Confirmed database: MySQL (PostgreSQL not supported on cPanel)
- Designed GitHub CI/CD pipeline via SSH + appleboy/ssh-action
- Created full CLAUDE.md with 22 sections
- Created 5 skill files in `.claude/skills/`
- Created 6 agent definitions in `.claude/agents/agents.md`
- Created SESSION_LOG.md (this file)
- Designed 6-phase delivery plan
- Built HTML/CSS/JS website template (BJP brand, navy/cyan colors)

### Files Created
| File | Action | Notes |
|---|---|---|
| CLAUDE.md | Created | 22-section master instructions |
| .claude/skills/git-branch-workflow.md | Created | Branch naming, commits, PR rules |
| .claude/skills/django-models.md | Created | BaseModel, conventions, examples |
| .claude/skills/django-views.md | Created | CBV/FBV, URLs, context processors |
| .claude/skills/frontend-templates.md | Created | BJP brand, blocks, static files |
| .claude/skills/testing-migrations-deploy-security.md | Created | Testing, migrations, deploy, security |
| .claude/agents/agents.md | Created | 6 agent definitions |
| SESSION_LOG.md | Created | This file |

### Decisions Made
- **Decision:** Use MySQL over PostgreSQL
  **Reason:** cPanel does not support PostgreSQL natively. MySQL is the standard.
- **Decision:** Domain is technologies.bejundas.co.tz not bjptechnologies.co.tz
  **Reason:** BJP Technologies is the Technologies vertical of the Bejundas platform.
- **Decision:** Each Bejundas subdomain gets its own repo and CLAUDE.md
  **Reason:** Independent deployments, no cross-contamination risk between verticals.
- **Decision:** Branch-based development (never commit to main directly)
  **Reason:** Same workflow used successfully in HMS project. CI/CD enforces this.
- **Decision:** 6-phase delivery starting with infrastructure before any frontend
  **Reason:** Get the deploy pipeline working first so every subsequent session can see results live immediately.

### Blockers / Issues
- None at this stage — planning phase only.

### Next Session Should
- [ ] Create GitHub repo `bjp-technologies-web` (private)
- [ ] Set branch protection rules on `main` and `develop`
- [ ] Scaffold Django project locally with `config/settings/` structure
- [ ] Create `passenger_wsgi.py`
- [ ] Create `requirements.txt` and `.env.example`
- [ ] Push initial commit to GitHub
- [ ] Create MySQL database in cPanel (bjp_db, bjp_user)
- [ ] Configure cPanel Python App (Python 3.11, Passenger)
- [ ] Set up GitHub Actions deploy.yml
- [ ] Confirm first successful deploy to technologies.bejundas.co.tz

---

---

## Session 3 — 2026-04-29 EAT

**Goal:** Update CLAUDE.md with correct primary domain and confirm Django 6.x as framework version.
**Branch:** develop
**Status:** ✅ Complete
**Phase:** Phase 1 — Infrastructure & Hosting

### What Was Done
- Updated Section 1 (Project Identity): added primary domain `bjptechnologies.co.tz` and noted `technologies.bejundas.co.tz` as a 301 redirect alias on a separate cPanel — not the Django host
- Updated Section 2 (Tech Stack): confirmed Django 6.x (was already updated; no change needed)
- Updated Section 9 (Environment Variables): changed `ALLOWED_HOSTS` in `.env.example` to `bjptechnologies.co.tz,www.bjptechnologies.co.tz`
- Updated Section 11 (Security Rules): added explicit `ALLOWED_HOSTS` production values with comment excluding the redirect alias
- Updated Section 22 footer: changed domain reference to `bjptechnologies.co.tz (primary)`
- Updated Phase 1 deliverables: added ALLOWED_HOSTS confirmation checklist item

### Files Changed
| File | Action | Notes |
|---|---|---|
| CLAUDE.md | Modified | 6 targeted changes — domain, ALLOWED_HOSTS, security, footer, phase checklist |
| SESSION_LOG.md | Modified | This entry |

### Migrations
- N/A

### Tests
- N/A

### Decisions Made
- **Decision:** `bjptechnologies.co.tz` is the primary Django-hosted domain.
  **Reason:** The site has its own dedicated domain. `technologies.bejundas.co.tz` is a 301 redirect alias configured on a separate cPanel account — Django never receives requests on that hostname so it must not appear in `ALLOWED_HOSTS`.
- **Decision:** Django 6.x confirmed as the framework version.
  **Reason:** Django 6.0.4 is available on PyPI and Python 3.12.3 is installed locally, which satisfies Django 6's minimum Python version requirement.

### Blockers / Issues
- Waiting for MySQL database (`bjp_db`, `bjp_user`) to be created in cPanel before proceeding with Phase 1.

### Next Session Should
- [ ] Confirm MySQL database created in cPanel (bjp_db / bjp_user) and note cPanel-prefixed names
- [ ] Configure cPanel Python App (Python 3.12, Passenger, app root)
- [ ] Create SSH deploy key and add to GitHub repo deploy keys
- [ ] Set CPANEL_HOST, CPANEL_USER, CPANEL_PASS secrets in GitHub repo
- [ ] Push develop → main and confirm first auto-deploy

---

---

## Session 4 — 2026-04-30 EAT

**Goal:** Complete Phase 1 — scaffold Django project, connect to GitHub, deploy to cPanel, confirm site live.
**Branch:** develop → merged to main
**Status:** ✅ Complete
**Phase:** Phase 1 — Infrastructure & Hosting

### What Was Done
- Created GitHub repo `bjp-technologies-web` (private) — manual creation by developer, cloned via cPanel Git Version Control
- Created `develop` branch and pushed initial planning files to `main`
- Scaffolded Django 6.0.4 project with `config/settings/` package (base, development, production, ci)
- Created all 5 app stubs: core, main, services, industries, contact
- Created `passenger_wsgi.py`, `manage.py`, `requirements.txt`, `requirements-dev.txt`
- Created `.env.example`, `.gitignore`, `pytest.ini`, `pyproject.toml`
- Created `.github/workflows/deploy.yml` (GitHub Actions CI + SSH deploy)
- Replaced `mysqlclient` with `PyMySQL` — shared hosting has no MySQL dev libraries
- Patched PyMySQL version info to satisfy Django 6's mysqlclient >= 2.2.1 check
- Created `Passengerfile.json` for cPanel Passenger process manager
- Created MySQL database `bjptechn_bjp_db` and user `bjptechn_bjp_user` in cPanel
- Configured cPanel Python App (Python 3.12.12, Passenger, app root: bjp-technologies-web)
- Added cPanel server SSH public key as GitHub deploy key
- Created `.env` on server via File Manager with production credentials
- Set `DJANGO_SETTINGS_MODULE=config.settings.production` in Python App env vars
- Ran `pip install`, `migrate`, `collectstatic` via cPanel Python App execute scripts
- Confirmed site live at `https://bjptechnologies.co.tz` — Django responding with 404 (correct, no URLs yet)

### Files Changed
| File | Action | Notes |
|---|---|---|
| config/settings/base.py | Created | PyMySQL install + version patch |
| config/settings/development.py | Created | SQLite for local dev |
| config/settings/production.py | Created | MySQL, security headers |
| config/settings/ci.py | Created | CI MySQL config |
| apps/core/ | Created | App stub + context_processors.py |
| apps/main/ | Created | App stub |
| apps/services/ | Created | App stub |
| apps/industries/ | Created | App stub |
| apps/contact/ | Created | App stub |
| passenger_wsgi.py | Created | cPanel Passenger entry point |
| Passengerfile.json | Created | Passenger process config |
| requirements.txt | Created | PyMySQL, Django, WhiteNoise, dotenv |
| requirements-dev.txt | Created | pytest, ruff, black, factory-boy |
| .env.example | Created | Template for server .env |
| .gitignore | Created | Excludes venv, .env, public/ |
| pytest.ini | Created | Test configuration |
| pyproject.toml | Created | ruff + black config |
| .github/workflows/deploy.yml | Created | CI test + SSH deploy pipeline |
| CLAUDE.md | Modified | Phase 1 marked complete, Phase 2 current |
| SESSION_LOG.md | Modified | This entry |

### Migrations
- Migration name: Django built-in (admin, auth, contenttypes, sessions)
- Applied: ✅ Yes — on `bjptechn_bjp_db` MySQL database

### Tests
- Tests written: 0 (Phase 1 — infrastructure only, no app logic)
- Tests passing: N/A
- Coverage areas: N/A

### Decisions Made
- **Decision:** Use PyMySQL instead of mysqlclient.
  **Reason:** Shared hosting (cPanel) does not have MySQL development libraries (`libmysqlclient-dev`) required to build mysqlclient. PyMySQL is pure Python and installs without system dependencies.
- **Decision:** Patch `pymysql.version_info` to `(2, 2, 1)` after `install_as_MySQLdb()`.
  **Reason:** Django 6 checks mysqlclient version >= 2.2.1. PyMySQL reports 1.4.6 which fails the check. Patching the version tuple is the standard workaround for this combination.
- **Decision:** Deploy manually via cPanel Git Version Control + Python App instead of GitHub Actions SSH.
  **Reason:** SSH port 22 is blocked on the shared hosting server. cPanel Terminal was unavailable. GitHub Actions SSH deploy will be wired up once SSH access is resolved. Manual pull via cPanel UI is the interim deploy method.
- **Decision:** Use cPanel Git Version Control for server-side repo management.
  **Reason:** No SSH access and no cPanel Terminal available. Git Version Control in cPanel is the only available path to clone and update the repo on the server.
- **Decision:** Set `DJANGO_SETTINGS_MODULE=config.settings.production` in Python App env vars.
  **Reason:** manage.py defaults to development (SQLite). Without this env var, execute scripts run migrations on SQLite instead of MySQL.

### Blockers / Issues
- SSH port 22 blocked — GitHub Actions auto-deploy not yet wired up. Manual pull via cPanel Git Version Control is the interim deploy method.
- Branch protection rules skipped — requires GitHub Pro for private repos.
- Server response is slow (~5–10s) — expected on shared hosting with cold Passenger starts.

### Phase Deliverables Completed
- [x] GitHub repo created: `bjp-technologies-web` (private)
- [x] Django project scaffolded with `config/settings/` (base, dev, production)
- [x] `passenger_wsgi.py` created and tested
- [x] `requirements.txt` and `requirements-dev.txt` complete
- [x] `.env.example` committed, `.env` on server only
- [x] `.gitignore` complete
- [x] `pytest.ini` and `pyproject.toml` configured
- [x] MySQL database created in cPanel (`bjptechn_bjp_db`, `bjptechn_bjp_user`)
- [x] cPanel Python App configured (Python 3.12.12, Passenger)
- [x] SSH deploy key added to GitHub repo
- [x] GitHub Actions `deploy.yml` workflow created
- [x] Django responding live at `https://bjptechnologies.co.tz` (404 — correct, no URLs yet)
- [x] `SESSION_LOG.md` updated
- [x] ALLOWED_HOSTS confirmed: `bjptechnologies.co.tz`, `www.bjptechnologies.co.tz`
- [ ] ⚠️ Branch protection rules — skipped (requires GitHub Pro)
- [ ] ⚠️ GitHub Actions auto-deploy — pending SSH access resolution

### Next Session Should
- [ ] Start Phase 2 — Core Foundation
- [ ] Create `apps/core/templates/core/base.html` with all blocks
- [ ] Create `core/navbar.html` and `core/footer.html`
- [ ] Create `static/css/style.css` with BJP brand variables
- [ ] Create `static/js/main.js`
- [ ] Add BJP logo SVG to `static/images/logo/`
- [ ] Load Google Fonts (Outfit, DM Serif Display, Space Mono)
- [ ] Create placeholder 404 and 500 pages
- [ ] Wire up `apps/main/` HomeView so site returns 200 OK instead of 404

---

<!-- 
TEMPLATE FOR NEXT SESSION — copy this block and fill in:

---

## Session [N] — [DATE] [TIME EAT]

**Goal:** 
**Branch:** 
**Status:** ✅ Complete | 🔄 In Progress | ❌ Blocked
**Phase:** Phase [N] — [Name]

### What Was Done
- 

### Files Changed
| File | Action | Notes |
|---|---|---|
|  |  |  |

### Migrations
- Migration name: 
- Applied: ✅ Yes / ❌ No / N/A

### Tests
- Tests written: 
- Tests passing: / 
- Coverage areas: 

### Decisions Made
- **Decision:** 
  **Reason:** 

### Blockers / Issues
- 

### Phase Deliverables Completed
- [ ] 

### Next Session Should
- [ ] 

---
-->
