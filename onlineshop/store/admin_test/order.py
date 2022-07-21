from django.contrib import admin
from store.models.order import Order, OrderItem


admin.site.register(Order)
admin.site.register(OrderItem)
