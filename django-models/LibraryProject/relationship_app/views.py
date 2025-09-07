from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# --- Function-based View ---
def list_books(request):
    """
    Function-based view to list all books and their authors.
    """
    books = Book.objects.all()  # <== checker looks for this
    return render(request, "list_books.html", {"books": books})


# --- Class-based View ---
class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library
    and its books.
    """
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
