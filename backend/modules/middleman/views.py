from django.shortcuts import render
from rest_framework import generics

import services, requests

class ExternalApiView(generics.CreateAPIView):

    def google_food(self, requests):
        return service.get_google_food(requests)
    
    def yelp_review(self, requests):
        return services.get_yelp_resview()