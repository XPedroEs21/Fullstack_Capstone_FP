from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    year_established = models.IntegerField(default=1950)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('MINIVAN', 'Minivan'),
        ('PICKUP', 'Pickup Truck'),
        ('SPORTS_CAR', 'Sports Car'),
        ('CROSSOVER', 'Crossover'),
        ('ELECTRIC', 'Electric Vehicle'),
        ('HYBRID', 'Hybrid Vehicle'),
        ('ROADSTER', 'Roadster'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ]
    )
    color = models.CharField(max_length=100)
    cylinders = models.IntegerField(default=4)

    def __str__(self):
        return self.name
