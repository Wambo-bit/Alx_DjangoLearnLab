# Create

**Command run in Django shell:**

```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
```

**Expected output (comment):**

```
# 1984 (1949) by George Orwell
```
