from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.templatetags.static import static

from Bookland.accounts.validators import validate_only_alphabetical, upper_first_letter


class BooklandUser(AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    MAX_LEN_GENDER = 6

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_alphabetical, upper_first_letter,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_alphabetical, upper_first_letter,
        ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=MAX_LEN_GENDER,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='mediafiles/profile_photos/',
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
