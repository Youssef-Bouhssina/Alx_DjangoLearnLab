
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
def create_sample_data():
    # Authors
    author1 = Author.objects.create(name='Author One')
    author2 = Author.objects.create(name='Author Two')

    # Books
    book1 = Book.objects.create(title='Book A', author=author1, publication_year=2000)
    book2 = Book.objects.create(title='Book B', author=author1, publication_year=2005)
    book3 = Book.objects.create(title='Book C', author=author2, publication_year=2010)
    book4 = Book.objects.create(title='Book D', author=author2, publication_year=2015)

    # Libraries
    library1 = Library.objects.create(name='Central Library')
    library1.books.add(book1, book2)
    library2 = Library.objects.create(name='Community Library')
    library2.books.add(book3, book4)

    # Librarians
    Librarian.objects.create(name='Librarian A', library=library1)
    Librarian.objects.create(name='Librarian B', library=library2)

    print("Sample data created!")

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"\nBooks by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(f"- {book.title} by {book.author.name}")

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")

if __name__ == '__main__':
    create_sample_data()
    query_books_by_author('Author One')
    list_books_in_library('Central Library')
    retrieve_librarian_for_library('Community Library')
