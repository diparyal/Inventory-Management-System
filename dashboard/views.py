from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from order.models import Order
# from django.http import HttpResponse

# Create your views here.
@login_required()
def home(request):
    # order = Order.objects.all()
    order = Order.objects.filter(supplier__isnull=True)
    context={'orders':order}
    return render(request,'dashboard/home.html',context)

