# Create Operation

## Objective
To create a new book entry in the `bookshelf` app.

## Commands and Output

1. **Open the Django shell:**
   ```bash
   python manage.py shell


# Create

from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# No direct output from the `create()` method, but the book entry is added to the database.
# You can verify its creation using the retrieve operation.