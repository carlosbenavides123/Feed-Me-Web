from django.shortcuts import render
from rest_framework import generics

import Infastructure.services as repository
import requests

class ExternalApiView(generics.CreateAPIView):

    def google_food(self, requests):
        return repository.get_google_food(requests)
    
    def yelp_review(self, requests):
        return repository.get_yelp_resview()