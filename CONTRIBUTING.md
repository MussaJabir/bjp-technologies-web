# Contributing to BJP Technologies Web

Thank you for contributing to this project. This document covers everything you need to get started.

---

## Before You Start

Read [`CLAUDE.md`](CLAUDE.md) fully before making any changes. It is the master reference for this project — coding conventions, branching rules, commit format, phase scope, and the definition of done are all defined there.

---

## Branching Workflow

Every piece of work starts on its own branch:

```bash
# Always branch from develop, never from main
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Branch naming

| Type | Pattern | Example |
|---|---|---|
| New feature | `feature/*` | `feature/blog-section` |
| Bug fix | `fix/*` | `fix/footer-mobile-layout` |
| Emergency fix | `hotfix/*` | `hotfix/broken-contact-form` |
| Non-code | `chore/*` | `chore/update-requirements` |
| Documentation | `docs/*` | `docs/api-reference` |

### Rules
- **Never commit to `main` or `develop` directly**
- PRs target `develop` first — `develop → main` requires a review
- Delete the branch after it is merged

---

## Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): short description

[optional body]
```

| Type | Use for |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructure, no behaviour change |
| `test` | Adding or updating tests |
| `chore` | Dependency updates, config changes |
| `ci` | CI/CD pipeline changes |

**Examples:**
```
feat(contact): add rate limiting on enquiry form submission
fix(navbar): correct z-index on mobile menu overlay
chore(deps): pin Django to 6.0.4
```

---

## Definition of Done

A task is only complete when all of the following are true:

- [ ] Code is on a feature branch (not `main` or `develop`)
- [ ] All new code has corresponding tests
- [ ] `pytest` passes with no failures
- [ ] `ruff check .` passes with no errors
- [ ] `black --check .` passes
- [ ] No hardcoded secrets or credentials
- [ ] Migrations created and tested locally
- [ ] Template renders correctly in a browser
- [ ] `collectstatic` runs without errors
- [ ] Branch committed with a conventional commit message
- [ ] PR description summarises what changed and why

---

## Pull Request Process

1. Ensure your branch is up to date with `develop`
2. Push your branch: `git push origin feature/your-feature-name`
3. Open a PR targeting `develop` on GitHub
4. Fill in the PR template fully
5. Wait for CI checks to pass
6. Request a review

**Do not merge your own PRs.**

---

## Running Locally

See the [Local Setup](README.md#local-setup) section in `README.md`.

```bash
# Tests
pytest

# Lint
ruff check .
black --check .
```

---

## Questions

Open a GitHub issue using the appropriate template, or contact the team at [info@bjptechnologies.co.tz](mailto:info@bjptechnologies.co.tz).
