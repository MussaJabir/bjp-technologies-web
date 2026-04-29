# Skill: Testing
# Read this before writing any test in BJP Technologies.

## Setup

```python
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings.development
python_files = tests/test_*.py
python_classes = Test*
python_functions = test_*
addopts = --tb=short -v
```

## Factories (factory_boy)

Never create test data directly. Always use factories:

```python
# apps/services/tests/factories.py
import factory
from apps.services.models import Service

class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name     = factory.Sequence(lambda n: f'Service {n}')
    slug     = factory.LazyAttribute(lambda o: o.name.lower().replace(' ', '-'))
    category = Service.Category.SOFTWARE
    summary  = factory.Faker('sentence', nb_words=10)
    description = factory.Faker('paragraph')
    is_active = True
    order    = factory.Sequence(lambda n: n)
```

## Model Tests

```python
# apps/services/tests/test_models.py
import pytest
from .factories import ServiceFactory

@pytest.mark.django_db
class TestServiceModel:
    def test_str_returns_name(self):
        service = ServiceFactory(name='Cybersecurity')
        assert str(service) == 'Cybersecurity'

    def test_slug_auto_generated(self):
        service = ServiceFactory(name='Cloud Infrastructure', slug='')
        assert service.slug == 'cloud-infrastructure'

    def test_has_timestamps(self):
        service = ServiceFactory()
        assert service.created_at is not None
        assert service.updated_at is not None
```

## View Tests

```python
# apps/services/tests/test_views.py
import pytest
from django.urls import reverse
from .factories import ServiceFactory

@pytest.mark.django_db
class TestServicesListView:
    def test_status_200(self, client):
        url = reverse('services:list')
        response = client.get(url)
        assert response.status_code == 200

    def test_correct_template(self, client):
        url = reverse('services:list')
        response = client.get(url)
        assert 'services/list.html' in [t.name for t in response.templates]

    def test_only_active_services_shown(self, client):
        active   = ServiceFactory(is_active=True)
        inactive = ServiceFactory(is_active=False)
        response = client.get(reverse('services:list'))
        assert active.name in str(response.content)
        assert inactive.name not in str(response.content)
```

## Form Tests

```python
@pytest.mark.django_db
class TestContactForm:
    def test_valid_form(self):
        data = {
            'first_name': 'John',
            'last_name':  'Doe',
            'email':      'john@example.com',
            'message':    'Hello, I need IT help.',
        }
        form = ContactForm(data=data)
        assert form.is_valid()

    def test_email_required(self):
        data = {'first_name': 'John', 'last_name': 'Doe', 'message': 'Hi'}
        form = ContactForm(data=data)
        assert not form.is_valid()
        assert 'email' in form.errors
```

---

# Skill: MySQL Migrations
# Read this before making any model change.

## Rules

1. **Never edit an applied migration** — create a new one
2. **Never delete a migration file**
3. **Always review** the generated migration before applying
4. **Name migrations descriptively**: `python manage.py makemigrations --name add_service_icon_field`
5. **Test migrations on dev** before pushing to production

## Safe Field Operations

```bash
# Add a new field (safe)
python manage.py makemigrations --name add_phone_to_contact

# Rename a field — DO THIS INSTEAD of renaming directly:
# 1. Add new field
# 2. Write data migration to copy values
# 3. Remove old field in a later migration
```

## Data Migrations

When you need to transform data during a migration:

```python
from django.db import migrations

def set_default_order(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    for i, service in enumerate(Service.objects.all()):
        service.order = i
        service.save()

class Migration(migrations.Migration):
    dependencies = [('services', '0002_service_order')]
    operations   = [migrations.RunPython(set_default_order, migrations.RunPython.noop)]
```

---

# Skill: cPanel Deploy
# Read this before any deployment action.

## Automated Deploy (preferred)
Push to `main` → GitHub Actions runs → auto-deploys. Nothing manual needed.

## Manual Deploy (emergency only)

```bash
ssh user@bjptechnologies.co.tz
cd ~/bjp-technologies-web
git pull origin main
source ~/virtualenv/bjp-technologies-web/3.11/bin/activate
pip install -r requirements.txt --quiet
python manage.py migrate --no-input
python manage.py collectstatic --no-input
touch tmp/restart.txt
echo "Deploy complete"
```

## Verify Deploy Worked

```bash
# Check app is running
curl -I https://bjptechnologies.co.tz

# Check for errors in Passenger log
tail -50 ~/logs/bjp-technologies-web/error_log
```

## Rollback

```bash
git log --oneline -5       # find previous commit hash
git checkout <hash>        # check out that commit
touch tmp/restart.txt      # restart app on that version
```

---

# Skill: Security
# Read this before any code review or before touching settings.

## Mandatory Production Settings

```python
DEBUG               = False
SECRET_KEY          = os.environ['SECRET_KEY']  # from .env — never hardcoded
ALLOWED_HOSTS       = ['bjptechnologies.co.tz', 'www.bjptechnologies.co.tz']
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS     = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE  = True
SESSION_COOKIE_SECURE = True
```

## Checks Before Any Merge to Main

- [ ] No secret keys, passwords, or tokens in any file
- [ ] `DEBUG = False` in production settings
- [ ] `.env` is in `.gitignore` and not committed
- [ ] `ALLOWED_HOSTS` doesn't contain `*`
- [ ] All forms have `{% csrf_token %}`
- [ ] File upload views validate type and size
- [ ] No `print()` statements left in production code
- [ ] No `TODO: fix security` comments left unaddressed

## Gitignore Must Include

```
.env
*.pyc
__pycache__/
public/static/
public/media/
venv/
*.sqlite3
.DS_Store
```
