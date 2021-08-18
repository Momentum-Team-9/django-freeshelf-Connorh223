from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField('Author', related_name='books')
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Author(models.Model):
    name = models.CharField(max_length=150)
    # books = models.ManyToManyField(Book, related_name='authors')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"