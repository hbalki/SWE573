from django.urls import path
from . import views

# authenticate

urlpatterns = [
    path('index', views.blog, name='blog'),
]