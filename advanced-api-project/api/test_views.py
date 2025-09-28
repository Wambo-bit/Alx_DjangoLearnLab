from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create an author and a book
        self.author = Author.objects.create(name="George Orwell", birth_year=1903)
        self.book = Book.objects.create(
            title="1984",
            author=self.author,
            publication_year=1949
        )

        # Endpoints
        self.list_url = "/books/"
        self.detail_url = f"/books/{self.book.id}/"
        self.create_url = "/books/create/"
        self.update_url = f"/books/{self.book.id}/update/"
        self.delete_url = f"/books/{self.book.id}/delete/"

    # -----------------
    # CRUD TESTS
    # -----------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Animal Farm", "author": self.author.id, "publication_year": 1945}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Animal Farm", "author": self.author.id, "publication_year": 1945}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Nineteen Eighty-Four", "author": self.author.id, "publication_year": 1949}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # -----------------
    # FILTERING / SEARCHING / ORDERING
    # -----------------
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Orwell")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_order_books_by_publication_year(self):
        Book.objects.create(
            title="Animal Farm",
            author=self.author,
            publication_year=1945
        )
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(
            response.data[0]["publication_year"],
            response.data[1]["publication_year"]
        )
