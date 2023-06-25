from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Passenger, PassengerSerializer,
    Flight, FlightSerializer,
    Reservation, ReservationSerializer
)

# -------------------- FIXED VIEW ------------------- #

class FixedView(ModelViewSet):
    pass

# -------------------- PASSENGER VIEW ------------------- #

class PassengerView(FixedView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

# -------------------- FLIGTH VIEW ------------------- #
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FlightView(FixedView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

# -------------------- Reservation VIEW ------------------- #

class ReservationView(FixedView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
