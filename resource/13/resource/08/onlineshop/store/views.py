from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from store.models import *

__all__ = ('product_view', )

# Create your views here.
def product_view(request):
    two_weeks_ago = timezone.now() - timezone.timedelta(weeks=2)
    # ----------------------------------------------------------------------
    # Q = query , OR filters
    # Product.objects.filter(title='product-1' | created_at__gte=)
    two_weeks_ago = timezone.now() - timezone.timedelta(weeks=2)
    # queryset = Product.objects.filter(title='product-1'  | created_at__gte=two_weeks_ago) WRONG
    # ~Q = not Q
    # a = two_weeks_ago + timezone.timedelta(days=10) # 4 days ago
    # queryset = Product.objects.filter(Q(title='product-0') | ~~Q(created_at__gte=a))
    # queryset = Product.objects.filter(Q(title='product-0') & Q(created_at__gte=a))
    # queryset = Product.objects.filter(title='product-0', created_at__gte=a)

    # ----------------------------------------------------------------------
    # Product matching query does not exist.
    products = []
    count = 0
    # products = [Product.objects.filter()]
    # products[0].filter()
    # try:
    #     product = Product.objects.get(title='product-0') # an object
    #     products.append(product)
    # except ObjectDoesNotExist:
    #     pass
    # ----------------------------------------------------------------------
    # give product object/instance or None
    # .first(), .last()
    # queryset.first()
    # product = Product.objects.filter(title='product-01').last()
    # if product:
    # products.append(product)
    # raise exception
    # print(products[0].created_at, products[0].title)
    # ----------------------------------------------------------------------
    # indexing 
    # Do not return a qs
    # .exists().filter() WRONG
    # existence = Product.objects.filter(title='product-0').exists()
    # print(f"existence: {existence}")
    # ----------------------------------------------------------------------
    # Count
    # Do not return a qs
    # .count().filter() WRONG
    # count = Product.objects.filter(created_at__year=2022).count()
    # print(f"count: {count}")
    # ----------------------------------------------------------------------
    # Limit & offset
    # 0-5
    # products = Product.objects.filter(created_at__year=2022)[:5]
    # limit, offset
    # products = Product.objects.filter(created_at__year=2022)[5:10]
    # Negative indexing is not supported.
    # اندکس منفی نداریم
    # - 
    # سورت بر اساس نزولی
    # +
    # سورت بر اساس صعودی
    # .order_by('-created_at')
    # نزولی بزرگترین اول است.
    # products = Product.objects \
    #     .filter(created_at__year=2022) \
    #     .order_by('-created_at')[:5]
    # ابتدا براساس عنوان به صورت صعودی سورت میکند
    # سپس بین آنهایی که عنوان یکسانی دارند،  بر اساس تاریخ ساخت آنها  نزولی سورت میکند.
    # products = Product.objects \
    #     .filter(created_at__year=2022) \
    #     .order_by('title', '-created_at')[:5]
    # ----------------------------------------------------------------------
    # F - An object capable of resolving references to existing query objects.
    # products = Product.objects.filter(title=F('slug'))
    # products = Product.objects.filter(slug=f('title'))
    # products = Product.objects.filter(title='slug')
    # name 'slug' is not defined
    # products = Product.objects.filter(title=slug)
    # ----------------------------------------------------------------------
    # products = Product.objects.all() # (103 queries)
    # select_related()
    # JOIN Product and Collection models (3 queries)
    # "store_product"."product_id",
    # "store_product"."slug",
    # "store_product"."title",
    # "store_product"."description",
    # "store_product"."price",
    # "store_product"."invetory",
    # "store_product"."collection_id",
    # "store_product"."last_update",
    # "store_product"."created_at",
    # "store_collection"."id",
    # "store_collection"."title"
    # products = Product.objects.select_related('collection').all()
    


    # products = list(queryset)
    return render(request, 'product.html', context={'products': list(products), 'count': count})
