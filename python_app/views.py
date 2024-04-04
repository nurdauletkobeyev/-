from django.shortcuts import render
from .models import Book
def books_page(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, "./books_page.html", context)
