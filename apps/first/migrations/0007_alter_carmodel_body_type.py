# Generated by Django 5.0.7 on 2024-08-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(choices=[('Universal', 'Universal'), ('HatchBack', 'Hatchback'), ('SUV', 'Suv'), ('Wagon', 'Wagon'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan')], max_length=10),
        ),
    ]
