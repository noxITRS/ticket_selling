from django.db import models
import uuid


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique_for_date='start_datetime')
    start_datetime = models.DateTimeField()

    def __str__(self):
        return f'"{self.name}" starting at {self.start_datetime}'
