from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# These serializes the book model instance
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#These validate the publication year to make sure it is not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cant be in the future"
            )    
        return value
    
# Author model serializer and nested book serializer to serialize the related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id, name, books')