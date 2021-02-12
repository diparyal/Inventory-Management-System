from django.shortcuts import render,redirect
from django import forms 
from .models import Product
from .serializers import ProductSerializer

from rest_framework import generics
from django.contrib.auth.decorators import login_required


# create a ModelForm 
class ProductForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Product 
        fields = "__all__"

# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@login_required()
def ProductAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    ProForm = ProductForm()
    context = { 'ProductForm': ProForm}
    return render(request,'product/addproduct.html',context)



