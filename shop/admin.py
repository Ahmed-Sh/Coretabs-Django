from django.contrib import admin
from . import models

def make_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)

make_price_zero.short_description = "Make selected products free"

def make_discount(modeladmin, request, queryset):
    for product in queryset:
        new_price = float(product.price)*0.8
    queryset.update(price=new_price)

make_discount.short_description = "Make 20%% Discount"

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category',)
    actions = [make_price_zero, make_discount]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']
    date_hierarchy = 'created_at'


admin.site.site_header = "Coretabs Online Shop Administration"
admin.site.site_title = "Coretabs Online Shop Administration"
admin.site.index_title = ""
