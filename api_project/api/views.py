# api/views.py
from rest_framework import generics, viewsets
#from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated  # for list view


class BookList(generics.ListAPIView):
    """
    GET /api/books/ -> returns list of books as JSON
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Book:
      - list:    GET    /api/books_all/
      - retrieve:GET    /api/books_all/<pk>/
      - create:  POST   /api/books_all/
      - update:  PUT    /api/books_all/<pk>/
      - partial: PATCH  /api/books_all/<pk>/
      - destroy: DELETE /api/books_all/<pk>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAdminOrReadOnly]
 # dev: public; change for production
