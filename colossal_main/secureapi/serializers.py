from rest_framework import serializers
from .models import SecdataModel


class DatasecSerialize(serializers.ModelSerializer):
    class Meta:
        model = SecdataModel
        fields = '__all__'