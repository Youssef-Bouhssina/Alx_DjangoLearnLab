from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    """
    This test suite evaluates the Book API endpoints, covering CRUD operations,
    permissions, and advanced query features like filtering, searching, and ordering.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        This method is run once for the entire test class.
        """
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.author = Author.objects.create(name='Test Author')
        cls.book1 = Book.objects.create(title='Book A', author=cls.author, publication_year=2022)
        cls.book2 = Book.objects.create(title='Book B', author=cls.author, publication_year=2023)

    def test_list_books_unauthenticated(self):
        """
        Ensure any user (authenticated or not) can list all books.
        """
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_unauthenticated(self):
        """
        Ensure any user can retrieve a single book.
        """
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book A')

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a new book.
        """
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2024}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a new book.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2024}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Book A', 'author': self.author.id, 'publication_year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book A')

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        """
        Test filtering the book list by publication year.
        """
        url = reverse('book-list') + '?publication_year=2022'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book A')

    def test_search_books_by_title(self):
        """
        Test searching the book list by title.
        """
        url = reverse('book-list') + '?search=Book A'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book A')

    def test_order_books_by_title(self):
        """
        Test ordering the book list by title.
        """
        url = reverse('book-list') + '?ordering=-title' # Descending order
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book B')
