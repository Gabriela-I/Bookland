# Generated by Django 3.2.20 on 2023-08-11 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0025_auto_20230811_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='seller_requests', to='accounts.booklanduser'),
            preserve_default=False,
        ),
    ]
