from django.urls import path
from .import views
app_name = "relationship_app"
urlpatterns=[
      # Function-based view: list all books
    path("books/", views.list_books, name="list_books"),

    # Class-based view: library detail by primary key
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]