from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.decorators import login_required, user_passes_test

from .serializers import UserSerializer
from django.views.generic.list import ListView

from rest_framework import generics
# from django.utils.translation import gettext as _

from .decorator import admin_status_required



# Create your views here.
class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat password'})

    #Edit label
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
        # widgets = {
        # 'username': forms.fields.TextInput(attrs={'placeholder': 'Your Name'}),
        # 'email': forms.fields.TextInput(attrs={'placeholder': 'Email Address'}),
        # # 'password1': forms.fields.CharField(attrs={'placeholder': 'Password'}),
        # # 'password2': forms.fields.CharField(attrs={'placeholder': 'Password confirmation'}),
        # }
        
        # fields = ['username','email','password1','password2']


def SignUpView(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_type = request.POST.get("user_types")
        password1= request.POST.get("password1")
        password2  = request.POST.get("password2")
        if password1 == password2:
            if user_type == "Seller":
                User.objects.create_user(username=username,email=email,password=password1,is_seller=True)
            elif user_type == "Buyer":
                User.objects.create_user(username=username,email=email,password=password1,is_buyer=True)
            else:
                User.objects.create_user(username=username,email=email,password=password1,is_admin=True)

        # print(done)
        # form = UserForm(request.POST)

        # print(form)
        # if form.is_valid():
        #     uform = form.save(commit=False)

        #     print(request.POST.get("user_types"))
        #     val = request.POST.get("user_types")

        #     if val == "Seller":
        #         uform.is_seller= True
        #     else:
        #         uform.is_buyer = True

        #     print(uform)
            # form.save()
            return redirect('login')
        # form = UserForm(request.POST)
        # print(request.POST)
        # return HttpResponse("Here's the text of the Web page.")

        # # if form.is_valid(): 
        # #     form.save()
        # #     return redirect('store')
    
    context = {'UserForm' : UserForm()}
    return render(request, 'all_users/register.html', context)  
   # OR

   # class register(generic.CreateView):
   #  form_class = UserCreationForm
   #  success_url = reverse_lazy('login')
   #  template_name = 'registration/signup.html'


# Create your views here.

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@admin_status_required
def UserList(request):

    context = {'Users': User.objects.all()}

    return render(request, 'all_users/user_list.html', context) 



