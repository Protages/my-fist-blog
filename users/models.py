from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    country = CountryField(verbose_name='Страна')

    class CategoryType(models.TextChoices):
        AUTO = 'Авто'
        ANIMALS = 'Животные'
        POLITICAL = 'Политика'
        ACTORS = 'Актеры'
        MOVIES = 'Фильмы'
        PROGRAMMING = 'Программирование'
        NOTHING = 'Ничего:('

    favorite_category = models.CharField(max_length=50, 
        verbose_name='Любимая категория',
        choices=CategoryType.choices, 
        default=CategoryType.NOTHING
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.get_full_name() if self.get_full_name() else self.username

    def get_absolute_url(self):
        return reverse('show_user_profile', kwargs={'username': self.username})
 
