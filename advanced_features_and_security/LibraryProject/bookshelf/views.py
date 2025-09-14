from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm
from django.db.models import Q
from .forms import ExampleForm

# List all books
# Lists all books - safe because Django auto-escapes output in templates
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Add book view (protected by permissions)
# Add book view - protected with permissions and CSRF token
@permission_required("bookshelf.add_book", raise_exception=True)  # Only users with 'add_book' permission can access
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST) # Using Django Form automatically validates and sanitizes input
        if form.is_valid():  # Validates & sanitizes input
            form.save() # ORM saves safely, preventing SQL injection
            return redirect('bookshelf:book_list')
    else:
        form = BookForm()
 # CSRF token is included in the template to prevent CSRF attacks
    return render(request, 'bookshelf/form_example.html', {'form': form})


# Delete book view (protected by permissions)
@permission_required("bookshelf.delete_book", raise_exception=True) # Only users with 'delete_book' permission can delete
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Safe way to fetch or return 404 if not found
    book.delete()
    return redirect("bookshelf:book_list")


# Example of safe search using Django ORM
# Search view - uses ORM filters instead of raw SQL to prevent SQL injection
def search_books(request):
    query = request.GET.get('q', '').strip() # Strip whitespace and sanitize user input
    results = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    ) if query else Book.objects.none()
    
    return render(request, 'bookshelf/book_list.html', {'books': results})
