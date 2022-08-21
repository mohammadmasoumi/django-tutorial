from django.urls import path
from .views import *

urlpatterns = [
    path('product', product_view),
    # product/{product_id}
]