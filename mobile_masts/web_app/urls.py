from django.urls import re_path, path
from . import views

urlpatterns = [
#     path('home/', views.index, name='index'),
    path('', views.table, name='table'),
    path('create/', views.create, name='create'),
    path('date_list', views.date_list, name='date_list'),
    path('table_five', views.table_five, name='table_five'),
    path('total_rent/', views.total_rent, name='total_rent'),
    path('dictionary/' views.dictionary, name='dictionary')

]
