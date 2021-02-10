from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse



# Create your views here.
class UserForm(UserCreationForm):
    #Edit label
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
        
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
            else:
                User.objects.create_user(username=username,email=email,password=password1,is_buyer=True)

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

def home(request):
    return HttpResponse("Here's the text of the Web page.")
