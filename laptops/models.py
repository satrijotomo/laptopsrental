from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptopmodel = models.CharField(max_length=70, blank=False, default='')
    serialno = models.CharField(max_length=50, blank=False, default='')
    image_path = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=300, blank=False, default='')
    owner = models.BooleanField(default=False)
