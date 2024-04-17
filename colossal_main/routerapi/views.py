from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import RouterSerialize
from .models import Routerapi

class RouterView(viewsets.ModelViewSet):
    queryset = Routerapi.objects.all()
    serializer_class = RouterSerialize