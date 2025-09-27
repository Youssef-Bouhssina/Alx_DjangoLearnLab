from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    """
    Tests for the Book API endpoints.
    """
    def setUp(self):
        """
        Set up the test data.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', author=self.author, publication_year=2022)

    def test_list_books(self):
        """
        Ensure we can list all books.
        """
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a new book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a new book.
        """
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a single book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book', 'author': self.author.id, 'publication_year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Ensure we can filter books by publication year.
        """
        Book.objects.create(title='Another Book', author=self.author, publication_year=2023)
        url = reverse('book-list') + '?publication_year=2022'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        """
        Ensure we can search for books by title.
        """
        Book.objects.create(title='Another Book', author=self.author, publication_year=2023)
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_order_books(self):
        """
        Ensure we can order books by title.
        """
        Book.objects.create(title='A New Book', author=self.author, publication_year=2023)
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A New Book')
