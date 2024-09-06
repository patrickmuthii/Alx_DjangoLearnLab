from django.shortcuts import render
from django_restframework import generics
from .models import Book
from rest_framework import generics, filters
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
#these is used for filterin g to allow the user to search,order or filter books by title, author, or publication year    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fiels = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']

#DetailView for retrieving a single book by ID

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#VIEW for creating anew book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

#VIEW for updating an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

#VIEW for deleting an existing book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]    
