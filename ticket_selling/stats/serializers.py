from rest_framework import serializers
from rest_framework import fields

class StatsSerializer(serializers.Serializer):
    event_name = serializers.CharField(source='event__name')
    ticket_type = serializers.CharField()
    count = serializers.IntegerField(source='ticket_type__count')

    class Meta:
        fields = ['event_name', 'ticket_type', 'count']