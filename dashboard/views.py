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
    app_order = Order.objects.filter(status='approved')

    context={'buyers':buyers, 'suppliers':suppliers ,'card':{'Product':pro_count,
    'Order':order_count,'Buyer Order': buyers.count(),'Suppliers Order':suppliers.count() }
    ,'app_order': app_order}
    return render(request,'dashboard/home.html',context)


def statusupdate(request):
    # staff = StaffRequest.objects.get(id=pk).update(status='Approved') OR
    data = json.loads(request.body)
    # print(data)
    productId = data['productId']
    action = data['action']
    approve_order = Order.objects.get(id=productId)

    if action == 'Approve':
        approve_order.status = 'approved'
    elif action == 'Decline':
        approve_order.status = 'decline'
    else:
        pass

    username=''

    if approve_order.supplier != None  :
        username= approve_order.supplier.username
    else:
        username= approve_order.buyer.username

    app_detail={
        'id':approve_order.id,
        'username': username,
        'product':approve_order.product.name,
        'units': approve_order.units,
    }


    # if approve_order.is_seller:
    #     username= 

    # approve_order={'id':staff.id,'username':staff.username}

    approve_order.save()

    # return JsonResponse('Payment submitted..', safe=False)
    return JsonResponse({ 'productId':productId,'app_detail':app_detail })


    # return redirect('home')


