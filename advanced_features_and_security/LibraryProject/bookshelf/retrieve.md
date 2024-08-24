# Retrieve

from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")

# Print book details
print(book.title, book.author, book.publication_year)

# Output: 1984 George Orwell 1949