from django.db import models

# Create your models here.
# Author model stores information about book authors.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name
    birth_year = models.IntegerField(null=True, blank=True)  # Author's birth year

    def __str__(self):
        return self.name


# Book model stores individual books and links each book to an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(
        Author,
        related_name='books',   # Enables reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
