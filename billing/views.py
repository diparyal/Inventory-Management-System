from django.shortcuts import render
from order.models import Order

# Create your views here.
def bill(request):
    context={}
    if request.user.is_seller:
        order = Order.objects.filter(supplier=request.user.id,status='approved')
        context={'orders':order}
    elif request.user.is_buyer:
        order = Order.objects.filter(buyer=request.user.id,status='approved')
        context={'orders':order}
    elif request.user.is_admin:
        order = Order.objects.all(status='approved')
        context={'orders':order}
    else:
        pass

    total = 0
    for i in order:
        total += i.product.price * i.units


    return render(request,'billing/bill.html',{'order':order,'total':total})
