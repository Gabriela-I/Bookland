# Generated by Django 3.2.20 on 2023-08-11 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_auto_20230811_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='phone_number',
            field=models.CharField(default='', max_length=14, validators=[django.core.validators.MinValueValidator(14)]),
        ),
    ]
