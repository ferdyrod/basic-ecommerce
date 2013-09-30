from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from profiles.models import Address


STATUS_CHOICES = (
    ('Starded', 'Starded'),
    ('Abandoned', 'Abandoned'),
    ('Collected', 'Collected'),
)


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User)
    cart = models.ForeignKey(Cart)
    order_id = models.CharField(default="ABC123", max_length=120)
    status = models.CharField(default="Starded", max_length=50, choices=STATUS_CHOICES)
    address = models.ForeignKey(Address, null=True, blank=True)
    cc_four = models.CharField(null=True, blank=True, max_length=4)

    class Meta:
        verbose_name = ('Order')
        verbose_name_plural = ('Orders')
        ordering = ['-status', '-cart']

    def __unicode__(self):
        return "Order number is %s" % (self.order_id)


SHIPPING_STATUS = (
    ('Shipping soon', 'Shipping Soon'),
    ('Shipped', 'Shipped'),
)


class ShippingStatus(models.Model):
    order = models.ForeignKey(Order)
    status = models.CharField(default="Not Shipped", max_length=120, choices=SHIPPING_STATUS)
    tracking_number = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = ('Shipping Status')
        verbose_name_plural = ('Shipping Statuses')

    def __unicode__(self):
        return str(self.status)
