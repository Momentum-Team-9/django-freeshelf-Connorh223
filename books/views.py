from django.shortcuts import redirect, render
from .models import User, Book, Author, Category

# Create your views here.

def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('list_books')
    return render(request, 'books/index.html', {'users': users})

def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html",
                {"books": books})