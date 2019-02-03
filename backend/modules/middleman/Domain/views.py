from rest_framework import generics

from modules.middleman.Infastructure.services import Google_API, Yelp_API

from modules.middleman.Domain import serializers


class ExternalApiView(generics.CreateAPIView):
    serializer_class = serializers.GoogleSerializer

    def get(self, request):
        return self.google_food(request)

    def google_food(self, request):
        goog = Google_API()
        return goog.google_API_Caller()

    def yelp_review(self, request):
        yelp = Yelp_API()
        return yelp.get_yelp_business_id()
