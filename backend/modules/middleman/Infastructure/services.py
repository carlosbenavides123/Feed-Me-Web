from rest_framework.response import Response

from django.conf import settings

import requests

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian%20grill&"\
                    "inputtype=textquery&fields=photos,"\
                    "formatted_address,name,opening_hours,rating&locationbias="\
                    "circle:2000@47.6918452,-122.2226413&"\
                    "key=" + settings.GOOGLE_API_KEY

YELP_REVIEWS_URL = "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews"


class Google_API():
    def __init__(self):
        # self.data = self.google_API_Caller()
        self.get_google_food()
        pass

    def get_google_food(self):
        return self.google_API_Caller()

    def google_API_Caller(self):
        """ Call the API """
        url = GOOGLE_PLACES_URL
        res = requests.get(url)
        res = res.json()
        return Response(res)


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
            "location": "9345 Reseda Blvd, Northridge, CA 91324",
            "latitude": 34.2404185,
            "longitude": -118.5385539
        }

        res = requests.get(url, params=params, headers=headers)
        res = res.json()
        return Response(res)
