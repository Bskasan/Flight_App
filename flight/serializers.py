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

    gender_text = serializers.SerializerMethodField()

    class Meta:
        model = Passenger
        exclude = []
    
    def get_gender_text(self, object):
        return object.get_gender_display()

# --------------------- FLIGHT SERIALIZER --------------------- #

class FlightSerializer(FixedSerializer):

    # Normally we can write directly the arrival or departure, but we wanted to see how the source code works and manipulate.
    departure_city = serializers.SerializerMethodField() # return from get_field_name()
    arrival_city = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "created",
            "created_id",
            "departure_city",
            "arrival_city",
            "created_time",
            "updated_time",
            "flight_number",
            "airline",
            "departure",
            "departure_date",
            "arrival",
            "arrival_date",
            "get_airline_display", # dont need SerializerMethodField.
        )

    def get_departure_city(self, obj):
        return obj.get_departure_display() # To show the departure value.
    
    def get_arrival_city(self, obj):
        return obj.get_arrival_display() # Obj comes automatically.

# ------------------ RESERVATION SERIALIZER ------------------- #

class ReservationSerializer(FixedSerializer):

    # Two Method
    # only __str__() method.
    # fligth = serializers.StringRelatedField()
    # ------------------------------------------


    # complete data
    flight = FlightSerializer() # ForeignKey 
    # ------------------------------------------
    # flight_id = serializers.IntegerField()

    # To see our passenger's details.
    passenger = PassengerSerializer(many=True) # ManyToMany()

    class Meta:
        model = Reservation
        exclude = []