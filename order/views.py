from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer

from rest_framework import generics
from django.contrib.auth.decorators import login_required




# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@login_required()
def AllOrder(request):
    order = Order.objects.all()
    context={'orders':order}
    return render(request,'order/display_order.html',context)
