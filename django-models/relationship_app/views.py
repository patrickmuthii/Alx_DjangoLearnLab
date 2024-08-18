from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.views.generic import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
