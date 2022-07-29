from django.shortcuts import render
from django.db import transaction
from store.models import *
from tags.models import *

__all__ = ('product_view', )


# use as a decorator
@transaction.atomic()
def product_view(request):

    # use as a context manager
    with transaction.atomic():
        order = Order()
        # order.customer = Customer
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        # set product_id to -1 
        item.product_id = 1
        item.quantity = 1
        item.price_unit = 10
        item.save()

    return render(request, 'empty.html')
