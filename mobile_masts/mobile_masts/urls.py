from django.contrib import admin
from django.urls import include, path
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web_app/', include('web_app.urls')),
]
