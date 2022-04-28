from django.db import models
from store.enums import MembershipChoices

"""
Bronze B
Silver S
Golden G
"""

# from .customers import *
# https://www.guru99.com/sqlite-database.html
# import just variables in __all__
__all__ = ('Customer', 'Address')


class Customer(models.Model):
    # MEMBERSHIP_BRONZE = 'B'
    # MEMBERSHIP_SILVER = 'S'
    # MEMBERSHIP_GOLDEN = 'G'

    # MEMBERSHIP_CHOICES = [
    #     # 'B' actual value store in DB
    #     # 'Bronze' human readable in django admin
    #     (MEMBERSHIP_BRONZE, 'Bronze'),
    #     (MEMBERSHIP_SILVER, 'Silver'),
    #     (MEMBERSHIP_GOLDEN, 'Golden')
    # ]

    # snake case
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    membership = models.CharField(
        max_length=1,
        choices=MembershipChoices.choices,
        default=MembershipChoices.BRONZE
    )

    # membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    # null=True/False
    # blank=True/False -> validation
    # blank=False, null=False
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#null
    birth_date = models.DateField(null=True)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # چون آدرس وابسته به کاربر است میاییم آن رابطه را در آدرس تعریف میکنیم
    # Address is related to Customer
    # We do not have Address entity without User entity
    # Parent: User | child: Address
    # We put relation in child
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    # if we delete user, what we should do with address?
    # CASCADE: if we delete user, address will delete automatically

    # on_delete options
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # models.CASCADE
    # اگر کاربر را پاک کنید آدرس هم پاک میشود.
    # models.PROTECT
    # تا آدرس پاک نشوند ااجازه پاک شدن کاربر را نمیدهد
    # اگر کاربر را پاک کنم مقدار فیلد کاستومر در مدل آدرس نال میشود
    # models.SET_NULL
