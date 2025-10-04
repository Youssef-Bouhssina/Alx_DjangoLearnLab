from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that includes the email field.
    """
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    """
    A custom form for updating user profile information.
    Allows users to update their username and email.
    """
    password = None  # Exclude the password field

    class Meta:
        model = User
        fields = ('username', 'email')
