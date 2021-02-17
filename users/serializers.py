from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ Serializer for the CustomUser object """

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def save(self):
        """ Create a new user with encrypted password and return it """
        new_user = CustomUser(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )
        password = self.validated_data["password"]

        if password == "password":
            raise serializers.ValidationError({"password": "Password must be different from 'password'"})
        new_user.set_password(password)
        new_user.save()
        return new_user
