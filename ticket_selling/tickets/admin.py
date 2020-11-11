from celery.local import try_import
from django.contrib import admin
from .models import TicketAvailability, TicketReservation

# Register your models here.
admin.site.register(TicketAvailability)
admin.site.register(TicketReservation)