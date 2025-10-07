from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ for tagging support

# Form for creating/updating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags
        widgets = {
            'tags': TagWidget(),  
        }

# Form for comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
