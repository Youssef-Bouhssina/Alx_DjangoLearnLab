import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

try:
    from bookshelf.models import Book
    print("Successfully imported Book model!")
except Exception as e:
    print(f"Error importing Book model: {e}")
