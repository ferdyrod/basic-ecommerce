from django.contrib import admin

from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductImage


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)