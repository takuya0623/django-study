from .models import Item
from rest_framework import serializers


class ItmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price']
