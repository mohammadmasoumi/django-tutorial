from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from store.models import *
from tags.models import *

__all__ = ('product_view', 'ProdcutDetailView')


def product_view(request):

    return render(request, 'empty.html')



class ProdcutDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = "product_template"
    pk_url_kwarg: str


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get(self, request, *args, **kwargs):
        """
        def get(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        """

        return super().get(request, *args, **kwargs)