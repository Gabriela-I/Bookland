from django.core.exceptions import ValidationError


def validate_only_alphabetical(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError('The username must contain only letters!')


def upper_first_letter(value):
    if not value[0].isupper():
        raise ValidationError('The first letter must be capitalized')


def start_with_plus(value):
    if not value[0] == '+':
        raise ValidationError('The first symbol must be "+"!')