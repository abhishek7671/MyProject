from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year_of_publish = models.IntegerField()

    def __str__(self):
        return self.title
