from django.db import models
from django.contrib.auth.models import User


# ----------------------------------------------------- #
# -------------------- FIX MODEL ---------------------- #
# ----------------------------------------------------- #

class FixedModel(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)



# ----------------------------------------------------- #
# -------------------- PASSENGER ---------------------- #
# ----------------------------------------------------- #
class Passenger(FixedModel):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Others'),
        ('P', 'Prefer Not to Say'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDERS, default='P')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# ----------------------------------------------------- #
# -------------------   FLIGHT   ---------------------- #
# ----------------------------------------------------- #
class Flight(FixedModel):

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
    departure = models.PositiveSmallIntegerField(choices=CITIES)
    departure_date = models.DateField()
    arrival = models.PositiveIntegerField(choices=CITIES)
    arrival_date = models.DateField()
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.flight_number} # {self.airline} # {self.departure} => {self.arrival}'


# ----------------------------------------------------- #
# ------------------ RESERVATION ---------------------- #
# ----------------------------------------------------- #

class Reservation(FixedModel):

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger)

    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)