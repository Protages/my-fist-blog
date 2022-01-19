from os import name
from django.urls import path, include
from django.contrib.auth import views

from .views import Registration, Profile, PasswordChangeDoneView


urlpatterns = [
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', include('django.contrib.auth.urls')),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/', Profile.as_view(), name='profile'),
]