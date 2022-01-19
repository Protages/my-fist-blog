from django.urls import path, include
from django.contrib.auth import urls

from .views import Registration


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', Registration.as_view(), name='registration'),
]