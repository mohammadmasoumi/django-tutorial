# Generated by Django 4.0.3 on 2022-03-10 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
            preserve_default=False,
        ),
    ]