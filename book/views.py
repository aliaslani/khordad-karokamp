from django.shortcuts import render, HttpResponse
from book.models import Author, Book


def index(request):
    return HttpResponse("Home Page")


def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book/booklist.html", context)


def book_detail(request, id):
    book = Book.objects.filter(id=id).first()
    context = {"book": book}
    return render(request, "book/book_detail.html", context)
