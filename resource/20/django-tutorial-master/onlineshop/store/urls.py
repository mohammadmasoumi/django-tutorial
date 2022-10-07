from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers
# from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = routers.DefaultRouter()

# /store/products
# /store/products/1/
# nested router - https://github.com/alanjds/drf-nested-routers
# /store/products/1/reviews
# /store/products/1/reviews/1/
# /store/products/1/reviews/2/
# /store/products/{product_pk}/reviews/{pk}/

# 'domain-nameservers-detail'
# 'domain-nameservers-list'

# /store/carts/{cart_pk}/items/{pk}

#                prefix               viewset,    basename

# products/ GET POST
# products/1/ GET PUT PATCH DELETE
router.register('products', viewset=ProductViewSet, basename='products')
router.register('collections', viewset=ProductViewSet, basename='collections')
router.register('carts', viewset=CartViewSet, basename='carts')
router.register('customers', viewset=CustomerViewSet, basename='customers')

product_nested_router = routers.NestedDefaultRouter(router, r'products', lookup='product') # /products/{product_pk}
product_nested_router.register('reviews', ReviewViewSet, basename='product-review' ) # /product/{product_pk}/reviews/{pk}

cart_nested_router = routers.NestedDefaultRouter(router, r'carts', lookup='cart')
cart_nested_router.register('items', CartItemViewSet, basename='cart-item' ) 

# urlpatterns = router.urls + nested_router.urls

urlpatterns = [
    # path('product', product_view),
    # product/{product_id}
    # my-product/22?collection_id=22
    # view: method = ProductView.as_view()
    # kwrgs = {"rest_id": 22}
    # vie'w(**kwargs) 
    # path('success', success_view, name="success-product"),
    # path('my-product/<slug:asghar_id>', ProductDetailView.as_view()),
    # path('my-product-list/', ProductListView.as_view(), name="product-list"),
    # path('my-product-list/<str:page>', ProductListView.as_view()),
    # path('my-product-create/', ProductCreateView.as_view()),
    # path('my-product/<slug:asghar_id>/update', ProductUpdateView.as_view()),
    # path('my-product/<slug:asghar_id>/delete', ProductDeleteView.as_view()),
    path("", include(router.urls)),
    path("", include(product_nested_router.urls)),
    path("", include(cart_nested_router.urls))
    # path("product/", product_list),
    # path("product2/", ProductList.as_view()),
    # path("product3/", ProductListCreateAPIView.as_view()),
    # path("product2/<int:id>", ProductDetails.as_view()), # Post, Get, Patch, Pug, Delete, list
    # path("product/<int:id>", product_details), # Post, Get, Patch, Pug, Delete, list
    # path("product/<str:id>", product_details2),
]

