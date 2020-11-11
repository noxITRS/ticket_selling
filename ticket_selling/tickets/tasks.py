from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta
from events.models import Event
from django.db.models.aggregates import Count
from celery import shared_task

from .models import TicketReservation


@shared_task
def update_orders():
    tickets = TicketReservation.objects.filter(reserved_time__lt=datetime.now()-timedelta(minutes=15))
    tickets.update(status=TicketReservation.EXPIRED)

    gropued_tickets = tickets.values('event__id', 'ticket_type').annotate(Count('ticket_type'))
    for q in gropued_tickets:
        ticket = Event.objects.get(pk=q.get('event__id')).ticket_types.get(type=q.get('ticket_type'))
        ticket.quantity += q.get('ticket_type__count')
        ticket.save()