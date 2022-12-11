from django.urls import path

from . import views

# authenticate

urlpatterns = [
    path('list-posts/', views.list_posts, name='list'),
    path('create-posts/', views.create_posts, name='create'),
    path('delete-posts/', views.delete_posts, name='delete'),
    path('edit-posts/', views.edit_posts, name='edit'),
    path('save-posts/', views.save_posts, name='save'),
]
