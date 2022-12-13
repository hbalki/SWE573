"""
mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog.views import contact
from preview.views import index, generate_preview
from login.views import login_request, register_request, logout_request


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('login.urls'), name='users'),
    path('posts/', include('blog.urls'), name='posts'),
    path('profile/', include('profile.urls'), name='profile'),
    path('contact/', contact, name='contact'),
    path('preview/', generate_preview, name='preview'),
    path('login', login_request, name='login'),
    path('register', register_request, name='register'),
    path('logout', logout_request, name='logout'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
