from django.urls import path
from book.views import home, index, book_detail


urlpatterns = [
    path("list/", home, name="home"),
    path("", index, name="index"),
    path("details/<str:id>/", book_detail, name="book_detail"),
]
