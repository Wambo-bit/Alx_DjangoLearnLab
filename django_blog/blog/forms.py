from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Add tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
