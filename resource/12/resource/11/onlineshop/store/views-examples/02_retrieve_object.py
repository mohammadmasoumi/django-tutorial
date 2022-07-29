from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import *

__all__ = ('product_view', )


def product_view(request):
    # variables
    count = 0
    products= []

    # fetch one element from database
    # [Caution]: might raise exception if requested object doesn't exist
    try:
        product = Product.objects.get(id=1) # this line doesn't hit the database
    except ObjectDoesNotExist:
        pass

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

