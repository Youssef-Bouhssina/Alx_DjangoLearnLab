from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookList(generics.ListCreateAPIView):
    """
    API view to retrieve a list of books or create a new book.
    - GET: Returns a list of all books.
    - POST: Creates a new book.
    Permissions:
    - Read-only access is allowed for unauthenticated users.
    - Write access is restricted to authenticated users.
    Filtering, Searching, and Ordering:
    - Filter by 'title', 'author', and 'publication_year'.
    - Search by 'title' and 'author__name'.
    - Order by 'title' and 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a book instance.
    - GET: Retrieves a single book by its ID.
    - PUT/PATCH: Updates a book instance.
    - DELETE: Deletes a book instance.
    Permissions:
    - Read-only access is allowed for unauthenticated users.
    - Write access is restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorList(generics.ListCreateAPIView):
    """
    API view to retrieve a list of authors or create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
