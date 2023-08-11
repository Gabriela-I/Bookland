from django.utils import timezone

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.urls import reverse

from Bookland.authors.models import Author

UserModel = get_user_model()


class Book(models.Model):
    MIN_PRICE = 1
    CONDITION = (
        ('', '-------'),
        ('Perfect', 'Perfect'),
        ('Good', 'Good'),
        ('Not very good', 'Not very good'),
    )

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


class MyList(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )


class BookComment(models.Model):
    MAX_TEXT_LENGTH = 400
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,

    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
