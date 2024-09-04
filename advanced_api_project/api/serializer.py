from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


#This serialises the Book model 
# it also validates that the publication year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future")    

#This serialises the Author model
# it also includes the name of the books written by the author
class AuthorSerializer(serializers.ModelSerializer):
    Book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'Book')       