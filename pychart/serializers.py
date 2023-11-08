from rest_framework import serializers
from .models import Mbit

class MbitSerializer(serializers.Serializer):
    class Meta:
        model = Mbit
        fields = ['frontend','backend','game','security','data']