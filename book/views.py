from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1 style='color: red; text-align:center;'>Hello</h1>")
