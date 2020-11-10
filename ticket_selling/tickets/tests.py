from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from datetime import datetime

from events.models import Event
from tickets.models import TicketAvailability
from tickets.serializers import TicketAvailabilitySerializer


class GetTicketAvailabilityInfo(APITestCase):
    client = APIClient()

    def setUp(self):
        self.event = Event.objects.create(
            id='e8f4e683-e873-4a20-a5b1-ec3fae004f92', 
            name="Robert 25th birthday party!", 
            start_datetime=datetime(2021, 1, 29, 18, 0)
            )

        self.first_ticket_type = TicketAvailability(
            id='e2273ee4-d3f0-4d76-804e-2ce9732be0c5',
            type='''Robert's mom''',
            quantity=0
        )

        self.second_ticket_type = TicketAvailability(
            id='e82501a1-f0ff-43e2-88cb-6c09f85086f8',
            type='''Robert's colleagues''',
            quantity=15
        )

        self.first_ticket_type.event = self.event
        self.second_ticket_type.event = self.event

    def test_get_info_about_tickets_availability(self):
        response = self.client.get(f'/events/{self.event.pk}/tickets/')
        queryset = TicketAvailability.objects.all()
        serializer = TicketAvailabilitySerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    