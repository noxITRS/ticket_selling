from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from datetime import datetime

from events.models import Event
from events.serializers import EventSerializer


class GetEventInfo(APITestCase):
    client = APIClient()

    def setUp(self):
        self.true_first_event = Event.objects.create(
            id='e8f4e683-e873-4a20-a5b1-ec3fae004f92', 
            name="Robert 25th birthday party!", 
            start_datetime=datetime(2021, 1, 29, 18, 0)
            )

        self.true_second_event = Event.objects.create(
            id='e2273ee4-d3f0-4d76-804e-2ce9732be0c5', 
            name="Robert 26th hangover!", 
            start_datetime=datetime(2022, 1, 30, 7, 0)
            )

    def test_get_info_about_events(self):
        response = self.client.get('/events/')
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_info_about_specific_event(self):
        response = self.client.get(f'/events/{self.true_first_event.pk}/')
        queryset = Event.objects.get(pk=self.true_first_event.pk)
        serializer = EventSerializer(queryset)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_info_about_not_existing_event(self):
        random_uuid = 'e82501a1-f0ff-43e2-88cb-6c09f85086f8'
        response = self.client.get(f'/events/{random_uuid}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
