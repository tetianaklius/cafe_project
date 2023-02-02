from django.db import models

import os.path
import uuid

from django.db import models


class Menu(models.Model):                                                            # нове
    title = models.CharField(max_length=30, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Events(models.Model):                                                            # нове
    title = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField()
    desc = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='events', blank=True)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)                               # нове

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

    def __iter__(self):                                                                # нове
        for item in self.dishes.all():
            yield item


class Dish(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    photo = models.ImageField(upload_to='dishes', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes")
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')


class Specials(models.Model):                                                            # нове
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='specials', blank=True)

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class About(models.Model):                                                         # нове
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000, blank=False)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='about/%y_%m_%d', blank=False)

    def __str__(self):
        return "About"


class WhoWeAre(models.Model):                                                         # нове
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    name = models.TextField(max_length=100, blank=False)
    desc = models.TextField(max_length=200, blank=False)
    photo = models.ImageField(upload_to='collective', blank=False)

    def __str__(self):
        return f'{self.name}'



