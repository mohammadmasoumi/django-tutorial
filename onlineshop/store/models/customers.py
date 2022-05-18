from django.db import models
from store.enums import MembershipChoices 

__all__ = ('Customer', 'Address', 'CustomerProxy')

class CustomerManager(models.Manager):
    def filter_with_fullname(self, *args, **kwargs):
        return self.filter(**kwargs).annotate(
            full_name=models.functions.Concat(models.F('first_name'), models.Value(' '), models.F('last_name')
        ))


class Customer(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    membership = models.CharField(
        max_length=1, 
        choices=MembershipChoices.choices, 
        default=MembershipChoices.BRONZE
    )
    birth_date = models.DateField(null=True)

    class Meta:
        ordering = ["-first_name", "last_name"]

    @property
    def my_full_name(self):
        # Why? Can be calculated from other fields
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.my_full_name}"

    __repr__ = __str__


class CustomerProxy(Customer):
    class Meta: 
        proxy = True

    objects = CustomerManager()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)    
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    __repr__ = __str__