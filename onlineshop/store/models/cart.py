
from django.db import models
from .products import Product

__all__ = ('Cart', 'CartItem')


class Cart(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.placed_at}"

    __repr__ = __str__


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product}-{self.cart}"

    __repr__ = __str__
