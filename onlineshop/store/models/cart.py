import uuid
from random import choice
from django.db import models
from django.core.validators import MinValueValidator
from .products import Product

__all__ = ('Cart', 'CartItem')


def my_uuid():
    namespace = choice(
        [uuid.NAMESPACE_DNS, uuid.NAMESPACE_DNS, uuid.NAMESPACE_X500])
    name = str(uuid.uuid4())

    return uuid.uuid5(namespace=namespace, name=name)


class Cart(models.Model):
    # 16 digits
    # "lkdsh-sdasds-asdasd-asdasd"
    # GUID -> globally unique identifier
    id = models.UUIDField(primary_key=True, default=my_uuid)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    __repr__ = __str__


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['product', 'cart']]

    def __str__(self):
        return f"{self.product}-{self.cart}"

    __repr__ = __str__
