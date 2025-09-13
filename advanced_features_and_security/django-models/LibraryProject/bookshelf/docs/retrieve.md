# Retrieve

**Command run in Django shell:**

```python
book = Book.objects.get(pk=b.pk)  # where b is the created object
print(book.title, book.author, book.publication_year)
```

**Expected output (comment):**

```
# 1984 George Orwell 1949
```
