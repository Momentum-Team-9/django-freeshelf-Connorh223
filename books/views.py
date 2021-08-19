# from books.forms import BookForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import User, Book, Author, Category

# Create your views here.


# Login / Home
def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('list_books')
    return render(request, 'books/index.html', {'users': users})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html',
                {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    else:
        form = BookForm
    return render(request, 'books/add_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    
    return render(request, 'books/delete_book.html', {'book': book})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'books/categories.html', {'categories': categories})

def show_categories(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    books = categories.books.all()

    return render(request, 'books/show_categories.html', {'categories': categories, 'books': books})



# def list_author(request):
#     authors = Author.objects.all()
#     return render(request, 'books/list_author.html', {'authors', authors})

