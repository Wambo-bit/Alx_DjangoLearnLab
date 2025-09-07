from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import all views from the app

urlpatterns = [
    # Book list
    path('books/', views.book_list, name='book_list'),

    # Library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User registration and authentication
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-specific views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book CRUD operations (with permissions)
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
