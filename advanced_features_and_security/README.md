# Advanced Features and Security in Django

## Custom User Model
- Extended `AbstractUser` with `date_of_birth` and `profile_photo`.

## Permissions and Groups
- Added custom permissions: `can_create`, `can_delete`.
- Applied permission decorators in views (`add_book`, `delete_book`).

## Running the Project
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`
