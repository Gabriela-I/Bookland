# Generated by Django 3.2.20 on 2023-08-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_auto_20230811_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='phone_number',
            field=models.CharField(default='', max_length=14),
        ),
    ]
