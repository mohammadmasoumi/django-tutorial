from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q
from store.models import *

__all__ = ('product_view', )

# Create your views here.
def product_view(request):
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#exact
    product_name = "product-1"
    # queryset, qs
    # lazy functions
    # queryset = Product.objects.all()
    # invetory>20 -> bool
    # lookup fields
    # Product.objects.filter(invetory__gt=20)
    # gt greater than
    # gte greater than equal
    # lt
    # lte
    # invetory = 20 
    # contains - case sensetive 
    # Product.objects.filter(title__icontains='T')
    # icontains - case insensitive
    # isnull
    # Product.objects.filter(description__isnull=False)
    # Product.objects.filter(title__iexact='Product-1')
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#exact
    # queryset = Product.objects.filter(title__iexact=product_name)
    # queryset = Product.objects.filter(price__range=(200, 300))
    # queryset = Product.objects.filter(title__in=["product-1", "product-2"])
    # [] AND [] AND [] => (, , , )
    # queryset = Product.objects.filter(created_at__year=2022, created_at__month=4)
    # queryset = Product.objects.filter(created_at__year=2022).filter(created_at__month=4)
    # timezone.datetime(year=2022, month=4)
    # date_range = (
    #     (timezone.now() - timezone.timedelta(hours=2)).isoformat(), 
    #     timezone.now().isoformat()
    # )
    # ('2022-04-02T10:46:41.494271+00:00', '2022-04-07T10:46:41.494271+00:00')
    # queryset = Product.objects.filter(created_at__range=date_range)
    # queryset = Product.objects.filter(pk=1) == .filter(product_id=1)
    # queryset = Product.objects.filter(collection__title='collection-0 ') # collection_id
    # Q = query
    queryset = Product.objects.filter()

    # # 1. for loop
    # for product in queryset:
    #     print(product)

    # # 2. cast to list
    # list(queryset)

    # # 3. access to the element
    # queryset[0]

    return render(request, 'product.html', context={'products': list(queryset)})
