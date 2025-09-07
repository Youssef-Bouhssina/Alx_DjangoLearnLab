import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create some data to work with
author1 = Author.objects.create(name='J.K. Rowling')
author2 = Author.objects.create(name='George R.R. Martin')

book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
book2 = Book.objects.create(title='A Game of Thrones', author=author2)
book3 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author1)

library1 = Library.objects.create(name='Downtown Library')
library1.books.add(book1, book3)

library2 = Library.objects.create(name='Uptown Library')
library2.books.add(book2)

librarian1 = Librarian.objects.create(name='John Doe', library=library1)

# Query all books by a specific author
print('Books by J.K. Rowling:')
books_by_author = Book.objects.filter(author__name='J.K. Rowling')
for book in books_by_author:
    print(f'- {book.title}')

# List all books in a library
print('\nBooks in Downtown Library:')
books_in_library = library1.books.all()
for book in books_in_library:
    print(f'- {book.title}')

# Retrieve the librarian for a library
print(f'\nLibrarian for {library1.name}:')
print(f'- {library1.librarian.name}')
