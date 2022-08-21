
from django.db import models
from .products import Product

__all__ = ('Cart', 'CartItem')


class Cart(models.Model):
    # created_at
    placed_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    placed_at = models.DateTimeField(auto_now_add=True)
