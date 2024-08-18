# Admin Interface Configuration

## Objective
Configure the Django admin interface to manage the `Book` model effectively.

## Steps Taken

1. **Register the `Book` Model:**
   - Modified `bookshelf/admin.py` to register the `Book` model with the Django admin.
   
   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       search_fields = ('title', 'author')
       list_filter = ('publication_year',)
