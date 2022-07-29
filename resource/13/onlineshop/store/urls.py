from django.urls import path
from .views import *

urlpatterns = [
    path('product', product_view),
    # product/{product_id}
    # my-product/22?collection_id=22
    # view: method = ProductView.as_view()
    # kwrgs = {"rest_id": 22}
    # vie'w(**kwargs) 
    path('success', success_view, name="success-product"),
    path('my-product/<slug:asghar_id>', ProductDetailView.as_view()),
    path('my-product-list/', ProductListView.as_view(), name="product-list"),
    path('my-product-list/<str:page>', ProductListView.as_view()),
    path('my-product-create/', ProductCreateView.as_view()),
    path('my-product/<slug:asghar_id>/update', ProductUpdateView.as_view()),
    path('my-product/<slug:asghar_id>/delete', ProductDeleteView.as_view()),
]

