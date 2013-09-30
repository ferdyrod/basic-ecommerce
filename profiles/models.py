from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    stripe_id = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.user)


class Address(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(null=True, blank=True, max_length=120)
    address1 = models.CharField(max_length=300, default="")
    address2 = models.CharField(null=True, blank=True, max_length=300, default="")
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    default_address = models.BooleanField(default=False)
    billing_address = models.BooleanField(default=True)
    shipping_address = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Address')
        verbose_name_plural = ('Addresses')

    def __unicode__(self):
        return self.address1
