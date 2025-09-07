from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.
# Function-based view: list all books
def list_books(request):
    """
    Renders a simple list of all books and their authors.
    Uses the template 'relationship_app/list_books.html'.
    """
    books = Book.objects.select_related('author').all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: show details for a library and its books
class LibraryDetailView(DetailView):
    """
    DetailView for Library.
    Exposes the library instance as 'library' in the template context.
    Template: relationship_app/library_detail.html
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    # optional: override get_context_data if you want to provide books explicitly
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["books"] = self.object.books.select_related("author").all()
        return ctx
