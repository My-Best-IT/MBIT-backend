from rest_framework import serializers
from .models import Mbit

class MbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbit
        fields = ['frontend', 'backend', 'game', 'security', 'data']
