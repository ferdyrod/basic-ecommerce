from django.db import models


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __unicode__(self):
        return 'message from ' + str(self.email)
