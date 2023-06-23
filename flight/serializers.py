from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)

# -------------------- FIXED SERIALIZER ------------------- #

class FixedSerializer(serializers.ModelSerializer):
    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        # User that signed in to the system.
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)

# -------------------- PASSENGER SERIALIZER ------------------- #

class PassengerSerializer(FixedSerializer):

    class Meta:
        model = Passenger
        exclude = []

# --------------------- FLIGHT SERIALIZER --------------------- #

class FlightSerializer(FixedSerializer):

    class Meta:
        model = Flight
        exclude = []

# ------------------ RESERVATION SERIALIZER ------------------- #

class ReservationSerializer(FixedSerializer):

    class Meta:
        model = Reservation
        exclude = []