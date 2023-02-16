from django.db import models
from django.core.validators import RegexValidator

from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField()
    sup_desc = models.TextField(max_length=500, blank=True)
    point_text_1 = models.TextField(max_length=200, blank=False)
    point_text_2 = models.TextField(max_length=200, blank=False)
    point_text_3 = models.TextField(max_length=200, blank=False)
    inf_desc = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='events', blank=False)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

    def __iter__(self):
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


class About(models.Model):
    title = models.CharField(max_length=100)
    sup_desc = models.TextField(max_length=2000, blank=False)
    check_double_text_1 = models.TextField(max_length=200, blank=False)
    check_double_text_2 = models.TextField(max_length=200, blank=False)
    check_double_text_3 = models.TextField(max_length=200, blank=False)
    inf_desc = models.TextField(max_length=2000, blank=False)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='about/%y_%m_%d', blank=False)

    def __str__(self):
        return "About"


class WhyUs(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    subtitle = models.CharField(max_length=200, unique=True, db_index=True)

    desc_1 = models.TextField(max_length=200, blank=False)
    desc_2 = models.TextField(max_length=200, blank=False)
    desc_3 = models.TextField(max_length=200, blank=False)


class Reservation(models.Model):
    phone_validator = RegexValidator(regex=r"^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$", message="Error in phone number")

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.phone}"

    class Meta:
        ordering = ("-date", )


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=False)
    # gallery_desc = models.TextField(max_length=300, blank=True)


class Chefs(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True, blank=True)
    com_desc = models.TextField(max_length=200, blank=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    name = models.TextField(max_length=100, blank=False)
    desc = models.TextField(max_length=200, blank=False)
    photo = models.ImageField(upload_to='collective', blank=False)

    def __str__(self):
        return f'{self.name}'


class Contacts(models.Model):
    phone = models.TextField(max_length=20, blank=False)
    phone_add = models.TextField(max_length=20, blank=True)
    address = models.TextField(max_length=200, blank=False)
    email = models.TextField(max_length=50, blank=False)
    email_add = models.TextField(max_length=50, blank=False)
    socials = models.TextField(max_length=100, blank=True)
    add_information = models.TextField(max_length=500, blank=True)
    sub_title = models.TextField(max_length=500, blank=True)
    open_days_1 = models.TextField(max_length=150, blank=False)
    open_hours_1 = models.TextField(max_length=50, blank=False)
    open_days_2 = models.TextField(max_length=150, blank=True)
    open_hours_2 = models.TextField(max_length=50, blank=True)


class Testimonials(models.Model):
    author = models.TextField(max_length=70, blank=False)
    author_desc = models.TextField(max_length=500, blank=False)
    quote = models.TextField(max_length=2000, blank=False)
    photo = models.ImageField(upload_to='testimonials', blank=False)

    def __str__(self):
        return f'{self.author}'

