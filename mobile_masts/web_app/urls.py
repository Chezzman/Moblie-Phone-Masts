from django.urls import re_path, path
from . import views

urlpatterns = [
#     path('home/', views.index, name='index'),
    path('', views.table, name='table'),
    path('create/', views.create, name='create'),
    path('total_rent/', views.total_rent, name='total_rent')

]
