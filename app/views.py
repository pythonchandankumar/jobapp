from django.shortcuts import render,get_object_or_404
from .form import *
from django.contrib.auth import authenticate,login,logout
from.models import *
from django.http  import HttpResponseRedirect
from django.contrib.auth.decorators import login_required





def  home(request):
    job=Job.objects.all()[0:3]
    return render(request,'home.html',{'job':job})


def signuppage(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user=form.save()
            account_type=request.POST.get('account_type','jobseeker')
            if account_type == 'employer' :
                userprofile=UserProfile.objects.create(user=user,is_employer=True)
                userprofile.save()
                return HttpResponseRedirect("/login/")
            else:
                userprofile=UserProfile.objects.create(user=user,is_employer=False)
                userprofile.save()
                return HttpResponseRedirect("/login/")
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
                return HttpResponseRedirect('/')
    else:
        fm=Loginform()
    return render(request,'login.html',{'form':fm})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')


def jobdetails(request,id):
    job=Job.objects.get(pk=id)
    return render(request,'jobdetails.html',{ "job":job })
        

def userdashboard(request):
    return render(request,'userprofile.html',{"userprofile":request.user.userprofile})


def add_job(request):
    if request.method=='POST':
        form=AddJobform(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.created_by=request.user
            job.save()
            return HttpResponseRedirect("/")
    else:
        form=AddJobform()
    return render(request,'addjob.html',{'form':form})



def applyjob(request,id):
    job=Job.objects.get(pk=id)
    if request.method=="POST":
        form=ApplicationJobform(request.POST)
        if form.is_valid():
            application=form.save(commit=False)
            application.job=job
            application.created_by=request.user
            application.save()
            return HttpResponseRedirect('/')    
    else:
        form=ApplicationJobform()
    return render(request,'applyjob.html',{'form':form,'job':job})


def view_applicantion(request,applicantion_id):
    application=get_object_or_404(Application,pk=applicantion_id,created_by=request.user)
    return render(request,'view_application.html',{ 'application':application}) 
