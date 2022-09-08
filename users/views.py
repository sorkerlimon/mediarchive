from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserCreationForm

from .models import Profile


# Create your views here.
@login_required(login_url='login')
def profile(request):
    # profile = Profile.objects.all()
    current_user = request.user
    # print (current_user.username)
    profile = Profile.objects.get(user = current_user)
    return render(request, 'users/profiles.html',{"profile": profile})



def loginUser(request):
    
    page = 'login'
    

    
    if request.user.is_authenticated: # url bolck Jokhon user login obosthay thakbe tokhn jno url e login lekhle login e na jay
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User not found')
        
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            # print('Username or password not found')
            messages.error(request,'User name or password not found')
        print(request.POST)
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'User Logout')
    return redirect('login')

def registerUser(request):
    
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,'User Registration Successfully Registered')
            
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request,'An error occurred while registering user')
    
    context = {'page':page, 'form':form}

    return render(request, 'users/login_register.html',context)
 