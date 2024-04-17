from rest_framework import serializers
from .models import Apiappusers


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiappusers
        fields = '__all__'