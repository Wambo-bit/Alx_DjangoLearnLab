## Blog Post Management

### Features
- Create, read, update, and delete (CRUD) blog posts.
- Only authenticated users can create posts.
- Only post authors can edit or delete their posts.
- Public access to post list and details.

### Key Files
- `blog/views.py` – Contains CRUD views.
- `blog/forms.py` – Defines `PostForm` (if used).
- `blog/urls.py` – Maps URLs to CRUD views.
- `blog/templates/blog/` – HTML templates for CRUD actions.

### Usage
1. Log in or register.
2. Go to `/posts/new/` to create a post.
3. View posts at `/`.
4. Edit or delete your posts through the post detail page.

## Comment Functionality

### Features
- Users can comment on blog posts.
- Comments are displayed under each post.
- Only authenticated users can create comments.
- Authors can edit or delete their own comments.

### Files
- `models.py` → Defines `Comment` model.
- `forms.py` → Contains `CommentForm`.
- `views.py` → CRUD views for comments.
- `urls.py` → Routes for adding/editing/deleting comments.
- `templates/blog/` → Comment-related templates.

### Permissions
- Only comment authors can edit/delete.
- All users can read comments.
- Non-authenticated users cannot comment.
