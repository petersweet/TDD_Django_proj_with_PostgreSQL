from django.db import models

# Create your models here.
class Publisher (models.Model):
    """Publisher of some article"""
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.title, self.country

class Author (models.Model):
    """Author of some story"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_adress = models.EmailField()

    def __str__(self):
        return self.first_name, self.last_name, self.email_adress

class Article (models.Model):
    """Body of some article"""

    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)