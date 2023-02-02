from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Dish


def main(request):
    categories = Category.objects.all()
    return render(request, "menu.html", context={
        "categories": categories
    })

