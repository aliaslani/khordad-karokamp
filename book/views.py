from django.shortcuts import render, HttpResponse, redirect
from book.models import Author, Book
from book.forms import CategoryForm


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


def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        category = request.POST.get("category")
        pd = request.POST.get("published_date")
        new_book = Book.objects.create(
            title=title, author=author, category=category, pd=pd
        )
        print(new_book)
        return redirect("home")
    else:
        return render(request, "book/new_book.html")


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data()
            print(data)
            return redirect("home")
    form = CategoryForm()
    return render(request, "book/new_category.html", context={"cat_form": form})


def create_author(request):
    return HttpResponse("new author")
