
from django.db import models
from .products import *
from .customers import *

__all__ = ('Order', 'OrderItem')



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # created_at
    placed_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    # 9999.99
    # max_digits 999999
    # decimal_places = .99
    price_unit = models.DecimalField(max_digits=6, decimal_places=2)
    placed_at = models.DateTimeField(auto_now_add=True)
