# CRUD Operations Documentation

## Create Operation

### Objective
To create a new book entry in the `bookshelf` app.

### Commands and Output

1. **Open the Django shell:**
   ```bash
   python manage.py shell

# Create.md

from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# No direct output from the `create()` method, but the book entry is added to the database.
# You can verify its creation using the retrieve operation.

# Retrieve.md

from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")

# Print book details
print(book.title, book.author, book.publication_year)

# Output: 1984 George Orwell 1949


# Update.md

from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# No direct output from the `save()` method. The book's title is updated to "Nineteen Eighty-Four".
# Confirm the update by performing a retrieve operation.

# Delete.md

from bookshelf.models import Book

# Retrieve the Book instance with the title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()

(1, {'bookshelf.Book': 1})

# No output from the `delete()` method. The book is deleted from the database.
