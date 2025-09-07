from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class BookForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, label="Author Name")

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'publication_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.author:
            self.initial['author_name'] = self.instance.author.name

    def save(self, commit=True):
        author_name = self.cleaned_data.pop('author_name')
        author, created = Author.objects.get_or_create(name=author_name)
        self.instance.author = author
        return super().save(commit=commit)
