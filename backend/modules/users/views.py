from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a new User in the db """
    serializer_class = UserSerializer
