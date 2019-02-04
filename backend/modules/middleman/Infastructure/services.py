from rest_framework.response import Response

from django.conf import settings

import requests

from random import randint

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"\
                    "location=34.0207289,-118.6926019"\
                    "&radius=1500&type=restaurant"\
                    "&keyword=chicken&"\
                    "key=" + settings.GOOGLE_API_KEY


YELP_PLACES_URL = "https://api.yelp.com/v3/businesses/search"
YELP_REVIEWS_URL = "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews"


class Google_API():
    def __init__(self):
        # self.data = self.google_API_Caller()
        self.get_google_food()
        pass

    def google_API_Caller(self):
        """ Call the API """
        url = GOOGLE_PLACES_URL
        res = requests.get(url)
        res = res.json()
        return res

    def get_google_food(self):
        """ From the response, choose a random restaurant """
        res = self.google_API_Caller()

        if not res['results']:
            self.return_error_message()

        randomResult = self.retrieve_random(res)

        while res['results'][randomResult]['opening_hours']['open_now'] is False:
            if not res['results']:
                self.return_error_message
            del res['results'][randomResult]
            randomResult = self.retrieve_random(res)
        return Response({"LOL":res['results'][randomResult]})

    def retrieve_random(self, res):
        randIdx = randint(0, len(res['results']) - 1)
        return randIdx

    def retrieve_yelp_id(self, res):
        """ From the randomly chosen restaurant
            Find the corressponding yelp business ID"""
        headers = {'Authorization': 'bearer %s' % settings.YELP_API_KEY}
        params = {
            "location": res['vicinity'],
            "latitude": res['geometry']['location']['lng'],
            "longitude": res['geometry']['location']['lng']
        }
        res = requests.get(YELP_PLACES_URL, params=params, headers=headers)
        target = res["name"]

        # for json in res['businesses']:
        #     if target == json['']
        return 

    def return_error_message(self):
        return Response({"error": "There might have been an issue with your"
                         "food choice."})

    def yelp_api_checker(self, res):
        """ From the randomly chose restaurants,
            check if their exists an associated yelp business id,
            which will be used for yelp api calls """
        


class Yelp_API():
    def __init__(self):
        pass

    def get_yelp_reviews(self):
        headers = {'Authorization': 'bearer %s' % settings.YELP_API_KEY}
        params = {
            "id": "WavvLdfdP6g8aZTtbBQHTw",
         }

        url = YELP_REVIEWS_URL
        res = requests.get(url, params=params, headers=headers)
        res = res.json()
        return Response(res)

    def get_yelp_business_id(self):
        headers = {'Authorization': 'bearer %s' % settings.YELP_API_KEY}
        url = "https://api.yelp.com/v3/businesses/search"
        params = {
            "location": "3939 Cross Creek Rd, Malibu",
            "latitude": 34.0207289,
            "longitude": 34.0207289
        }

        res = requests.get(url, params=params, headers=headers)
        res = res.json()
        return Response(res)
