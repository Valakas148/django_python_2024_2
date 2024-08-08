from rest_framework import serializers

from apps.first.models import CarModel


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'price', 'year', 'body_type','photo', 'created_at', 'updated_at')


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}


