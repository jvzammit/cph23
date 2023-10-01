from rest_framework import serializers

from orders.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "code", "first_name", "last_name", "email", "shipping_address"]
        model = Customer

    def validate(self, attrs):
        first_name = attrs.get("first_name")
        last_name = attrs.get("last_name")
        if first_name or last_name:
            if not all([first_name, last_name]):
                raise serializers.ValidationError(
                    "Provide both first name and last name"
                )
        return attrs
