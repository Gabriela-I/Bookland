from django.utils import timezone

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.urls import reverse

from Bookland.authors.models import Author

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Book(models.Model):
    MIN_PRICE = 1
    CONDITION = (
        ('', '-------'),
        ('Perfect', 'Perfect'),
        ('Good', 'Good'),
        ('Not very good', 'Not very good'),
    )
    # CATEGORIES = (
    #     ('Romance', 'Romance'),
    #     ('Fantasy', 'Fantasy'),
    #     ('Criminal', 'Criminal'),
    #     ('Historical novel', 'Historical novel'),
    #     ('Thriller', 'Thriller'),
    #     ('Science fiction', 'Science fiction'),
    #     ('Poetry', 'Poetry'),
    #     ('Biography/autobiography', 'Biography/autobiography'),
    #     ('Health', 'Health'),
    #     ('Psychology', 'Psychology'),
    #     ('Esoteric', 'Esoteric'),
    #     ('Home, Family, Hobby', 'Home, Family, Hobby'),
    #     ("Children's literature", "Children's literature"),
    #     ('Other', 'Other'),
    # )

    book_photo = models.ImageField(
        upload_to='mediafiles/book_photos/',
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    author = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    publisher = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=100,
        default='uncategorized',
    )

    condition = models.CharField(
        max_length=13,
        choices=CONDITION,
        default='',
        blank=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    upload_date = models.DateTimeField(
        default=timezone.now,
    )

