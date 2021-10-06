from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.cats_list, name='cats_list'),
    path('cat/<int:pk>', views.cat_detail, name='cat_detail'),
] 

