from django.db import models
from store.models.products import Product
# from .products import Product
# from . import Product

__all__ = ('Review', )


class Review(models.Model):
    # product.reviews
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=256)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)