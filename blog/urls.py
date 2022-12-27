from django.urls import path
from . import views


# authenticate

urlpatterns = [

    path('add-comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('list-posts/', views.list_posts, name='list'),
    path('detail-posts/<slug:slug>/', views.detail_posts, name='detail'),
    path('create-posts/', views.create_posts, name='create'),
    path('delete-posts/<slug:slug>/', views.delete_posts, name='delete'),
    path('edit-posts/<slug:slug>/', views.edit_posts, name='edit'),
    path('save-posts/', views.save_posts, name='save'),
    # path('login/', views.login_request, name='login'),
    # path('register/', views.register_request, name='register'),
    # path('logout/', views.logout_request, name='logout'),
    # path('', views.index, name='preview'),
    # path('preview/', generate_preview, name='generate'),
    # path('tag/<slug:slug>/', tagged, name='tagged'),
]