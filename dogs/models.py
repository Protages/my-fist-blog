from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='dogs/img/', default='dogs/img/default.jpg' , blank=True, null=True)

    def __str__(self):
        return self.name