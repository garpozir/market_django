# Generated by Django 3.1 on 2021-12-18 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20211218_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsool',
            name='code',
            field=models.PositiveIntegerField(default=44067, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='کد محصول توسط سیستم تعیین می شود'),
        ),
    ]
