from django.db import models
from django.conf import settings
from store.enums import MembershipChoices 

__all__ = ('Customer', 'Address', 'CustomerProxy')

class CustomerManager(models.Manager):
    # Customer.objects.filter()

    def active_customer(self, *args, **kwargs):
        return self.filter(is_active=True, **kwargs)

    def filter_with_fullname(self, *args, **kwargs):
        return self.filter(**kwargs).annotate(
            full_name=models.functions.Concat(models.F('first_name'), models.Value(' '), models.F('last_name')
        ))


"""
auth.User

# concreate 
Profile <-> User

-------------------------------
# ingeritance
extend User

User(AbstractUser)
change authentication method
email(unique)
"""

class Customer(models.Model):
    phone = models.CharField(max_length=254)
    membership = models.CharField(
        max_length=1, 
        choices=MembershipChoices.choices, 
        default=MembershipChoices.BRONZE
    )
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering = ["-user__first_name", "user__last_name"]

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

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

    def __str__(self):
        return f"{self.customer}-{self.city}-{self.street}"

    __repr__ = __str__