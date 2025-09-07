from django.urls import path
from .views import list_books, LibraryDetailView, register, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from django.contrib.auth import views as auth_views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_dashboard/', admin_view, name='admin_view'),
    path('librarian_dashboard/', librarian_view, name='librarian_view'),
    path('member_dashboard/', member_view, name='member_view'),
    path('book/add/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]
