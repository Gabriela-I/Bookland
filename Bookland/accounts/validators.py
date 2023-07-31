from django.core.exceptions import ValidationError


def validate_only_alphabetical(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError('The username must contain only letters!')