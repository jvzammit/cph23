from rest_framework import serializers
from rest_framework.test import APITestCase

from orders.serializers import CustomerSerializer


class CustomerSerializerTests(APITestCase):
    def test_validate_without_any_name_data_provided(self):
        # Given neither first_name nor last_name are provided
        data = {}

        # When validate is called
        # Then no validation error is raised
        self.assertEqual(CustomerSerializer().validate(data), data)

    def test_validate_partial_name_provided(self):
        # Given first_name is provided without last_name
        data = {"first_name": "John", "last_name": ""}

        # When validate is called
        # Then validation error is raised
        with self.assertRaisesMessage(
            serializers.ValidationError,
            "Provide both first name and last name",
        ):
            CustomerSerializer().validate(data)

    def test_validate_full_name_provided(self):
        # Given both first_name and last_name are provided
        data = {"first_name": "John", "last_name": "Doe"}

        # When validate is called
        # Then no validation error is raised
        self.assertEqual(CustomerSerializer().validate(data), data)
