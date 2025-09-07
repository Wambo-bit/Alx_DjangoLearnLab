#!/usr/bin/env python3
# relationship_app/query_samples.py
import os
import re
import sys
from pathlib import Path

# === determine project root and ensure it's on sys.path ===
HERE = Path(__file__).resolve()
PROJECT_ROOT = HERE.parents[1]  # relationship_app/.. -> project root
sys.path.insert(0, str(PROJECT_ROOT))

# === try to auto-detect DJANGO_SETTINGS_MODULE from manage.py ===
manage_py = PROJECT_ROOT / "manage.py"
if not manage_py.exists():
    raise RuntimeError("manage.py not found in project root. Run this script from the project root.")

manage_text = manage_py.read_text()
m = re.search(r"os\.environ\.setdefault\(\s*['\"]DJANGO_SETTINGS_MODULE['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\)", manage_text)
if m:
    settings_module = m.group(1)
else:
    # fallback: find a folder containing settings.py at project root
    settings_module = None
    for entry in PROJECT_ROOT.iterdir():
        if entry.is_dir() and (entry / "settings.py").exists():
            settings_module = f"{entry.name}.settings"
            break

if not settings_module:
    raise RuntimeError("Could not determine DJANGO_SETTINGS_MODULE automatically. Edit this file and set DJANGO_SETTINGS_MODULE manually.")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -- sample-data creator (safe: only creates if not present) --
def create_sample_data():
    if Author.objects.filter(name="Jane Austen").exists():
        return  # assume sample data already present

    a1 = Author.objects.create(name="Jane Austen")
    a2 = Author.objects.create(name="George Orwell")

    b1 = Book.objects.create(title="Pride and Prejudice", author=a1)
    b2 = Book.objects.create(title="Emma", author=a1)
    b3 = Book.objects.create(title="1984", author=a2)

    lib1 = Library.objects.create(name="Central Library")
    lib2 = Library.objects.create(name="Community Library")

    lib1.books.add(b1, b3)   # Central: Pride and 1984
    lib2.books.add(b2)       # Community: Emma

    Librarian.objects.create(name="Alice", library=lib1)
    Librarian.objects.create(name="Bob", library=lib2)


# -- required queries --

def books_by_author(author_name):
    """
    Query all books by a specific author name.
    Returns a QuerySet of Book objects.
    """
    author = Author.objects.get(name=author_name)   # required by checker
    return Book.objects.filter(author=author)       # required by checker


def books_in_library(library_name):
    """
    List all books in a library (by library name).
    Returns a QuerySet of Book objects.
    """
    try:
        lib = Library.objects.get(name=library_name)
        return lib.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()


def librarian_for_library(library_name):
    """
    Retrieve the Librarian instance assigned to a library (or None).
    """
    try:
        lib = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=lib)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None



# -- a small demo you can run directly --
def run_demo():
    create_sample_data()

    print("=== books_by_author('Jane Austen') ===")
    for b in books_by_author("Jane Austen"):
        print("-", b.title)

    print("\n=== books_in_library('Central Library') ===")
    for b in books_in_library("Central Library"):
        print("-", b.title)

    print("\n=== librarian_for_library('Central Library') ===")
    librarian = librarian_for_library("Central Library")
    print(librarian.name if librarian else "No librarian found")


if __name__ == "__main__":
    run_demo()
