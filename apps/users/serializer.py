from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from apps.users.models import Profile

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'surname', 'age', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'password',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'last_login',
                  'created_at',
                  'updated_at',
                  'profile'
                  )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        password = validated_data.pop('password', None)
        user = UserModel(**validated_data)
        if password:
            user.set_password(password)

        user.save()
        Profile.objects.create(user=user, **profile)
        return user

