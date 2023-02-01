from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Dish


# варіант адмінки на швидкоруч
# admin.site.register(Category)
# admin.site.register(Dish)

# варіант адмінки, щоб таблиця Dish була вкладена в Category(підпорядкована,вбудована)
# створюємо клас
class DishAdmin(admin.TabularInline):
    model = Dish
    # вказуємо поле привязки - спосок, в якому буде назва поля
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]

    # виводить в рядки в адмінці наступні поля
    list_display = ['title', 'position', 'is_visible']

    # дозволяє редагувати прямо в рядку наступні поля
    list_editable = ['position', 'is_visible']


# можна додати в адмінку таблицю dish ще раз як просту таблицю, а не підпорядковану

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish

    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc', 'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']

    # можна додати панель фільтрів
    list_filter = ['category', 'is_visible']

    # якщо таблиця довга, розбити її на сторінки
    # list_per_page = 2