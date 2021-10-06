from django.conf import settings
from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    text = models.TextField()
    years = models.PositiveIntegerField()
    picture_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='cats/img/', null=True, blank=True)

    def __str__(self):
        return self.name