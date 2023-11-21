from rest_framework import serializers
from .models import StoreContact

class StoreContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreContact
        fields = '__all__'