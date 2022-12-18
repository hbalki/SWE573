from django.urls import path
from . import views
from .views import login_request, logout_request, register_request

urlpatterns = [
    path('/login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),

]