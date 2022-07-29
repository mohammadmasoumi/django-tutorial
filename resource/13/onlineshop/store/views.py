from django.shortcuts import render
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from store.models import *
from tags.models import *
from random import randint



__all__ = (
    'product_view', 
    'success_view',
    'ProductView', 
    'ProductDetailView', 
    'ProductListView', 
    'ProductCreateView',
    'ProductUpdateView',
    'ProductDeleteView'
)


def product_view(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass

    return render(request, 'empty.html')

def success_view(request):
    return render(request, 'success.html')

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
    paginate_by = 10
    queryset = Product.objects.filter()
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductCreateView(CreateView):
    model = Product
    # "(app)/(model)(template_name_suffix).html"
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('product-list')
    fields = [
        'title',
        'description',
        'unit_price',
        'inventory',
    ]

    def form_valid(self, form):
        # print(form.data)
        # form.instance.collection = Collection.objects.filter().first() 
        # form.instance.slug = form.data.get("title")
        # form.instance.pk = Product.objects.filter().order_by("-created_at").first().pk + 1
        self.object = form.save(commit=False)
        self.object.collection = Collection.objects.filter().first()
        self.object.slug = self.object.title
        self.object.pk = 1000    
        self.object.save()   

        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    # "(app)/(model)(template_name_suffix).html"
    # pk_url_kwarg: str = 'pk'
    slug_url_kwarg = "asghar_id"
    slug_field = "slug"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('product-list')
    fields = [
        'title',
        'description'
    ]


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('success-product')
    slug_url_kwarg = "asghar_id"
    slug_field = "slug"
