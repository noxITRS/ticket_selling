from rest_framework import serializers

from events.serializers import EventSerializer
from tickets.models import TicketAvailability, TicketReservation


class TicketAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAvailability
        fields = ['type', 'quantity']


class TicketReservationCreateSerializer(serializers.ModelSerializer):
    event_id = serializers.UUIDField()
    ticket_type = serializers.CharField()

    class Meta:
        model = TicketReservation
        fields = ['id', 'event_id', 'ticket_type']


class TicketReservationRetrieveSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = TicketReservation
        fields = ['id', 'event', 'ticket_type', 'status', 'reserved_time', 'last_modified']
