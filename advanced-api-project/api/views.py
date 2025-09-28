# api/views.py
from rest_framework import generics, permissions, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # if you created api/filters.py
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.
# 1. List all books
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Supports:
     - Filtering (title, author name, publication_year, year ranges)
     - Searching (title and author name)
     - Ordering (title, publication_year, author name)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # backends: order matters only for evaluation; include all three
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]

    # use the custom FilterSet for advanced filtering (range filters etc.)
    filterset_class = BookFilter

    # text search (SearchFilter) — performs a search across these fields
    search_fields = ['title', 'author__name']

    # fields allowed for ordering
    ordering_fields = ['title', 'publication_year', 'author__name']

    # default ordering
    ordering = ['title']


# 2. Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 3. Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        # Custom behavior: log creation
        print(f"Book created: {serializer.validated_data['title']}")
        serializer.save()




# 4. Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom behavior: log update
        print(f"Book updated: {serializer.validated_data['title']}")
        serializer.save()



# 5. Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all books.
    Accessible to everyone (no authentication required).
    """
    ...
