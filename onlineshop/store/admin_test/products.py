from django.contrib import admin
from store.models.products import Promotion, Collection, Product


# called it everything. 
# by convension ModelName+Admin
# solution2
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # display list
    list_display = [
        'title', 'unit_price'
    ]



# solution1
# admin.site.register(Product, ProductAdmin)
admin.site.register(Promotion)
admin.site.register(Collection)