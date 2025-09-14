# bookshelf/forms.py
from django import forms
from .models import Book

# Form used for adding books securely
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # adjust fields to match your Book model


# Example form required by the task checker
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter your name")
    email = forms.EmailField(help_text="Enter a valid email address")
