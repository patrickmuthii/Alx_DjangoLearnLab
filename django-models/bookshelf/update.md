# Update

from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# No direct output from the `save()` method. The book's title is updated to "Nineteen Eighty-Four".
# Confirm the update by performing a retrieve operation.
