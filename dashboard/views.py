from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from order.models import Order
import json
from django.http import JsonResponse

# from django.http import HttpResponse

# Create your views here.
@login_required()
def home(request):
    # order = Order.objects.all()
    pro_count = Product.objects.count()
    order_count = Order.objects.count()
    buyers = Order.objects.filter(supplier__isnull=True,status='pending')
    # print(buyers)
    suppliers = Order.objects.filter(buyer__isnull=True,status='pending')
    context={'buyers':buyers, 'suppliers':suppliers ,'card':{'Product':pro_count,
    'Order':order_count,'Buyer Order': buyers.count(),'Suppliers Order':suppliers.count() }}
    return render(request,'dashboard/home.html',context)


def statusupdate(request):
    # staff = StaffRequest.objects.get(id=pk).update(status='Approved') OR
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']
    staff = Order.objects.get(id=productId)

    if action == 'Approve':
        staff.status = 'approved'
    elif action == 'Decline':
        staff.status = 'decline'
    else:
        pass

    staff.save()

    # return JsonResponse('Payment submitted..', safe=False)
    return JsonResponse({ 'productId':productId})


    # return redirect('home')


