# Delete

from bookshelf.models import Book

# Retrieve the Book instance with the title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()

(1, {'bookshelf.Book': 1})

# No output from the `delete()` method. The book is deleted from the database.
