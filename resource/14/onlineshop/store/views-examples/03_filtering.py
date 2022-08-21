from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import *

__all__ = ('product_view', )


def product_view(request):
    # variables
    count = 0
    products= []

    # filtering elements
    query_set = Product.objects.filter(price=20)

    # How about filtering products which have their price are greater than 20
    # query_set = Product.objects.filter(price>20) # ???
    # `filter()` is a function, so you should pass parameters
    # python tries to evaluate `price>20` expression, so it will search for `price` variable in module.
    # `filter(price>20)` == `filter(True/False)`


    # product = Product.objects.get(pk=1) # django automatically reference to the model's primary key

    """
    # ********************* fetching one element ********************* 

    # 1. `.get()`
    try:
        # In case object doesn't exist, raise `ObjectDoesNotExist` exception
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist: # or Product.DoesNotExist 
        # exception handling 
        pass

    # 2. `.filter()`
    # In case object doesn't exist, returm `None`
    product = Product.objects.filter(pk=1).first()

    # ********************* check existance of an element ********************* 
    # Return `True` or `False`
    product = Product.objects.filter(pk=1).exists()
    """

    return render(request, 'product.html', context={'products': list(products), 'count': count})

