from rest_framework import generics

from modules.middleman.Infastructure.services import Google_API

from modules.middleman.Domain import serializers


class ExternalApiView(generics.CreateAPIView):
    serializer_class = serializers.GoogleSerializer

    def get(self, request):
        return self.google_food(request)

    def google_food(self, request):
        return Google_API.get_google_food()
