from rest_framework.response import Response

from django.conf import settings

import requests

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian%20grill&"\
                    "inputtype=textquery&fields=photos,"\
                    "formatted_address,name,opening_hours,rating&locationbias="\
                    "circle:2000@47.6918452,-122.2226413&"\
                    "key=" + settings.GOOGLE_API_KEY


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
        return res
