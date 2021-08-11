from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.User, name='User'),
    path('Usershow', views.Usershow, name='Usershow'),
    path('addUser', views.addUser, name='addUser'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]

