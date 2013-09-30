from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=220)
    description = models.CharField(blank=True, null=True, max_length=3000)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=100)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ['-title', ]

    def __unicode__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='product/images/')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ('ProductImage')
        verbose_name_plural = ('ProductImages')

    def __unicode__(self):
        return str(self.image)
