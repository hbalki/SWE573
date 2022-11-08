from django.urls import path
from . import views

# authenticate

urlpatterns = [
    path('index', views.post_list, name='post_list'),
]