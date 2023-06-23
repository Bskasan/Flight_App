from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)

# -------------------- FIXED SERIALIZER ------------------- #

class PassengerSerializer(serializers.ModelSerializer):
    pass

# -------------------- PASSENGER SERIALIZER ------------------- #

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        exclude = []

# --------------------- FLIGHT SERIALIZER --------------------- #

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        exclude = []

# ------------------ RESERVATION SERIALIZER ------------------- #

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        exclude = []