# Skill: Django Models
# Read this before writing or modifying any model in BJP Technologies.

## BaseModel (always inherit from this)

Defined in `apps/core/models.py`. Every model in this project inherits from it.

```python
import uuid
from django.db import models

class BaseModel(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

## Rules

1. **Always inherit BaseModel** — never use Django's default integer PK for exposed models
2. **No `null=True` on CharFields or TextFields** — use `blank=True, default=''`
3. **Always define `__str__`** — return a human-readable string
4. **Always define `Meta`** with `verbose_name` and `verbose_name_plural`
5. **Use `choices` tuples** for any field with fixed options
6. **Use `SlugField`** for URL-friendly identifiers, with `unique=True`
7. **Use `ordering`** in Meta for predictable querysets

## Example: Service Model

```python
from django.db import models
from django.utils.text import slugify
from apps.core.models import BaseModel


class Service(BaseModel):
    class Category(models.TextChoices):
        SOFTWARE     = 'software',     'Software Development'
        WEBSITE      = 'website',      'Website & Digital Solutions'
        CLOUD        = 'cloud',        'Cloud & Infrastructure'
        SECURITY     = 'security',     'Cybersecurity'
        MANAGED_IT   = 'managed_it',   'Managed IT Services'
        PAYMENTS     = 'payments',     'Payment Integrations'
        CONSULTING   = 'consulting',   'IT Consulting & Advisory'

    name        = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True, blank=True)
    category    = models.CharField(max_length=20, choices=Category.choices)
    summary     = models.CharField(max_length=300)
    description = models.TextField()
    icon        = models.CharField(max_length=10, default='💻', help_text='Emoji icon')
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name        = 'Service'
        verbose_name_plural = 'Services'
        ordering            = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
```

## Example: ContactEnquiry Model

```python
class ContactEnquiry(BaseModel):
    class Status(models.TextChoices):
        NEW     = 'new',     'New'
        READ    = 'read',    'Read'
        REPLIED = 'replied', 'Replied'

    first_name   = models.CharField(max_length=80)
    last_name    = models.CharField(max_length=80)
    email        = models.EmailField()
    phone        = models.CharField(max_length=20, blank=True, default='')
    company      = models.CharField(max_length=120, blank=True, default='')
    service      = models.ForeignKey(
        'services.Service',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='enquiries'
    )
    message      = models.TextField()
    ip_address   = models.GenericIPAddressField(null=True, blank=True)
    status       = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)

    class Meta:
        verbose_name        = 'Contact Enquiry'
        verbose_name_plural = 'Contact Enquiries'
        ordering            = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.email}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

## After Writing a Model

1. Run `python manage.py makemigrations`
2. Run `python manage.py migrate`
3. Register in `admin.py`
4. Write model tests in `tests/test_models.py`
