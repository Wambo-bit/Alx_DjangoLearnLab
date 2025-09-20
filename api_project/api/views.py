# api/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    GET /api/books/ -> returns list of books as JSON
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
