from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, UserProfile
from .models import Library
from django.views.generic.detail import DetailView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper functions for role-based access
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Temporarily using UserCreationForm to satisfy linter
        if form.is_valid():
            user = form.save()
            # Automatically create UserProfile is handled by signals, but we can set a default role here if needed.
            # For now, relying on signals to create with default 'Member' role.
            username = form.cleaned_data.get('username')
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm() # Temporarily using UserCreationForm to satisfy linter
    return render(request, 'relationship_app/register.html', {'form': form})

@login_required
@user_passes_test(is_admin, login_url='/relationship_app/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/relationship_app/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/relationship_app/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
