import os
import sys
import django

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.LibraryProject.settings")  # replace LibraryProject with your project folder name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(Author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == "__main__":
    # Example usage (requires data in DB)
    print("Books by Jane Austen:")
    for book in books_by_author("Jane Austen"):
        print("-", book.title)

    print("\nBooks in Central Library:")
    for book in books_in_library("Central Library"):
        print("-", book.title)

    print("\nLibrarian for Central Library:")
    print(librarian_for_library("Central Library"))
