from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

#list all books in the database
def list_books(request):
    return render(request, 'list_books.html')

class ListView(request):
    models = Book
    template_name = 'list_books.html'
    return render(request (template_name = 'list_books.html')books = Book.objects.all())

