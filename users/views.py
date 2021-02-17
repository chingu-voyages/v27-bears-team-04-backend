from rest_framework import generics

from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer


class UserList(generics.ListCreateAPIView):
    """ Create a new user in the system """
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
