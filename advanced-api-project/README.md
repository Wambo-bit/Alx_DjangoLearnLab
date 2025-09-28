# 📚 Advanced API Project – Django REST Framework

This project is part of the **Alx_DjangoLearnLab** repo and demonstrates advanced API development using **Django** and **Django REST Framework (DRF)**.  
It focuses on building a flexible API with **custom serializers, generic views, permissions, filtering, searching, and ordering**.

---

## 🚀 Features Implemented

### ✅ Phase 0: Project Setup
- Created a new Django project: `advanced_api_project`
- Added app: `api`
- Installed and configured **Django REST Framework**
- Created `Author` and `Book` models with relationships
- Implemented custom serializers with nested relationships and validation

### ✅ Phase 1: Custom & Generic Views
- Added **generic views** for the Book model:
  - List all books (`/api/books/`)
  - Retrieve a book by ID (`/api/books/<id>/`)
  - Create a book (`/api/books/create/`)
  - Update a book (`/api/books/update/<id>/`)
  - Delete a book (`/api/books/delete/<id>/`)
- Applied **permission classes**:
  - Authenticated users can create, update, delete
  - Anonymous users have read-only access

### ✅ Phase 2: Filtering, Searching, and Ordering
- Integrated **django-filter** package
- Implemented:
  - Filtering by `title`, `author`, `publication_year`
  - Searching across `title` and `author`
  - Ordering by `title` and `publication_year`

### ✅ Phase 3: Unit Testing
- Added automated tests for API endpoints
- Verified CRUD operations, filtering, searching, ordering
- Ensured authentication & permission rules are enforced

---


## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Wambo-bit>/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/advanced-api-project
