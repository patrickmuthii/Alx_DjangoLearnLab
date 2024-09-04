from django.db import models

# Create your models here.

#creation of the Author model it stores detail about the author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#craetion of the Book model it stores detail about the book including the publication year
# title and  the author as the foreign key for the Author model  
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    