#from django.shortcuts import render
from .models import Book, Author, Library, Librarian
#from django.views.generic import DetailView
from django.http import HttpResponse

def list_books(request):
    books = Book.objects.all()
    response_text = '\n'.join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_text, content_type='text/plain'



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
