from django.shortcuts import render
from .models import Book, Author, Librarian
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
