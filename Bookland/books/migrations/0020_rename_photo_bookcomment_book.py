# Generated by Django 3.2.20 on 2023-08-10 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20230810_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcomment',
            old_name='photo',
            new_name='book',
        ),
    ]