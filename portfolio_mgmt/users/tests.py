from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
# Create your tests here.


class UserLoginTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser', password='testpass', email='test@example.com')
        self.client = APIClient()
        self.url = ('/user/login/')

    def test_login(self):
        payload= {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserRegisterTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ('/user/register/')

    def test_register(self):
        payload= {
            'username': 'prabesh',
            'password': 'uprety412',
            'password2': 'uprety412',
            'email': 'prabeshuprety1@thamescollege.edu.np',
            'first_name':'prabesh',
            'last_name':'uprety',
        }
        response = self.client.post(self.url, data=payload)
        data= response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['username'], payload['username'])