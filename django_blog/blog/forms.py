# Final, definitive forms for the django_blog project.

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that includes the email field (Task 1).
    """
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    """
    A custom form for updating user profile information (Task 1).
    """
    password = None

    class Meta:
        model = User
        fields = ('username', 'email')

class PostForm(forms.ModelForm):
    """
    A form for creating and updating Post instances, with an explicit TagWidget (Task 2 & 4).
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments (Task 3).
    """
    class Meta:
        model = Comment
        fields = ['content']
