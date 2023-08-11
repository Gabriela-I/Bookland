from django.utils import timezone

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from Bookland.accounts.validators import validate_only_alphabetical, upper_first_letter
from Bookland.authors.models import Author
from Bookland.books.validators import start_with_plus

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


class Purchase(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    MIN_LEN_PHONE_NUMBER = 14
    DELIVERY_METHODS = (
        ('FedEx', 'FedEx'),
        ('DHL', 'DHL'),
        ('UPS', 'UPS'),
    )

    PAYMENT_METHODS = (
        ('Cash on Delivery', 'Cash on Delivery'),
    )

    buyer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    seller = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='seller_requests',)

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    purchase_date = models.DateTimeField(
        auto_now_add=True,
    )
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        # validators=(
        #     validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        #     validate_only_alphabetical, upper_first_letter,
        # ),
        default='',
    )

    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        # validators=(
        #     validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
        #     validate_only_alphabetical, upper_first_letter,
        # ),
        default='',
    )

    phone_number = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        # validators=(
        #     validators.MinValueValidator(MIN_LEN_PHONE_NUMBER),
        #     start_with_plus,
        # ),

        default='',
    )

    address_for_delivery = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        default=''
    )

    delivery_method = models.CharField(
        max_length=5,
        choices=DELIVERY_METHODS,
        default=''
    )

    payment_method = models.CharField(
        max_length=16,
        choices=PAYMENT_METHODS,
        default=''
    )
