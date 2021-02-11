from django.shortcuts import render

# Create your views here.
from .models import Delivery
from .serializers import DeliverySerializer

from rest_framework import generics



# Create your views here.

class DeliveryView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer