from django.contrib import admin

from .models import Order, ShippingStatus

class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['order_id', ]
        return self.readonly_fields


class ShippingStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = ShippingStatus


admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingStatus, ShippingStatusAdmin)
