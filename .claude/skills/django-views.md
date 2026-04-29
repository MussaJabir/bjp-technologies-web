# Skill: Django Views & URLs
# Read this before writing any view or URL pattern.

## View Choice Guide

| Situation | Use |
|---|---|
| Simple page, no model | `TemplateView` or FBV |
| List of model objects | `ListView` |
| Single model object | `DetailView` |
| Create object | `CreateView` |
| Update object | `UpdateView` |
| Delete object | `DeleteView` |
| Form that isn't a model form | FBV with form class |
| Complex mixed logic | FBV |

## Class-Based View Patterns

### Home Page
```python
from django.views.generic import TemplateView
from apps.services.models import Service
from apps.industries.models import Industry

class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services']   = Service.objects.filter(is_active=True)[:6]
        context['industries'] = Industry.objects.filter(is_active=True)
        return context
```

### Service Detail
```python
from django.views.generic import DetailView
from apps.services.models import Service

class ServiceDetailView(DetailView):
    model               = Service
    template_name       = 'services/detail.html'
    context_object_name = 'service'
    slug_field          = 'slug'
    slug_url_kwarg      = 'slug'
```

### Contact Form (FBV — mixed form + email logic)
```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.ip_address = get_client_ip(request)
            enquiry.save()
            send_contact_notifications(enquiry)
            return redirect('contact:success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
```

## URL Patterns

Every app has its own `urls.py`. Root `config/urls.py` includes them:

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('',            include('apps.main.urls',       namespace='main')),
    path('services/',   include('apps.services.urls',   namespace='services')),
    path('industries/', include('apps.industries.urls', namespace='industries')),
    path('contact/',    include('apps.contact.urls',    namespace='contact')),
]
```

```python
# apps/services/urls.py
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('',          views.ServicesListView.as_view(), name='list'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='detail'),
]
```

## Template Names Convention

Always follow: `appname/action.html`

```
apps/main/templates/main/home.html
apps/main/templates/main/about.html
apps/services/templates/services/list.html
apps/services/templates/services/detail.html
apps/contact/templates/contact/contact.html
apps/contact/templates/contact/success.html
```

## URL Usage in Templates

Always use `{% url %}` tag — never hardcode paths:

```html
<a href="{% url 'services:list' %}">All Services</a>
<a href="{% url 'services:detail' slug=service.slug %}">{{ service.name }}</a>
<a href="{% url 'contact:contact' %}">Contact Us</a>
```

## Context Processors

Global context available in all templates via `apps/core/context_processors.py`:

```python
def company_info(request):
    return {
        'company_name':  'BJP Technologies (T) Limited',
        'company_phone': '+255 678 290 994',
        'company_email': 'info@bjptechnologies.co.tz',
        'company_address': 'Ubungo – Dar es Salaam, Tanzania',
    }
```

Register in `settings/base.py`:
```python
'OPTIONS': {
    'context_processors': [
        ...
        'apps.core.context_processors.company_info',
    ],
},
```
