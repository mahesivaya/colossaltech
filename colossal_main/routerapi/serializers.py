from rest_framework import serializers
from .models import Routerapi

class RouterSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Routerapi
        fields = '__all__'