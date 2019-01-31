from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user object """

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_active')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
