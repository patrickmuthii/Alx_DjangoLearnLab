from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# These serializes the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# This is uded to validate the  publication year to make sure that the date is not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError(
                'Publication year cannot be in the future'
            
            )    
        return value

# These serializes the Author model with the Book model 
class AuthorSerializer(serializers.ModelSerializer):
    Book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'Book')
