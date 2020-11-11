from django.db.models import query
from django.db.models.aggregates import Count
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from tickets.models import TicketReservation
from stats.serializers import StatsSerializer
from django.contrib.auth.models import User

class StatsViewSet(viewsets.ViewSet):
    serializer_class = StatsSerializer
    queryset = User.objects.all()

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def tickets_per_event(self, request, pk=None):
        grouped_tickets = TicketReservation.objects.values('event__name', 'ticket_type').annotate(Count('ticket_type'))
        print(grouped_tickets)

        return Response(StatsSerializer(grouped_tickets, many=True).data)
