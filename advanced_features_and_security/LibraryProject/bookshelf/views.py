from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    # logic for adding a book
    return render(request, "bookshelf/add_book.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")
