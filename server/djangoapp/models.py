from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# CarModel model
class CarModel(models.Model):
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)

    # Type choices
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    TRUCK = 'Truck'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
        (TRUCK, 'Truck'),
    ]

    type = models.CharField(
        max_length=15,
        choices=CAR_TYPES,
        default=SEDAN
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
