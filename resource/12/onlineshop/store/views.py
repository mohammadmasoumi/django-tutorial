from django.shortcuts import render
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from store.models import *
from tags.models import *


__all__ = ('product_view', 'ProductView', 'ProductDetailView', 'ProductListView')


def product_view(request):

    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass

    return render(request, 'empty.html')

# View
# ship
# sheep
class ProductView(View):

    def get(self, request):
        return HttpResponse("Hello")


# get_object, get_queryset, get_context_data
class ProductDetailView(DetailView):
    model = Product
    context_object_name = "asghar"
    template_name: str = "product_template.html"
    slug_url_kwarg = "asghar_id"
    slug_field = "slug"
    queryset = Product.objects.filter(inventory__gte=10)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductListView(ListView):
    model = Product
    template_name: str = "product_list_template.html"
    paginate_by = 50
    queryset = Product.objects.filter(inventory__gte=10)
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context