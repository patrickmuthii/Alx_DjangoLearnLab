from django.db import models

# Create your models here.
# created an author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Created a book model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
