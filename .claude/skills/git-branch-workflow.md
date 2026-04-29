# Skill: Git Branch Workflow
# Read this before any git operation in the BJP Technologies project.

## Branch Types and Naming

| Type | Pattern | Example |
|---|---|---|
| Feature | `feature/short-description` | `feature/contact-form` |
| Bug fix | `fix/short-description` | `fix/navbar-mobile-overlap` |
| Hotfix | `hotfix/short-description` | `hotfix/broken-passenger-wsgi` |
| Chore | `chore/short-description` | `chore/update-requirements` |
| Docs | `docs/short-description` | `docs/deployment-guide` |
| Tests | `test/short-description` | `test/contact-view-coverage` |

## Starting Any New Task

```bash
# Always start from develop (not main)
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

## Committing

Use Conventional Commits format:
```
type(scope): short imperative description

Optional body explaining WHY, not what.

Optional footer: refs #issue, BREAKING CHANGE: description
```

Types: `feat` `fix` `docs` `style` `refactor` `test` `chore` `ci`
Scopes: `core` `main` `services` `contact` `industries` `auth` `admin` `deploy` `deps`

Good examples:
```
feat(contact): add contact enquiry form with MySQL model
fix(services): correct slug generation for service with apostrophe
test(main): add HomeView and AboutView unit tests
chore(deps): upgrade Django to 5.1.3
ci(deploy): add collectstatic step before restart
```

## Finishing a Feature

```bash
# Run all checks first
pytest
ruff check .
black --check .

# Stage and commit
git add .
git commit -m "feat(scope): description"

# Push branch
git push origin feature/your-feature-name

# Report to developer: "Branch ready. Open PR targeting develop."
# DO NOT merge yourself.
```

## Protected Branch Rules

- `main` — no direct commits ever. CI/CD deploys from here.
- `develop` — no direct commits. Feature branches merge here via PR.
- All PRs require CI to pass before merge is allowed.

## After a Merge

Delete the feature branch locally:
```bash
git checkout develop
git pull origin develop
git branch -d feature/your-feature-name
```
