from django.views.generic import DetailView, ListView

from .models import Service


class ServicesListView(ListView):
    model = Service
    template_name = "services/list.html"
    context_object_name = "services"
    queryset = Service.objects.filter(is_active=True).order_by("order")


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/detail.html"
    context_object_name = "service"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_services"] = (
            Service.objects.filter(is_active=True).exclude(pk=self.object.pk).order_by("order")
        )
        return context
