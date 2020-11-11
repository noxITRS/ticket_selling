from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


from events.models import Event
from tickets.models import TicketReservation
from tickets.serializers import TicketReservationCreateSerializer, TicketReservationRetrieveSerializer


class TicketReservationViewSet(viewsets.ViewSet):
    queryset = TicketReservation.objects.all()
    serializer_class = TicketReservationCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        event_queryset = Event.objects.all()
        event = get_object_or_404(event_queryset, pk=data.get('event_id'))
        ticket_type = get_object_or_404(event.ticket_types, type=data.get('ticket_type'))
        if ticket_type.quantity == 0:
            return Response({"error": "There's not enough tickets on stock, please try again later"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        ticket_type.quantity -= 1
        ticket_type.save()
        order = TicketReservation(event=event, ticket_type=ticket_type.type)
        order.save()
        serializer = TicketReservationCreateSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = TicketReservationRetrieveSerializer(order)
        return Response(serializer.data)
