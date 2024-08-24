# from .models import Book, Author, Library, Librarian 

# #query all books by specific authors

# def get_books_by_author(author_name):
#     author = Author.objects.get(name=author_name)
#     books = Book.objects.filter(author=author)
#     return books

# #quert list all books in a library

# def get_books_in_library(library_name):
#     library = Library.objects.get(name=library_name)
#     books = books.all()
#     return books

# #Retrieve the Libraian for a librry

# def get_librarian_for_library(library_name):
#     library = Library.objects.get(name=library_name)
#     librarian = Librarian.objects.get(library=library)
 #   return librarian


from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.
author_name = "author.name"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books: by {author.name}")
for book in books:
    print(f" -{book.title}")


#List all books in a library.
library_name = "library.name"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library.name}: ")
for book in books:
    print(f" -{book.title}").objects.all()


#Retrieve the librarian for a library
librarian_name = "librarian.name"
librarian = Librarian.objects.get(library=librarian_name)
library = librarian.library
for librarian in library:
    print(f"Librarian: {librarian.name}) for ({library.name})")
