from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#  serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#These ensure that the publication year is not in the future

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError('Publication year must be in the past')
        return value

#serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    Books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'books')
