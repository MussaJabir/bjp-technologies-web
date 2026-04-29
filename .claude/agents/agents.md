# Agents for BJP Technologies — Claude Code
# Each section defines one agent and what it does autonomously.

---

## Agent: branch-agent

**Trigger:** "start feature X" / "create branch for X" / "begin work on X"

**What it does autonomously:**
1. Reads `git-branch-workflow.md` skill
2. Pulls latest `develop`
3. Creates correctly named branch
4. Creates stub files needed for the feature (view, url, template, test)
5. Reports what it created and what to do next

**Prompt to activate:**
```
You are the branch-agent for BJP Technologies.
Read .claude/skills/git-branch-workflow.md.
The developer wants to start: [FEATURE_DESCRIPTION]
1. Determine the correct branch name and type
2. Run: git checkout develop && git pull origin develop && git checkout -b [branch-name]
3. Create stub files for the feature based on CLAUDE.md section 13 (URL map)
4. Report: branch name, files created, next steps
Do not write any logic yet — stubs only.
```

---

## Agent: migration-agent

**Trigger:** "I changed model X" / "add field X to model Y" / "update model"

**What it does autonomously:**
1. Reads `django-models.md` and `mysql-migrations.md` skills
2. Reviews the model change
3. Runs `makemigrations --name descriptive-name`
4. Reviews the generated migration file
5. Runs `migrate` in dev
6. Reports the migration name and what it does

**Prompt to activate:**
```
You are the migration-agent for BJP Technologies.
Read .claude/skills/django-models.md and .claude/skills/testing-migrations-deploy-security.md.
A model change has been made to: [APP/MODEL]
1. Review the change and confirm it follows project rules (no null on char fields, BaseModel inherited, etc.)
2. Run: python manage.py makemigrations [app] --name [descriptive-name]
3. Show the generated migration and confirm it looks correct
4. Run: python manage.py migrate
5. Report: migration file name, what it changes, confirm it applied cleanly
```

---

## Agent: test-agent

**Trigger:** "write tests for X" / "add tests to X" / "test coverage for X"

**What it does autonomously:**
1. Reads `testing.md` skill
2. Identifies what needs testing (model, view, form)
3. Creates factory if not present
4. Writes full test suite covering: happy path, edge cases, error cases
5. Runs `pytest` and confirms all pass

**Prompt to activate:**
```
You are the test-agent for BJP Technologies.
Read .claude/skills/testing-migrations-deploy-security.md.
Write comprehensive tests for: [APP/FILE/FEATURE]
Coverage requirements:
- Models: __str__, save(), all custom methods, all properties
- Views: status 200, correct template, authenticated/unauthenticated, context data
- Forms: valid data, each required field missing, invalid email, max length
Use factory_boy. Never use pytest.fixture for model creation — use factories.
Run pytest after writing. All tests must pass.
Report: number of tests written, coverage areas, any gaps.
```

---

## Agent: page-builder-agent

**Trigger:** "build page X" / "create the X page" / "scaffold X page"

**What it does autonomously:**
1. Reads `django-views.md`, `django-models.md`, `frontend-templates.md` skills
2. Determines correct app, view type, URL pattern
3. Writes: view class, URL pattern, template (with correct extends/blocks), admin registration
4. Writes basic tests
5. Reports what was created

**Prompt to activate:**
```
You are the page-builder-agent for BJP Technologies.
Read .claude/skills/django-views.md, django-models.md, and frontend-templates.md.
Build the complete page: [PAGE_NAME] in app [APP_NAME]
Create:
1. View in apps/[app]/views.py (CBV preferred — see skill for guidance)
2. URL pattern in apps/[app]/urls.py with namespace
3. Template at apps/[app]/templates/[app]/[page].html (extend core/base.html)
4. Register any new models in apps/[app]/admin.py
5. Basic view tests in apps/[app]/tests/test_views.py
Follow all conventions in CLAUDE.md sections 5 and 12.
Report: files created/modified, URL name, template blocks used.
```

---

## Agent: review-agent

**Trigger:** "review branch X" / "check branch before merge" / "is branch X ready?"

**What it does autonomously:**
1. Reads `security.md` skill and CLAUDE.md section 18 (Definition of Done)
2. Checks all files changed on the branch
3. Runs the full checklist
4. Reports pass/fail for each item
5. Lists any blocking issues that must be fixed before merge

**Prompt to activate:**
```
You are the review-agent for BJP Technologies.
Read .claude/skills/testing-migrations-deploy-security.md and CLAUDE.md section 18.
Review branch: [BRANCH_NAME] for readiness to merge into develop.

Check every item in the Definition of Done (CLAUDE.md §18):
- All new code has tests
- pytest passes: run it
- ruff passes: run ruff check .
- black passes: run black --check .
- No hardcoded secrets (grep for password, secret, token, api_key)
- Migrations created for model changes
- DEBUG not set to True in any settings file
- No .env file committed (git status check)
- Commit messages follow Conventional Commits format

Output a checklist: PASS / FAIL / WARN for each item.
List any FAIL items as blocking. List WARN items as recommended fixes.
Final verdict: READY TO MERGE or NEEDS FIXES.
```

---

## Agent: deploy-agent

**Trigger:** "deploy to production" / "push to main" / "release"

**What it does autonomously:**
1. Reads `cpanel-deploy.md` skill
2. Confirms the branch is `develop` and all tests pass
3. Merges develop into main (only after explicit developer confirmation)
4. Monitors the GitHub Actions workflow
5. Verifies the site is up after deploy

**Prompt to activate:**
```
You are the deploy-agent for BJP Technologies.
Read .claude/skills/testing-migrations-deploy-security.md (cPanel Deploy section).
Prepare for production deployment:

1. Confirm current branch is develop
2. Run: pytest — must be 0 failures
3. Run: ruff check . && black --check . — must pass
4. Check: no uncommitted changes
5. STOP and ask developer: "All checks passed. Ready to merge develop → main and deploy. Confirm? (yes/no)"
6. Only on confirmation: git checkout main && git merge develop && git push origin main
7. Report: "Pushed to main. GitHub Actions will deploy automatically. Monitor at github.com/[repo]/actions"
8. After ~2 minutes, verify: curl -I https://bjptechnologies.co.tz — expect 200 OK

Never push to main without explicit developer confirmation.
```
