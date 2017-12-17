from django.contrib import admin
from .models import Product, Category, ProductImage, ImageElement, SiteImage, Warehouse, Box, Theme
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    inlines = [
        ProductImageInline,
    ]

class ProductInline(admin.TabularInline):
    model = Product

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Warehouse)
admin.site.register(Box)
admin.site.register(SiteImage)
admin.site.register(ProductImage)
admin.site.register(ImageElement)
admin.site.register(Theme)

