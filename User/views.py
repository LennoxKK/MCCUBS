from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Import login_required decorator
from .forms import UserRegForm

# Create your views here.
def register(request):
    if request.method=="post":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username') #Get the user name that is submitted
            messages.success(request,f'Your account has been created! You are now able to login ')#Show the success message
            return redirect('login')
    else:
        form =UserRegForm
    return render(request, 'users/register.html',{'form':form})
    
@login_required # Require user logged in before they can access profile page
def profile(request):
    return render(request, 'users/profile.html')