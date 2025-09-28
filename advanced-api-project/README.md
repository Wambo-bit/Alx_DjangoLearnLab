# 📘 Advanced API Project – Django REST Framework

This project demonstrates advanced **Django REST Framework (DRF)** usage with **custom serializers, nested relationships, generic views, and permissions**.  
It is part of the **Alx_DjangoLearnLab** exercises.

---

## 🚀 Features

- **Custom Models**
  - `Author` – represents a writer with a `name`.
  - `Book` – represents a book with `title`, `publication_year`, and a foreign key to `Author`.

- **Custom Serializers**
  - `BookSerializer` – validates publication year (cannot be in the future).
  - `AuthorSerializer` – includes nested books dynamically.

- **Generic Views**
  - List all books
  - Retrieve a single book
  - Create a new book
  - Update an existing book
  - Delete a book

- **Permissions**
  - Anyone can **read** (`GET` requests).
  - Only authenticated users can **create, update, or delete**.

---

## 📂 Project Structure

