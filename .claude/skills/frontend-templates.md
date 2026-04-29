# Skill: Frontend Templates
# Read this before writing or editing any HTML template.

## Template Inheritance

Every page template extends `core/base.html`:

```html
{% extends 'core/base.html' %}
{% load static %}

{% block title %}Services — BJP Technologies{% endblock %}
{% block meta_description %}Comprehensive IT services including software development, cloud infrastructure, cybersecurity and more.{% endblock %}

{% block content %}
  <!-- page content here -->
{% endblock %}
```

## Base Template Blocks

| Block | Purpose |
|---|---|
| `title` | Page `<title>` tag — always include company name |
| `meta_description` | Meta description for SEO |
| `extra_css` | Page-specific CSS link tags |
| `content` | Main page content |
| `extra_js` | Page-specific JS script tags |

## BJP Brand CSS Variables

Always use CSS variables — never hardcode hex colors in templates:

```css
var(--navy)        /* #0D1B4B — primary brand */
var(--navy-dark)   /* #080F2E — darkest navy */
var(--blue)        /* #1565C0 — action blue */
var(--blue-light)  /* #1E88E5 — hover */
var(--accent)      /* #00C6FF — cyan accent */
var(--white)       /* #FFFFFF */
var(--off-white)   /* #F4F6FC — light backgrounds */
var(--grey-light)  /* #E8ECF4 — borders */
var(--grey)        /* #8A94B0 — muted text */
var(--text-body)   /* #3A4468 — body text */
```

## Static Files

Every template that uses static files must load the tag:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo/bjp-logo.svg' %}" alt="BJP Technologies">
<script src="{% static 'js/main.js' %}"></script>
```

## Common Components

### Section Header Pattern
```html
<div class="section-header">
  <span class="section-tag">What We Do</span>
  <h2>Section Title</h2>
  <p>Supporting description text.</p>
</div>
```

### Service Card Pattern
```html
<div class="service-card">
  <div class="service-icon">{{ service.icon }}</div>
  <h4>{{ service.name }}</h4>
  <p>{{ service.summary }}</p>
  <a href="{% url 'services:detail' slug=service.slug %}" class="service-link">
    Learn More →
  </a>
</div>
```

### Button Patterns
```html
<a href="{% url 'contact:contact' %}" class="btn btn-primary">Get in Touch →</a>
<a href="{% url 'services:list' %}" class="btn btn-dark">View Services →</a>
<a href="tel:+255678290994" class="btn btn-outline">Call Us</a>
```

### Contact Detail Pattern
```html
<div class="contact-detail">
  <div class="contact-detail-icon">📞</div>
  <div class="contact-detail-text">
    <div class="label">Phone</div>
    <div class="value">
      <a href="tel:{{ company_phone }}">{{ company_phone }}</a>
    </div>
  </div>
</div>
```

## Template Tags & Filters

Always use built-in Django tags. Don't write custom template tags unless absolutely necessary.

```html
{% for service in services %}
  {% if service.is_active %}
    {{ service.name }}
    {{ service.description|truncatewords:30 }}
    {{ service.created_at|date:"d M Y" }}
  {% endif %}
{% empty %}
  <p>No services available.</p>
{% endfor %}
```

## Accessibility Rules

- Every `<img>` must have `alt` attribute
- Forms must have `<label>` for every input
- Use semantic HTML: `<main>`, `<nav>`, `<section>`, `<article>`, `<footer>`
- Buttons that are links use `<a>`, not `<button>`
- Heading hierarchy: one `<h1>` per page, followed by `<h2>`, `<h3>` etc.

## JavaScript in Templates

Never write inline JavaScript in templates. Put JS in `static/js/main.js` or page-specific files:

```html
{% block extra_js %}
<script src="{% static 'js/contact.js' %}"></script>
{% endblock %}
```

Use `data-*` attributes to pass Django context to JS:
```html
<div id="services-count" data-count="{{ services.count }}"></div>
```
