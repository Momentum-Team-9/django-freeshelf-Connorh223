from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="books"
    )
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<Book title=(self.title)>"
    
    def __str__(self):
        return self.title




class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"