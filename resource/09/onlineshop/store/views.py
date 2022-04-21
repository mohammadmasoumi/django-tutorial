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
    # fetchone, fetchall
    count = 0

    # products = Product.objects.filter(collection=1).only('title') 
    # products = Product.objects.filter(collection__title='collection-0')
    # cursor = connection.cursor()
    # cursor.execute('''
    # SELECT "store_product"."product_id",
    #    "store_product"."slug",
    #    "store_product"."title",
    #    "store_product"."description",
    #    "store_product"."price",
    #    "store_product"."invetory",
    #    "store_product"."collection_id",
    #    "store_product"."last_update",
    #    "store_product"."created_at"
    #     FROM "store_product"
    #     INNER JOIN "store_collection"
    #         ON ("store_product"."collection_id" = "store_collection"."id")
    #     WHERE "store_collection"."title" = "collection-0"
    # ''')
    # row = cursor.fetchone() # len: 9
    # row = cursor.fetchall() # len: 10
    # for item in row:
    #     print(item)
    #     print("---------------")
    # print(type(row), len(row))

    # only
    # در استفاده از only دقت لازم را به خرج دهید
    # اگر بخواهید به فیلدی دسترسی پیدا کنید که در only نیازوردید 
    # به ازای هر کدوم از فیلد های اضافه یک کوِری به دیتابیس خورده میشود.
    
    # products = Product.objects.filter(collection__title='collection-0').only('title') # 13 queries 
    # products = Product.objects.filter(collection__title='collection-0').only('title', 'created_at') # 3 queries 
    
    # [Product, Product, Product]
    # title
    # product.description => new query

    # defer
    # products = Product.objects.filter(collection__title='collection-0').defer('title') # 13 queries 
    # products = Product.objects.filter(collection__title='collection-0').defer('title', 'created_at') # 23 queries 
    # products = Product.objects.filter(collection__title='collection-0') # 3 queries 

    # select_related
    # one-to-one, one-to-many
    # products = Product.objects.filter() # 103 queries
    # products = Product.objects.select_related('collection') # 3 queries
    
    # cache quey
    # products[0] # 4 queries
    
    # list(products)
    # list(products)
    # list(products)
    # list(products)

    # products[0] # 3 queries

    # prefetch_related
    # many to many
    # products = Product.objects.select_related('collection').prefetch_related('promotion').get(title='product-0')
    # products = [products]
    # for prodcut in products:
    #     print(prodcut.promotion.all())
    #     # print(prodcut.promotion.filter(descrition='asghar'))
    #     # print(dir(prodcut))
    #     # for item in dir(prodcut):
    #     #     if 'pro' in item:
    #     #         print(item)

    # values
    products = Product.objects.filter(title="product-0").annotate(new_id=F("product_id"))
    print(products[0].new_id)

    # products = list(queryset)
    return render(request, 'product.html', context={'products': list(products), 'count': count})
