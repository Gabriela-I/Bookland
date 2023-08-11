# Generated by Django 3.2.20 on 2023-07-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20230725_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('Perfect', 'Perfect'), ('Good', 'Good'), ('Not very good', 'Not very good')], default='uncategorized', max_length=13),
        ),
    ]