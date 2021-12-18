# Generated by Django 3.1 on 2021-12-18 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20211219_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsool',
            name='code',
            field=models.PositiveIntegerField(default=43545, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)], verbose_name='کد محصول توسط سیستم تعیین می شود'),
        ),
    ]