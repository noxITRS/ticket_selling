from rest_framework import serializers

from tickets.models import TicketAvailability

class TicketAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAvailability
        fields = ['type', 'quantity']