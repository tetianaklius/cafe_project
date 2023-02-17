from django.urls import path
from .views import main, update_reservation, list_reservations

app_name = "main_page"

urlpatterns = [
    path("", main, name="main_path"),
    path("manager/update_reserve/<int:pk>", update_reservation, name="update_reservation"),
    path("manager/reserve_list/", list_reservations, name="list_reservations"),

]


