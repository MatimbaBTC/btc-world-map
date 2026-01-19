from rest_framework import serializers
from .models import Event, CircularEconomy, Community

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CircularEconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = CircularEconomy
        fields = '__all__'

class CummunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'