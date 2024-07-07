from django.contrib import admin
from store.admin  import ProductAdmin
from tag.models import TaggedItem
from store.models import Product
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 0

class CustomerProductAdmin(ProductAdmin): 
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)