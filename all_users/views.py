from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
class UserForm(UserCreationForm):
    #Edit label
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = '__all__'
        
        fields = ['username','email','password1','password2']


def SignUpView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form.save()
        return redirect('login')
        # form = UserForm(request.POST)
        # print(request.POST)
        # return HttpResponse("Here's the text of the Web page.")

        # # if form.is_valid(): 
        # #     form.save()
        # #     return redirect('store')
    else:
        form = UserForm()
        context = {'form' : form}
        return render(request, 'all_users/register.html', context)  


   # OR

   # class register(generic.CreateView):
   #  form_class = UserCreationForm
   #  success_url = reverse_lazy('login')
   #  template_name = 'registration/signup.html'

def home():
    return HttpResponse("Here's the text of the Web page.")
