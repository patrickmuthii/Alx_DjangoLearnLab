from .models import Book, Author, Library, Librarian 

#query all books by specific authors

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

#quert list all books in a library

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = Book.all()
    return books

#Retrieve the Libraian for a librry

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian