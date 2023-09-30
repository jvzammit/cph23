from datetime import datetime, time

from django.db import models
from django.utils import timezone


class Address(models.Model):
    country_code = models.CharField(max_length=2)


class Customer(models.Model):
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    shipping_address = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.email:
            return self.email
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return "n/a"


class OrderQueryset(models.QuerySet):
    def created_today(self):
        today_floor = datetime.combine(
            timezone.now(), time.min, tzinfo=timezone.get_current_timezone()
        )
        return self.filter(created_at__gte=today_floor)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = OrderQueryset.as_manager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)
