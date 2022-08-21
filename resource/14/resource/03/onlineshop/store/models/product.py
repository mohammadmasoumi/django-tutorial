import string
import random
from django.db import models

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


# Create your models here.
class Product(models.Model):
    # django create id for us by default
    # id 1, 2, 3, sequence 
    product_id = models.CharField(primary_key=True, default=id_generator) 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.CharField
    title = models.CharField(max_length=100) # varchar(100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # 9999.99
    invetory = models.PositiveIntegerField()
    # auto_now: هر زمانی که رکورد جاری را داارید آپدیت میکنید  خود جنگو مقدار این فیلد را آپدیت میکند
    # auto_now_add: فقط دفعه اول 
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
