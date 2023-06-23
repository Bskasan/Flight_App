from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Passenger, PassengerSerializer,
    Flight, FlightSerializer,
    Reservation, ReservationSerializer
)

# -------------------- FIXED VIEW ------------------- #

class FixView(ModelViewSet):
    pass

# -------------------- PASSENGER VIEW ------------------- #

class PassengerView(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

# -------------------- FLIGTH VIEW ------------------- #

class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# -------------------- Reservation VIEW ------------------- #

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
