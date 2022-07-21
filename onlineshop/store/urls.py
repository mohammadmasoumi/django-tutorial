from django.urls import path
from .views import *

urlpatterns = [
    path('product', product_view),
    # product/{product_id}
    path('my-product/<slug:slug>/', ProdcutDetailView.as_view(), name='product-detail'),
]