from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    # https://django-filter.readthedocs.io/en/stable/ref/filterset.html

    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            # 'title': ['icontains'],
            'unit_price': ['gt', 'lt']
        }