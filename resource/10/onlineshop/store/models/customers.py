from django.db import models
from store.enums import MembershipChoices 

__all__ = ('Customer', 'Address', 'CustomerProxy')

class CustomerManager(models.Manager):
    
    # def filter(self, *args, **kwargs):
    #     pass
    # from django.db import models
    # from.django.db.models import F, Value
    # from django.db.models.functions import Concat

    def filter_with_fullname(self, *args, **kwargs):
        # Customer.objects.filter()
        # self.filter()
        # Customer.objects.filter()
        return self.filter(**kwargs).annotate(
            full_name=models.functions.Concat(models.F('first_name'), models.Value(' '), models.F('last_name')
        ))


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

    class Meta:
        ordering = ["-first_name", "last_name"]

    # manager
    # objects = CustomerManager()

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

    @property
    def my_full_name(self):
        # Why? Can be calculated from other fields
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.my_full_name}"

    __repr__ = __str__

    # def __repr__(self):
    #     return f"{self}"


class CustomerProxy(Customer):

    class Meta(Customer.Meta): 
        # The default ordering for the object, for use when obtaining lists of objects:
        # Customer.objects.filter().order_by("-birth_date")
        # ordering = ['-birth_date']
        # ordering = Customer.Meta.ordering + ['-birth_date']
        proxy = True

    # manager
    objects = CustomerManager()


# Customer.objects.filter()
# MyCustomer.objects.filter()

# A ----------> B
# A ---> C ---> B

# class CustomerManager(models.Manager):
    
#     # def filter(self, *args, **kwargs):
#     #     pass
#     # from django.db import models
#     # from.django.db.models import F, Value
#     # from django.db.models.functions import Concat

#     def filter_with_fullname(self, *args, **kwargs):
#         # Customer.objects.filter()
#         # self.filter()
#         Customer.objects.filter()

#         return self.filter(**kwargs).annotate(
#             full_name=models.functions.Concat(models.F('first_name'), models.Value(' '), models.F('last_name')
#         ))

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



# from django.db import models

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True
#         ordering = ['name']

# class Unmanaged(models.Model):
#     class Meta:
#         abstract = True
#         managed = False

# class Student(CommonInfo, Unmanaged):
#     home_group = models.CharField(max_length=5)

#     class Meta(CommonInfo.Meta, Unmanaged.Meta):
#         pass