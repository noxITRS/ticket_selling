from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from datetime import datetime, timedelta

from events.models import Event
from tickets.models import TicketAvailability, TicketReservation
from tickets.serializers import TicketAvailabilitySerializer, TicketReservationRetrieveSerializer
from ticket_selling.urls import API_BASE_URL

class GetTicketAvailabilityInfoTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.event = Event.objects.create(
            id='e8f4e683-e873-4a20-a5b1-ec3fae004f92', 
            name="Robert 25th birthday party!", 
            start_datetime=datetime(2021, 1, 29, 18, 0)
            )

        self.first_ticket_type = TicketAvailability(
            id='e2273ee4-d3f0-4d76-804e-2ce9732be0c5',
            event=self.event,
            type='''Robert's mom''',
            quantity=0
        )

        self.second_ticket_type = TicketAvailability(
            id='e82501a1-f0ff-43e2-88cb-6c09f85086f8',
            event=self.event,
            type='''Robert's colleagues''',
            quantity=15
        )

    def test_get_info_about_tickets_availability(self):
        response = self.client.get(f'/{API_BASE_URL}events/{self.event.pk}/tickets/')
        queryset = TicketAvailability.objects.all()
        serializer = TicketAvailabilitySerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReserveTicketTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.event = Event.objects.create(
            id='e8f4e683-e873-4a20-a5b1-ec3fae004f92', 
            name="Robert 25th birthday party!", 
            start_datetime=datetime(2021, 1, 29, 18, 0)
            )

        self.ticket_type = TicketAvailability.objects.create(
            id='e82501a1-f0ff-43e2-88cb-6c09f85086f8',
            event=self.event,
            type='''Robert's colleagues''',
            quantity=15
        )

        self.sold_ticket_type = TicketAvailability.objects.create(
            id='e2273ee4-d3f0-4d76-804e-2ce9732be0c5',
            event=self.event,
            type='''Robert's mom''',
            quantity=0
        )

        self.reserved_ticket = TicketReservation.objects.create(
            event=self.event,
            ticket_type=self.sold_ticket_type.type,
            )

    def test_making_reservation(self):
        from django.contrib.auth.models import User
        user = User.objects.create_superuser('john', 'lennon@thebeatles.com', 'johnpassword')

        base_quantity = self.ticket_type.quantity
        self.client.force_login(user=user)
        data = {
            "event_id": self.event.pk,
            "ticket_type": self.ticket_type.type
        }
        response = self.client.post(f'/{API_BASE_URL}tickets/', data=data)

        self.ticket_type.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.ticket_type.quantity, base_quantity - 1)

    def test_sold_ticket_reservation(self):
        from django.contrib.auth.models import User
        user = User.objects.create_superuser('john', 'lennon@thebeatles.com', 'johnpassword')

        self.client.force_login(user=user)
        data = {
            "event_id": self.event.pk,
            "ticket_type": self.sold_ticket_type.type
        }

        response = self.client.post(f'/{API_BASE_URL}tickets/', data=data)

        self.ticket_type.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(self.sold_ticket_type.quantity, 0)

    def test_get_info_about_reservation(self):
        response = self.client.get(f'/{API_BASE_URL}tickets/{self.reserved_ticket.id}/')
        serializer = TicketReservationRetrieveSerializer(self.reserved_ticket)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
