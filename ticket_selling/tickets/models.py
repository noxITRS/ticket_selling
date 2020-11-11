from django.db import models
import uuid

from events.models import Event


class TicketReservation(models.Model):
    RESERVED = 'R'
    PAID = 'P'
    EXPIRED = 'E'
    STATUS = [
        (RESERVED, 'Reserved'),
        (PAID, 'Paid'),
        (EXPIRED, 'Expired')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='orders', blank=True, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=20)
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=RESERVED,
    )
    reserved_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'"{self.status}" | order: {self.id} | event_name: {self.event.name}| ticket_type: {self.ticket_type}'


class TicketAvailability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='ticket_types', blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "Ticket Availabilities"
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'type'], 
                name='unique_type'
            )
        ]

    def __str__(self):
        return f'"{self.type}" ticket for "{self.event.name}" event.'
