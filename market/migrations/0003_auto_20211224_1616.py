# Generated by Django 3.1.7 on 2021-12-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20211224_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsool',
            name='userid',
            field=models.IntegerField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
