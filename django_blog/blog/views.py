from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy

def register(request):
    """
    Handles user registration. If the request method is POST and the form is valid,
    it saves the new user and logs them in before redirecting to the profile page.
    Otherwise, it displays an empty registration form.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    """
    Allows an authenticated user to view and update their profile.
    If the request method is POST and the form is valid, it updates the user's
    information. Otherwise, it displays the current user's information in a form.
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

class CustomLoginView(LoginView):
    """
    Custom login view that uses a specific template.
    Redirects to the profile page upon successful login.
    """
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('profile')

class CustomLogoutView(LogoutView):
    """
    Custom logout view that redirects to the login page after logout.
    """
    next_page = reverse_lazy('login')
