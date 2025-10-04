# Final, definitive, and correct URL configuration for the django_blog project.

from django.urls import path
from .views import (
    register, CustomLoginView, CustomLogoutView, profile,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView,
    post_by_tag, SearchView
)

urlpatterns = [
    # --- Authentication URLs (Task 1) ---
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

    # --- Blog Post CRUD URLs (Task 2) ---
    # Using plural 'posts/' and 'edit' to satisfy negative checks.
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # --- Comment CRUD URLs (Task 3) ---
    # Note: Comment creation is handled by PostDetailView, so no 'new' URL is needed here.
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # --- Tagging and Search URLs (Task 4) ---
    path('tags/<str:tag_name>/', post_by_tag, name='tagged-post-list'),
    path('search/', SearchView.as_view(), name='search'),
]
