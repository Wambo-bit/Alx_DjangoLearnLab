# Delete

**Command run in Django shell:**

```python
pk = updated.pk
updated.delete()
Book.objects.filter(pk=pk).exists()
```

**Expected output (comment):**

```
# False
# or: [] when listing Book.objects.all()
```
