from django.db import models

# Create your models here.
import os.path
import uuid

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    # щоб в адмінці відображалася назва категорії, потрібно реалізувати метод str
    def __str__(self):
        return f'{self.title}'

    # щоб в адмінці записи сортувалися, потрібно прописати списком або кортежем атрибути за якими сортуємо
    class Meta:
        ordering = ('position',)


class Dish(models.Model):

    # можна формувати за допогою модуля uuid нове коректне унікальне імя файла,
    # зберігаючи поточне розширення файлу
    # def get_file_name(self, file_name: str):
    #     ext = file_name.strip().split('.')[-1]
    #     new_name = f'{uuid.uuid4()}.{ext}'
    #     return os.path.join('dishes', new_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # upload_to присвоїти стрічку (назву папки)  додає підпапку, в якій будуть зберігатися фотки,
    # можна ще додати такий шаблон 'dishes/%y_%m_%d'- тоді буде створюватися папка, назва якої це поточна дата
    photo = models.ImageField(upload_to='dishes', blank=True)

    # або результат виконання функції, визначеної вище, яка буде формувати імя файла і яка повертає стрічку -
    # photo = models.ImageField(upload_to=get_file_name, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')