from django.urls import path
from .views import BooklistView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('books', BooklistView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

]
