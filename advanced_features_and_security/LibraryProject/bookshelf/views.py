from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


@permission_required('bookshelf.can_view_book', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        book = Book(title=title, author=author)
        book.save()
        return redirect('view_books')
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        book.title = title
        book.author = author
        book.save()
        return redirect('view_books')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_book',raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method =='POST':
        book = book.object.get(pk=pk)
        book.delete()
        return redirect('view_books')   
    return render(request, 'bookshelf/delete_book.html', {'book': book})
