from django.shortcuts import render,redirect
from .models import Order
from .serializers import OrderSerializer

from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django import forms

# from all_users.models import User
# from all_users import User


# Create your views here.
class OrderForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Order 
        # fields = "__all__"
        fields = ['product','units']
        

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@login_required()
def AllOrder(request):
    context={}
    if request.user.is_seller:
        order = Order.objects.filter(supplier=request.user.id)
        context={'orders':order}
    elif request.user.is_buyer:
        order = Order.objects.filter(buyer=request.user.id)
        context={'orders':order}
    elif request.user.is_admin:
        order = Order.objects.all()
        context={'orders':order}
    else:
        pass
    return render(request,'order/display_order.html',context)

@login_required()
def AddOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False)
            if request.user.is_seller:
                comment.supplier= request.user
            # print(request.POST)
            elif request.user.is_buyer:
                comment.buyer = request.user
            else:
                pass

         
            form.save()
        return redirect('all_order') 

    context= { 'form': OrderForm() }
    return render(request,'order/add_order.html',context)


