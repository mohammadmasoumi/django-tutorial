from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from store.models import *


"""
[Table]
product1 -> inventory_quantity(product1)
product2 -> inventory_quantity(product1)
product3 -> inventory_quantity(product1)
product4 -> inventory_quantity(product1)
"""
"""
list comprehenstion

[item * 2 for item in []]
[item * 2 for item in [] if item % 2]
[item // 2 if item % 2 else item * 2 for item in []]
[item for items in [] for item in items]

[lambda] 
anonymous function
map(lambda x: x % 2, [])
"""

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "product_count"]
    list_display_links = ["id"]
    list_editable = ["title"]
    search_fields =  ["title"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("product"))

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        #              admin:APP_MODEL_PAGE
        url = reverse("admin:store_product_changelist") + f"?collection={collection.id}"
        # return f"<a href='{url}'>{collection.product_count}</a>"
        return format_html("<a href='{}'>{}</a>", url, collection.product_count)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta._get_fields(reverse=False)]
    search_fields = ["email"]
    list_display_links = ["email"]
    list_editable = ["first_name", "last_name", "membership"]
    ordering = ["first_name", "-last_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 10 => LOW
    # 10 => HIGH
    list_display = ["id", "title", "slug", "description","unit_price","inventory", "collection","inventory_status","my_collection_id"]
    list_display_links = ["id"]
    list_editable = ["title",]
    search_fields = ["collection"]
    actions = ["clear_inventory"]
    list_select_related = ["collection"]
    list_per_page: int = 10
    list_max_show_all: int = 500 # ?
    
    # create form
    fields = ["title", "slug"] 
    exclude = ["promotion"]
    readonly_fields = ["inventory"]
    prepopulated_fields = {
        "slug": ["title"]
    }
    search_fields = ["collection"]
    autocomplete_fields = ["collection"]


    @admin.action(description="clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, 
            f"{updated_count} products has been successfully updated.",
            messages.SUCCESS
        )

    @admin.display(ordering="inventory")
    def inventory_status(self, product: Product):
        return "LOW" if product.inventory < 10 else "HIGH"

    def my_collection_id(self, product: Product):
        return product.collection.id


# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(Cart)
# admin.site.register(CartItem)
# admin.site.register(Address)

