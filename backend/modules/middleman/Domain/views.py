from rest_framework import generics

from modules.middleman.Infastructure.services import Google_API


class ExternalApiView(generics.CreateAPIView):

    def google_food(self):
        return Google_API.get_google_food()
