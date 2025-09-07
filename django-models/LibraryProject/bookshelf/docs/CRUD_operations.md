# CRUD operations for Book model

## Create
```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
```
# Expected:
# 1984 (1949) by George Orwell

## Retrieve
```python
book = Book.objects.get(pk=b.pk)
print(book.title, book.author, book.publication_year)
```
# Expected:
# 1984 George Orwell 1949

## Update
```python
book.title = "Nineteen Eighty-Four"
book.save()
updated = Book.objects.get(pk=book.pk)
print(updated.title)
```
# Expected:
# Nineteen Eighty-Four

## Delete
```python
pk = updated.pk
updated.delete()
Book.objects.filter(pk=pk).exists()
```
# Expected:
# False
