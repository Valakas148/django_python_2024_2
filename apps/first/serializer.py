from rest_framework import serializers

from apps.first.models import CarModel


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'price', 'year', 'body_type', 'created_at', 'updated_at')

    # def create(self, validated_data: dict):
    #     car = CarModel.objects.create(**validated_data)
    #     return car
    #
    # def update(self, instance, validated_data: dict):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #         instance.save()
    #         return instance

