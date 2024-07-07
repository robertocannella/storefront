from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse

from tag.models import TaggedItem
from . import models
from django.db.models import Count



class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
            ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
      

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    extra = 0
    min_num = 1
    max_num = 10
    model = models.OrderItem
    # prepopulated_fields = {
    #     'unit_price' : ['unit_price']
    # }


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
    list_per_page  = 10
        


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    search_fields = ['title']
    autocomplete_fields = ['collection']
    # exclude = ['promotions']
    # fields = ['title', 'slug']
    list_display = [ 'title' , 'unit_price', 'inventory_status','collection']
    list_editable = ['unit_price']
    list_per_page  = 10
    list_filter = ['collection', 'last_update', InventoryFilter]

    # does not work bec
    prepopulated_fields = {
        'slug' : ['title']
    }

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset:QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.SUCCESS
        )
        
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'membership','orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['last_name', 'first_name']
    search_fields = ['last_name__istartswith', 'first_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer' : str(customer.id)
            })
        )
        return format_html('<a href={}>{}</a>', url, customer.orders_count) 
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )


# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection' : str(collection.id)
            })
            )
        return format_html('<a href={}>{}</a>', url, collection.products_count) 
        
    

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )