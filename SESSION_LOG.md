# SESSION_LOG.md — BJP Technologies (T) Limited
# technologies.bejundas.co.tz

> This file is updated by Claude Code at the end of every working session.
> It is the single source of truth for project progress, decisions, and context.
> Never delete entries. Always append new entries at the bottom.
> Committed to git at the end of every session.

---

## Project Summary

**Repo:** bjp-technologies-web
**Domain:** technologies.bejundas.co.tz
**Stack:** Django 6 + MySQL + cPanel + GitHub Actions
**Current Phase:** Phase 1 — Infrastructure & Hosting
**Started:** April 2026

## Phase Progress

| Phase | Name | Status |
|---|---|---|
| Phase 1 | Infrastructure & Hosting | 🔄 In Progress |
| Phase 2 | Core Foundation | ⏳ Pending |
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
