from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from  django.contrib.auth.models import User

from .models import Profiles
from .forms import SignupForm





# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        
        user = authenticate(username=username, password=password)
        login(request,user)


        return redirect('/accounts/profile')
        
    else:
        form = SignupForm()
    
    return render(request, 'registration/signup_form.html', {'form':form})
        



def profile(request):
    pass
    # profile = Profiles.objects.get(user=request.user)
    # return render(request, 'registration/profile.html',{'profile':profile})

   



def edit_profail(request):
    pass

