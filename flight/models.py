from django.db import models
from django.contrib.auth.models import User


# ----------------------------------------------------- #
# -------------------- PASSENGER ---------------------- #
# ----------------------------------------------------- #
class Passenger(models.Model):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Others'),
        ('P', 'Prefer Not to Say'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDERS, default='P')
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


# ----------------------------------------------------- #
# -------------------   FLIGHT   ---------------------- #
# ----------------------------------------------------- #
class Flight(models.Model):

    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('SUN', 'Sun Airlines'),
        ('PGS', 'Pegasus Airlines'),
    )

    CITIES = (
        (1, 'Adana'),
        (6, 'Ankara'),
        (7, 'Antalya'),
        (9, 'Aydın'),
        (10, 'Balıkesir'),
        (16, 'Bursa'),
        (32, 'Isparta'),
        (34, 'Istanbul'),
        (35, 'Izmir'),
        (44, 'Malatya'),
        (52, 'Ordu'),
    )

    flight_number = models.CharField(max_length=64)
    airline = models.CharField(max_length=3, choices=AIRLINES, default='THY')
