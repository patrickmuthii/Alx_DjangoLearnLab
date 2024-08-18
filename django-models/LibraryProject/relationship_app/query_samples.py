from relationship_app.models import Author, Book, Library, librarian

#query all books by a specific author

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books


#list all books by a specific library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

#retrieve the librarian for a library

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian