# Generated by Django 5.0.7 on 2024-07-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_alter_carmodel_price_alter_carmodel_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(choices=[('Universal', 'Universal'), ('HatchBack', 'Hatchback'), ('SUV', 'Suv'), ('Wagon', 'Wagon'), ('Coupe', 'Coupe')], default='SUV', max_length=10),
            preserve_default=False,
        ),
    ]
