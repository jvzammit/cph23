import arrow
import time_machine
from django.test import TestCase
from orders.models import Order
from orders.tests.factories import CustomerFactory, OrderFactory


class CustomerTests(TestCase):
    def test_str_returns_email(self):
        # Given customer with email set
        customer = CustomerFactory(email="test@test.com")

        # When __str__ is called
        # Then customer's email is returned
        self.assertEqual(str(customer), "test@test.com")

    def test_str_returns_name(self):
        # Given customer with email unset, first_name and last_name set
        customer = CustomerFactory(
            email="",
            first_name="John",
            last_name="Doe",
        )

        # When __str__ is called
        # Then customer's name is returned
        self.assertEqual(str(customer), "John Doe")

    def test_str_returns_not_available(self):
        # Given customer with both email and name details unset
        customer = CustomerFactory(email="", first_name="", last_name="")

        # When __str__ is called
        # Then 'n/a' is returned
        self.assertEqual(str(customer), "n/a")


class OrderQuerysetTests(TestCase):
    @time_machine.travel("2023-09-10 14:30")
    def test_created_today(self):
        # Given three orders created on today's date's boundaries
        date1 = arrow.get("2023-09-09 23:59").datetime  # yesterday
        date2 = arrow.get("2023-09-10 00:00").datetime  # today 00:00
        date3 = arrow.get("2023-09-10 00:01").datetime  # today 00:01

        _ = OrderFactory(created_at=date1)
        order2 = OrderFactory(created_at=date2)
        order3 = OrderFactory(created_at=date3)

        # When created_today is called
        queryset = Order.objects.all().created_today()

        # Then the expected orders are returned
        self.assertQuerysetEqual(
            queryset,
            queryset.filter(id__in=[order2.id, order3.id]),
        )
