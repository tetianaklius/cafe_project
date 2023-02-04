from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Dish, Menu, Events, About, WhoWeAre


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']


class CategoryInMenu(admin.TabularInline):                                     # нове
    model = Category
    raw_id_fields = ['menu']


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


@admin.register(Menu)                                                     # нове
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [CategoryInMenu]
    list_display = ['title', 'is_visible']
    list_editable = ['is_visible']
    list_filter = ['is_visible']


@admin.register(Events)                                                     # нове
class EventsAdmin(admin.ModelAdmin):
    model = Events

    list_display = ['title', 'position', 'is_visible', 'desc', 'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']
    list_filter = ['is_visible']


@admin.register(About)                                                     # нове
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ['title']


@admin.register(WhoWeAre)                                                     # нове
class AdminWhoWeAre(admin.ModelAdmin):
    model = WhoWeAre

    list_display = ['name', 'position', 'is_visible', 'desc', 'photo']
    list_editable = ['position', 'is_visible']
    list_filter = ['is_visible']



