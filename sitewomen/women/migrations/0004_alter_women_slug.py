# Generated by Django 4.2.7 on 2023-11-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
