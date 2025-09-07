from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # API URLs
    path('api/books/', views.BookListCreate.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view(), name='book-detail-update-delete'),
]
