# Generated by Django 4.0.3 on 2022-03-10 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product2_promotionproduct_product2_promotion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotionproduct',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='promotionproduct',
            name='promotion_id',
        ),
        migrations.DeleteModel(
            name='Product2',
        ),
        migrations.DeleteModel(
            name='PromotionProduct',
        ),
    ]
