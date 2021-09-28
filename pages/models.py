from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    is_resolved = models.BooleanField(default=False)
    contacted_at = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = ('contact')
        verbose_name_plural = ('contacts')


    def __str__(self):
        return self.email    