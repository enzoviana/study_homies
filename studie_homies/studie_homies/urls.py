from django.contrib import admin
from django.urls import path, include
from django import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('base.url')),
]



