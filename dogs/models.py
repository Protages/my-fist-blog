from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=150, verbose_name='Описание')
    text = models.TextField(verbose_name='Полное описание')
    image = models.ImageField(upload_to='dogs/img/', default='dogs/img/default.jpg' , blank=True, null=True, verbose_name='Картинка')

    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Собака'
        verbose_name_plural='Собаки'
        ordering=['name']