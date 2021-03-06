from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user object """

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """ Create a new user with encrypted password and return it """
        return get_user_model().objects.create_user(**validated_data)
