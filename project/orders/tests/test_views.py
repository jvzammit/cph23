from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from orders.models import Customer


class CustomerViewSetTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test")
    
    def setUp(self):
        self.client.force_login(user=self.user)

    def test_create_without_any_name_data_provided(self):
        # Given neither first_name nor last_name are provided
        data = {"code": "test-code"}

        # When data is posted
        response = self.client.post("/api/customers/", data=data)
        
        # Then customer is created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        customer = Customer.objects.get(id=response.data["id"])
        self.assertEqual(customer.code, "test-code")

    def test_create_partial_name_provided(self):
        # Given first_name is provided without last_name
        data = {"code": "test-code", "first_name": "John", "last_name": ""}

        # When data is posted
        response = self.client.post("/api/customers/", data=data)
        
        # Then an error is returned
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {'non_field_errors': ['Provide both first name and last name']}
        )

    def test_create_full_name_provided(self):
        # Given both first_name and last_name are provided
        data = {"code": "test-code", "first_name": "John", "last_name": "Doe"}

        # When data is posted
        response = self.client.post("/api/customers/", data=data)

        # Then customer is created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        customer = Customer.objects.get(id=response.data["id"])
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")
