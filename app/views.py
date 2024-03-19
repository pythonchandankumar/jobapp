from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout





def  home(request):
    return render(request,'home.html')


def signuppage(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Signup()
    return render(request,'signup.html',{'form':form})


def loginview(request):
    if request.method=="POST":
        fm=Loginform(request.POST)
        if fm.is_valid():
            u=fm.cleaned_data['username']
            p=fm.cleaned_data['password']
            user=authenticate(username=u, password=p)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        fm=Loginform()
    return render(request,'login.html',{'form':fm})


def logoutview(request):
    logout(request)
    return redirect("home")



        
        
