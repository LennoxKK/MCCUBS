import csv
from django.contrib.auth import  login

from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from .models import CustomUser
from .extraforms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Import login_required decorator
from .forms import UserRegForm,UserUpdateForm,CUserUpdateForm, ProfileUpdateForm
from .models import User


from django.shortcuts import HttpResponse

# Create your views here.
def register(request):
    if request.method=="POST":
       # print(request)
        form=UserRegForm(request.POST)
       # print(form)
        if form.is_valid():
            print(request)
            form.save()
            username= form.cleaned_data.get('first_name') #Get the user name that is submitted
            messages.success(request,f'Your account has been created!{{username}}, You are now able to login ')#Show the success message
           # url = reverse('Users:profile', kwargs={'username': str(username)})
            url=reverse('home')
            return redirect(url)
    else:
        form =UserRegForm
    return render(request, 'users/register.html',{'form':form})
    
# Require user logged in before they can access profile page
# Update it here
@login_required
def profile(request,username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Users:profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def user_profile(request,username):
    if request.method == 'POST':
        u_form = CUserUpdateForm(request.POST, instance=request.first_name)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.first_name.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Users:profile') # Redirect back to profile page

    else:
        #u_form = CUserUpdateForm(instance=(username))
        #print(request.POST,username,u_form)
        p_form = ProfileUpdateForm()
        print(p_form)
    context = {
        'u_form':CUserUpdateForm,
      #  'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def _export_(request):
    model=User
    print(request.POST)
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['first_name',
            'sir_middle_name',
            'reg_no',
            'level',
            'phone_number',
            'place_of_residence',
            'gender'])
    for user in model.objects.all():
        user = [user.first_name,user.sir_middle_name,user.reg_no,user.level,user.phone_number,user.place_of_residence,user.gender]
        writer.writerow(user)

    response['Content-Disposition']='attachment;filename="members.csv"'
    return response




def create_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            url = reverse('Users:view', kwargs={'first_name': str(user.first_name)})
            return redirect(url)
    else:
        form = CustomUserForm()
    return render(request, 'users/create_profile.html', {'form': form})


def view_profile(request, first_name):
    user = get_object_or_404(CustomUser, first_name=first_name)
    context = {'user': user}
    return render(request, 'users/profile.html', context)

