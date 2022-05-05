from django.shortcuts import render
from store.models import *

__all__ = ('product_view', )


def product_view(request):
    # variables
    count = 0
    products= []

    # fetch all elements from database
    query_set = Product.objects.all() # this line doesn't hit the database
    
    # Chaining filters, django hits the database once
    # query_set = Product.objects.filter().filter().filter().order_by()

    """
    # ********************* lazy loading ********************* 
    # Django evaluates queryset whenever you use it, for instance, casting to list, for loop over it
    
    # Under below circumstances, django evaluates querysets.
    # 1. cast to list
    # print(list(query_set))
    
    # 2. loop over it
    # for product in query_set:
    #     print(property)
    
    # 3. access to one element
    # print(query_set[0])
    
    
    # ********************* queryset caching *********************
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
    

    # ********************* limit & offset *********************
    [Caution]: you can't use negative indexes.
    # 
    # print(query_set[0:5]) # first five elements, offset: 0, limit: 5
    # print(query_set[5:15]) # second five elements, offset: 5, limit: 10
    """

    return render(request, 'product.html', context={'products': list(products), 'count': count})

