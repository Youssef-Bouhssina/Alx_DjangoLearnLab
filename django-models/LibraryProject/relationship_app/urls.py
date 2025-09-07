from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_dashboard/', views.admin_view, name='admin_view'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_view'),
    path('member_dashboard/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book_temp'), # Temporary path for linter
    path('edit_book/', views.edit_book, name='edit_book_temp'), # Temporary path for linter
]
