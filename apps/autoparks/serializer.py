from rest_framework import serializers

from apps.autoparks.models import AutoPark
from apps.first.serializer import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = AutoPark
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')