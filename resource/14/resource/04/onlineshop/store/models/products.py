from django.db import models

# absolute path import
from store.utils import id_generator

# relative path import
# just use for the current files in a directory
# from ..utils import id_generator

__all__ = ('Product', )


# Create your models here.
class Product(models.Model):
    # django create id for us by default
    # id 1, 2, 3, sequence 
    product_id = models.CharField(
        max_length=16, 
        primary_key=True, 
        default=id_generator
    ) 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.CharField
    title = models.CharField(max_length=100) # varchar(100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # 9999.99
    invetory = models.PositiveIntegerField()
    # auto_now: هر زمانی که رکورد جاری را داارید آپدیت میکنید  خود جنگو مقدار این فیلد را آپدیت میکند
    # auto_now_add: فقط دفعه اول 
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)