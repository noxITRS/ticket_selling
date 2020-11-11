from django.urls import path, include
from rest_framework import routers

from events.views import EventViewSet
from tickets.views import TicketReservationViewSet

router = routers.DefaultRouter()

router.register('events', EventViewSet)
router.register('tickets', TicketReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]