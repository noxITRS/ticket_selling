from django.db import models
import uuid

from events.models import Event


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
