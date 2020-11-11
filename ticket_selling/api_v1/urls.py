from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from events.views import EventViewSet
from tickets.views import TicketReservationViewSet
from stats.views import StatsViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Ticket Selling API",
      default_version='v1',
      description="Small application provides API for ticket selling.",
      contact=openapi.Contact(email="strzybny.robert@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)


router = routers.DefaultRouter()

router.register('events', EventViewSet)
router.register('tickets', TicketReservationViewSet)
router.register('stats', StatsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
    ]