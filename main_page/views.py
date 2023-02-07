from django.shortcuts import render
# from django.http import HttpResponse
from .models import Category, Dish
from .forms import ReservationForm


def main(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)

    form_reserve = ReservationForm()
    return render(request, "main_page.html", context={
        "categories": categories,
        "dishes": dishes,
        "special_dishes": special_dishes,
        "form_reserve": form_reserve,
    })

