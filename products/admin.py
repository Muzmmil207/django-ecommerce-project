from django.contrib import admin
from .models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock', 'is_active', 'updated']
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    