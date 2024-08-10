# Generated by Django 5.1 on 2024-08-10 19:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('year_established', models.IntegerField(default=1950)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'), ('COUPE', 'Coupe'), ('CONVERTIBLE', 'Convertible'), ('HATCHBACK', 'Hatchback'), ('MINIVAN', 'Minivan'), ('PICKUP', 'Pickup Truck'), ('SPORTS_CAR', 'Sports Car'), ('CROSSOVER', 'Crossover'), ('ELECTRIC', 'Electric Vehicle'), ('HYBRID', 'Hybrid Vehicle'), ('ROADSTER', 'Roadster')], default='SUV', max_length=15)),
                ('year', models.IntegerField(default=2023, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(2015)])),
                ('color', models.CharField(max_length=100)),
                ('cylinders', models.IntegerField(default=4)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
