from django.contrib import admin
from django.urls import re_path
from django.urls import path
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
]
