from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q, F, Value, Count, Min, Max, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from store.models import *
from tags.models import *

__all__ = ('product_view', )

# Create your views here.
def product_view(request):
    # number of product
    count = 0
    products, customers = [], []

    # ---------------------------------- Simple queryset ----------------------------------
    # fetch all elements from database
    query_set = Product.objects.all() # this line doesn't hit the database
    
    # Chaining filters, django hits the database once
    # query_set = Product.objects.filter().filter().filter().order_by()

    # First five elements
    # print(query_set[0:5])
    # [Caution]: you can't use negative indexes.

    # lazy loading 
    # Django evaluates queryset whenever you use it, for instance, casting to list, for loop over it
    
    # Under below circumstances, django evaluates querysets.

    # 1. cast to list
    # print(list(query_set))

    # 2. loop over it
    # for product in query_set:
    #     print(property)

    # 3. access to one element
    # print(query_set[0])

    # [Caution]: In this case, be careful about django queryset caching.
    
    # 1. first approach
    # fetch first element of queryset, not all of them
    print(query_set[0])
    # fetch all elements from database, the previous one included!
    print(list(query_set))

    # 2. second approach
    # fetch all elements from database and cache them.
    print(list(query_set))
    # reach from cache queryset 
    print(query_set[0])



    # products = Product.objects.filter(title="product-0").annotate(new_id=F("product_id"))
    # print(products[0].new_id)

    # ------------------------------ Aggregation ------------------------------ 
    # proper way of counting all objects of a table
    # count = Product.objects.aggregate(Count('pk'))
    
    # # what if we use description ?
    # count = Product.objects.aggregate(Count('description'))
    
    # # keyword
    # count = Product.objects.aggregate(count=Count('product_id'), min_price=Min('price'), max_price=Max('price'))

    # print(f"count: {count}")
    
    # ------------------------------ Annotate ------------------------------ 
    # QuerySet.annotate() received non-expression(s): True.
    # products = Product.objects.annotate(is_available=Value(True))
    # products = Product.objects.select_related('collection').prefetch_related('promotion').annotate(is_available=Value(True))

    # string concatenation
    # customers = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    # print(f"customers: {list(customers)}")

    # Count orders of customer
    # customers = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('price') * 0.8, output_field=DecimalField())
    # products = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )
    # print(products)

    # generic models
    # content_type = ContentType.objects.get_for_model(Product)
    # TaggedItem.objects.select_related('tag').filter(
    #     content_type=content_type,
    #     object_id=1
    # )

    # product = Product.objects.get(title='product-0')
    # t = TaggedItem(content_object=product, tag='test')
    # get_tags_for(Product, 1)

    
    # count = Product.objects.filter().count()
    # aggregate: تجمیع شده
    # from django.db.models import Count, Min, Max, Avg, Sum
    # count = Product.objects.aggregate(
    #     Count('product_id') 
    # )

    # group by collection 
    
    # collection 0 pro 1
    # collection 0 pro 2
    # collection 0 pro 3

    # collection 1 pro 4
    # collection 1 pro 5

    # first, last, sum, count, addTolist, avg, min, max
    
    # count = Product.objects.filter(collection_id=1).aggregate(
    #     count=Count('product_id'), 
    #     sum=Sum('price'), 
    #     min_price=Min('price') , 
    #     max_price=Max('price')
    # )

    # # https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/aggregates/
    # # select_related oneToOne and OneToMany 
    # p = Product.objects.select_related('collection').filter(collection_id=1, price=int(count.get('max_price')))
    
    # print("-----------------------")
    # for item in p:
    #     # query to db for each item
    #     print(item.collection.title)

    # {'count': , 'min_price': ?}    
    # {'product_id__count': 100}

    # 
    from django.db.models import Value
    from django.db.models.functions import Concat

    # products = Product.objects.filter(title="product-0").annotate(
    #     new_id=Concat(Value("asghar"), Value(" "), F("product_id")) 
    # )

    # from .customers import *
    # https://www.guru99.com/sqlite-database.html
    # import just variables in __all__

    # a, *b, c = [1, 2, 3, 4]
    # print(b)

    # d = dict(name='ali', age=12)
    # d = {'name':'ali', 'age':12}

    # h = {**d, 'school': 'A'}
    # print(h)
    # # {'name':'ali', 'age':12, 'school': 'A'}

    # h.update(city='varamin')
    # # {'name':'ali', 'age':12, 'school': 'A', 'city': 'varamin'}

    # k = 'town'
    # h.update(k='varamin')
    # # {'name':'ali', 'age':12, 'school': 'A', 'city': 'varamin', 'k': 'varamin'}

    # h[k] = 'varamin'
    # # {'name':'ali', 'age':12, 'school': 'A', 'city': 'varamin', 'k': 'varamin', 'town': 'varamin'}
    # -----------------------------------------------------

    # def do(*args, **kwargs):
    #     # args: ('ali', ), tuple
    #     # kwargs: {'name': 'ali'}, dict
        
    #     # **kwargs.get('name')

    #     print(", ".join(args))
    #     print(kwargs.get('name'))
    #     pass


    # do(name='ali')
    # do('ali')

    # objects: Manager
    # .filter
    # .all
    # .aggregate
    # .annotate
    # .filter_with_fullname()

    # customers = Customer.objects.annotate(
    #     full_name=Concat(F('first_name'), Value(' '), F('last_name')
    # ))

    # Customer.objects = CustomerManager()

    # repr()
    # eval("print('mohammad')")

    customers = CustomerProxy.objects.filter_with_fullname(first_name="ali")
    # customers = Customer.objects.filter(first_name="ali")

    print("------------------------------------")
    for customer in customers:
        print(customer.full_name)
        print(customer.my_full_name)
        print(str(customer))
        # print(f"repr(customer): {repr(customer)}")
        # c = eval(repr(customer))
        

    # print(c.first_name)

    # products = list(queryset)
    return render(request, 'product.html', context={'products': list(products), 'count': count})
