from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Book
from django import forms

# Form for Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# List view for books - anyone can view the list
class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'

# Detail view for a single book - requires view permission
class BookDetailView(PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'bookshelf/book_detail.html'
    context_object_name = 'book'
    permission_required = 'bookshelf.can_view'

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to view book details.')
        return redirect('book_list')

# Create view for adding a new book - requires create permission
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to create books.')
        return redirect('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

# Update view for editing a book - requires edit permission
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_edit'

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to edit books.')
        return redirect('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

# Delete view for removing a book - requires delete permission
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_delete'

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to delete books.')
        return redirect('book_list')

# Function view example with permission check
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Implementation details would go here
    return render(request, 'bookshelf/edit_book.html', {'book': book})
