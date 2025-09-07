
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.models import User

# Create sample data
def create_sample_data():
    # Clear existing data to prevent duplicates
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()
    User.objects.all().delete()
    UserProfile.objects.all().delete()

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

    # Users and UserProfiles
    admin_user = User.objects.create_user(username='admin', password='adminpass')
    UserProfile.objects.filter(user=admin_user).update(role='Admin')

    librarian_user = User.objects.create_user(username='librarian', password='librarianpass')
    UserProfile.objects.filter(user=librarian_user).update(role='Librarian')

    member_user = User.objects.create_user(username='member', password='memberpass')
    UserProfile.objects.filter(user=member_user).update(role='Member')

    print("Sample data created!")

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found.")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian found for '{library_name}'.")

if __name__ == '__main__':
    create_sample_data()
    query_books_by_author('Author One')
    list_books_in_library('Central Library')
    retrieve_librarian_for_library('Community Library')
