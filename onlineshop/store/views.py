from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import *
from tags.models import *

__all__ = ('product_view', )


def product_view(request):

    return render(request, 'empty.html')
