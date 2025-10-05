from django.urls import path
from book.views import (
    home,
    index,
    book_detail,
    create_book,
    create_category,
    create_author,
)


urlpatterns = [
    path("list/", home, name="home"),
    path("", index, name="index"),
    path("details/<str:id>/", book_detail, name="book_detail"),
    path("book/new/", create_book, name="new_book"),
    path("category/new/", create_category, name="new_category"),
    path("author/new/", create_author, name="new_author"),
]
