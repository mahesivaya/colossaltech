from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Apiappusers
from .serializers import ApiSerializer


class Appuserlist(generics.ListCreateAPIView):
    queryset = Apiappusers.objects.all()
    serializer_class = ApiSerializer


class Appuserdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apiappusers.objects.all()
    serializer_class = ApiSerializer