from django.db import models
from store.utils import id_generator


__all__ = ('Product', )


class Promotion(models.Model):
    descrition = models.TextField()
    discount = models.PositiveIntegerField()


# class PromotionProduct(models.Model):
#     promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)
#     product_id = models.ForeignKey('Product2', on_delete=models.CASCADE)
#     extra_field = models.CharField(max_length=255)


# class Product2(models.Model):
#     promotion = models.ManyToManyField(Promotion, through=PromotionProduct)


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    product_id = models.CharField(
        max_length=16, 
        primary_key=True, 
        default=id_generator
    ) 
    title = models.CharField(max_length=100) # varchar(100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # 9999.99
    invetory = models.PositiveIntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)