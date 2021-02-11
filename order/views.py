from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer

from rest_framework import generics



# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



def AllOrder(request):
    order = Order.objects.all()
    context={'orders':order}
    return render(request,'order/display_order.html',context)
