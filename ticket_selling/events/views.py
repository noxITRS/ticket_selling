from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        serializer = EventSerializer(self.queryset, many=True)
        return Response(serializer.data) 

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
