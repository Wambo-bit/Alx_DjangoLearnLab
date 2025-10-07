📝 Django Blog Project

A full-featured Django blog application with user authentication, CRUD for posts, comments, tags, and search.
Built with simplicity, clarity, and scalability in mind.

⚡ Quick Start
1️⃣ Clone the Repository
git clone https://github.com/Wambo-bit/django-blog.git
cd django-blog
2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
pip install django django-taggit
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a Superuser
python manage.py createsuperuser
6️⃣ Run the Development Server
python manage.py runserver

✍️ Blog Post Management
Features

Create, read, update, and delete (CRUD) blog posts.

Only authenticated users can create posts.

Only post authors can edit or delete their posts.

Public access to post list and details.

Key Files

blog/views.py – Contains CRUD views.

blog/forms.py – Defines PostForm.

blog/urls.py – Maps URLs to CRUD views.

blog/templates/blog/ – HTML templates for CRUD actions.

Usage

Log in or register.

Go to /posts/new/ to create a post.

View posts at /.

Edit or delete your posts through the post detail page.

💬 Comment Functionality
Features

Users can comment on blog posts.

Comments are displayed under each post.

Only authenticated users can create comments.

Authors can edit or delete their own comments.

Files

models.py → Defines Comment model.

forms.py → Contains CommentForm.

views.py → CRUD views for comments.

urls.py → Routes for adding/editing/deleting comments.

templates/blog/ → Comment-related templates.

Permissions

Only comment authors can edit/delete.

All users can read comments.

Non-authenticated users cannot comment.

🏷️ Tagging and 🔍 Search Functionality
Features

Add multiple tags to each blog post.

Tags are clickable — view all posts sharing the same tag.

A search bar allows users to search by title, content, or tags.

🏷️ Adding Tags During Post Creation

When creating or editing a blog post:

Go to "New Post".

Enter your title and content.

In the tags field, type tags separated by commas (e.g., django, python, webdev).

Submit to save your post.

✅ Each tag appears under your post. Clicking a tag shows all posts with that tag.

🔍 Using the Search Bar

You can search for posts by keywords or tags:

Locate the search bar at the top of the posts page.

Enter a word or phrase (e.g., Django, Tutorial, Python).

Press Enter to view all matching posts.

💡 The search checks post titles, content, and tags.

👩‍💻 Author

Mary Muthima Wambui
ALX Django LearnLab Project
📧 muthimamary@gmail.com
🌐 https://marymuthima.vercel.app/  

