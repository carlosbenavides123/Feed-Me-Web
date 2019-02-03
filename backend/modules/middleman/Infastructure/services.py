from rest_framework.response import Response

from django.conf import settings

import requests
# location=-33.8670522,151.1957362&radius=1500&type=restaurant=cruise&key=AIzaSyAEAXEZ8Z-3ReCoSukBYutcDpzCvP9R-Jw
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
        return Response({"lol": GOOGLE_PLACES_URL})

    def get_google_food(self):
        """ From the response, choose a random restaurant """
        return self.google_API_Caller()

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
            "location": "9345 Reseda Blvd, Northridge, CA 91324",
            "latitude": 34.2404185,
            "longitude": -118.5385539
        }

        res = requests.get(url, params=params, headers=headers)
        res = res.json()
        return Response(res)
