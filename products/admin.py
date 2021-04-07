from django.contrib import admin
from .models import Product, Category

# Extends built-in model admin class

class ProductAdmin(admin.ModelAdmin):

    # tuple that will tell the admin which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register clasess in their respective models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
