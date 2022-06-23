
from django.db import models
from .products import *
from .customers import *
from store.enums import PaymentStatusChoices

__all__ = ('Order', 'OrderItem')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, 
        choices=PaymentStatusChoices.choices, 
        default=PaymentStatusChoices.PENDING
    )

    def __str__(self):
        return f"{self.customer}"

    __repr__ = __str__


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_unit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.product}-{self.order}"

    __repr__ = __str__