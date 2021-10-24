from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=150, verbose_name='Описание')
    text = models.TextField(verbose_name='Полное описание')
    years = models.PositiveIntegerField(verbose_name='Продолжительность жизни')
    picture_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='cats/img/', null=True, blank=True, verbose_name='Картинка')

    def get_absolute_url(self):
        return reverse('cat_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Кошка'
        verbose_name_plural='Кошки'
        ordering=['name']