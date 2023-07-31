from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from Bookland.accounts.validators import validate_only_alphabetical


class BooklandUser(AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    MAX_LEN_GENDER = 6
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    address = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    phone_number = models.IntegerField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=MAX_LEN_GENDER,
        null=True,
        blank=True,
        choices=GENDER,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
