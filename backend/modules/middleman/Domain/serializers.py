from modules.middleman.models import GoogleApiResponse

from rest_framework import serializers


class GoogleSerializer(serializers.ModelSerializer):
    """ Serializer for user object """

    class Meta:
        model = GoogleApiResponse
        fields = '__all__'
        # fields = ('email', 'username', 'is_active', 'password')
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
