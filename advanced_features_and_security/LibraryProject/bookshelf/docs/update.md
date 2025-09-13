# Update

**Command run in Django shell:**

```python
book.title = "Nineteen Eighty-Four"
book.save()
updated = Book.objects.get(pk=book.pk)
print(updated.title)
```

**Expected output (comment):**

```
# Nineteen Eighty-Four
```
