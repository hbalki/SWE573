from django.urls import path
from . import views


urlpatterns = [
    path('my-profile', views.my_profile_request, name='show_me'),
    path('my-friends', views.friends_request, name='friends'),
]
