from django.views.generic import TemplateView

DEFAULT_INDUSTRIES = [
    ("Startups & SMEs", "startups-smes"),
    ("Financial Institutions", "financial-institutions"),
    ("NGOs & Development Orgs", "ngos-development"),
    ("Education Institutions", "education"),
    ("Healthcare Providers", "healthcare"),
    ("Retail & Wholesale", "retail-wholesale"),
]


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["default_industries"] = DEFAULT_INDUSTRIES
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"
