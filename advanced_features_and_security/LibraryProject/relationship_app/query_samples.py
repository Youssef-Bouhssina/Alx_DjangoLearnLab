import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create some sample data
def create_sample_data():
    # Authors
    author1 = Author.objects.create(name="Author One")
    author2 = Author.objects.create(name="Author Two")

    # Books
    book1 = Book.objects.create(title="Book A", author=author1)
    book2 = Book.objects.create(title="Book B", author=author1)
    book3 = Book.objects.create(title="Book C", author=author2)
    book4 = Book.objects.create(title="Book D", author=author2)

    # Libraries
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2, book3)
    library2 = Library.objects.create(name="Branch Library")
    library2.books.add(book4)

    # Librarians
    librarian1 = Librarian.objects.create(name="Librarian John", library=library1)
    librarian2 = Librarian.objects.create(name="Librarian Jane", library=library2)

    print("Sample data created successfully.")

# Query functions
def query_books_by_author(author_name):
    print(f"\n--- Books by {author_name} ---")
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"- {book.title}")

def list_books_in_library(library_name):
    print(f"\n--- Books in {library_name} ---")
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"- {book.title} by {book.author.name}")

def retrieve_librarian_for_library(library_name):
    print(f"\n--- Librarian for {library_name} ---")
    library = Library.objects.get(name=library_name)
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"- {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

if __name__ == "__main__":
    create_sample_data()
    query_books_by_author("Author One")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("Branch Library")
