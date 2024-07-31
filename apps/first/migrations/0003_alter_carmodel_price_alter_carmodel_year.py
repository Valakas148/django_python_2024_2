# Generated by Django 5.0.7 on 2024-07-31 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_carmodel_options_alter_carmodel_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2024)]),
        ),
    ]
