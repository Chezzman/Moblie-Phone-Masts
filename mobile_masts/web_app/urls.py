from django.urls import re_path, path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),

    path('create/', views.create, name='create')
]
