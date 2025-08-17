from django.db import models
from django.utils import timezone

# Create your models here.

class Contact (models.Model):
    name = models.CharField(max_length= 255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length= 300)
    message = models.TextField(null=False)
    create_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta():
        ordering = ['-create_date']