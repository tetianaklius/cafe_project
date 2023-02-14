from django.contrib import admin

from django.contrib import admin
from .models import Category, Dish, Events, About, Chefs, Gallery, Reservation, Contacts

# admin.site.register(Reservation)


@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    model = Reservation
    list_display = ["name", "phone", "persons", "message", "is_processed"]
    list_editable = ["is_processed"]


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish

    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc', 'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']

    list_filter = ['category', 'is_visible']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events

    list_display = ['title', 'position', 'is_visible', 'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']
    list_filter = ['is_visible']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ['title']


@admin.register(Chefs)
class AdminChefs(admin.ModelAdmin):
    model = Chefs

    list_display = ['name', 'position', 'is_visible', 'desc', 'photo']
    list_editable = ['position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery


admin.site.register(Contacts)

