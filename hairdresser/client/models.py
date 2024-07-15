from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, max_length=100)
    
