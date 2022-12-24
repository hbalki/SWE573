from django.urls import path
from . import views
from .views import tagged, generate_preview, index

# authenticate

urlpatterns = [

    path('add-comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('list-posts/', views.list_posts, name='list'),
    path('detail-posts/<slug:slug>/', views.detail_posts, name='detail'),
    path('create-posts/', views.create_posts, name='create'),
    path('delete-posts/<slug:slug>/', views.delete_posts, name='delete'),
    path('edit-posts/<slug:slug>/', views.edit_posts, name='edit'),
    path('save-posts/', views.save_posts, name='save'),
    path('tag/<slug:slug>/', tagged, name='tagged'),
]
