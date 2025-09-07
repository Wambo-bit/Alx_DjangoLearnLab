from django.urls import path
from .views import book_list, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', book_list, name='book-list'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
