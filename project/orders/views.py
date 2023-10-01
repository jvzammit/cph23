from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets

from orders.models import Customer
from orders.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerSerializer
