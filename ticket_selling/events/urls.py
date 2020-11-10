from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from events.views import EventViewSet


router = routers.DefaultRouter()

router.register('', EventViewSet)

urlpatterns = [

    ]

urlpatterns += router.urls