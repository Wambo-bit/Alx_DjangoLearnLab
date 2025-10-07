# Django Blog Authentication System

## Overview
This module implements user authentication features for the Django Blog, including registration, login, logout, and profile management.

## Features
- **Registration**: Users can create an account with username, email, and password.
- **Login/Logout**: Django’s built-in authentication system handles user sessions.
- **Profile Management**: Logged-in users can view and update their email.

## Security
- All forms include `{% csrf_token %}` for CSRF protection.
- Passwords are hashed using Django’s `PBKDF2` algorithm.
- Profile pages are protected with `@login_required`.

## URLs
| URL Path | View Function | Description |
|-----------|----------------|-------------|
| `/register/` | `register_view` | Create a new user |
| `/login/` | `login_view` | Log in user |
| `/logout/` | `logout_view` | Log out user |
| `/profile/` | `profile_view` | View and update profile |

## Testing
1. Run `python manage.py runserver`.
2. Open `/register/` to create a new account.
3. Test login/logout.
4. Access `/profile/` to edit user email.
