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

    # Normally we can write directly the arrival or departure, but we wanted to see how the source code works and manipulate.
    departure_city = serializers.SerializerMethodField() # return from get_field_name()
    arrival_city = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        exclude = []

    def get_departure_city(self, obj):
        return obj.get_departure_display() # To show the departure value.
    
    def get_arrival_city(self, obj):
        return obj.get_arrival_display() # Obj comes automatically.

# ------------------ RESERVATION SERIALIZER ------------------- #

class ReservationSerializer(FixedSerializer):

    class Meta:
        model = Reservation
        exclude = []