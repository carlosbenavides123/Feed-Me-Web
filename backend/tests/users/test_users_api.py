from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('users:create')


def create_user(**param):
    return get_user_model().objects.create_user(**param)


class PublicUserApiTest(TestCase):
    """ Test the public apis (non authenticated) """

    def setUp(self):
        self.client = APIClient()

    """ Creating a user, updating a user, testing validation test """

    def test_create_valid_user_return_successful(self):
        """ Given a payload with valid data, create a user """
        payload = {
            "email": "awesomeUser@gmail.com",
            "password": "secret",
            "username": "awesomeguy1"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
