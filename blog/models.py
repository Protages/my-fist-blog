from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    text = models.TextField(help_text='Напишите что-нибудь..', verbose_name='Текст')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, 
        null=True, blank=True, related_name='posts', verbose_name='Категория'
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
        ordering=['-create_date', 'title']


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edit_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')
    comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='comments',
        blank=True, null=True, verbose_name='Комментарий к комментарию'
    )

    def __str__(self):
        return f'{self.author}'

    class Meta:
        ordering = ['-create_date', 'author']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        