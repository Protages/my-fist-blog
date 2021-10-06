from django.urls import path
from . import views

urlpatterns = [
    path('', views.dogs_list, name='dogs_list'),
    path('dog/<int:pk>', views.dog_detail, name='dog_detail'),
]