from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from order.models import Order
from product.models import Product
from order.models import Order
# from django.http import HttpResponse

# Create your views here.
@login_required()
def home(request):
    # order = Order.objects.all()
    pro_count = Product.objects.count()
    order_count = Order.objects.count()
    buyers = Order.objects.filter(supplier__isnull=True,)
    # print(buyers)
    suppliers = Order.objects.filter(buyer__isnull=True)
    context={'buyers':buyers, 'suppliers':suppliers ,'pro_count':pro_count,'order_count':order_count}
    return render(request,'dashboard/home.html',context)

