from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q, F, Value
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from store.models import *

__all__ = ('product_view', )

# Create your views here.
def product_view(request):

    products = Product.objects.filter(title="product-0").annotate(new_id=F("product_id"))
    print(products[0].new_id)








    # products = list(queryset)
    return render(request, 'product.html', context={'products': list(products)})
