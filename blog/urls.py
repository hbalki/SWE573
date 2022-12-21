from django.urls import path

from . import views
from .views import generate_preview, index, tagged

# authenticate

urlpatterns = [

    path('add-comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('list-posts/', views.list_posts, name='list'),
    path('detail-posts/<int:pk>/', views.detail_posts, name='detail'),
    path('create-posts/', views.create_posts, name='create'),
    path('delete-posts/<int:pk>/', views.delete_posts, name='delete'),
    path('edit-posts/<int:pk>/', views.edit_posts, name='edit'),
    path('save-posts/', views.save_posts, name='save'),
    path('generate/', generate_preview, name='generate'),
    path('preview/', index, name='preview'),
    path('tag/<slug:tag_slug>/', tagged, name='tagged'),
]
