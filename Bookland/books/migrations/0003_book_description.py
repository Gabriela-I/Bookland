# Generated by Django 3.2.20 on 2023-07-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20230721_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]