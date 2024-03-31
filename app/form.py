from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth .forms import AuthenticationForm,UsernameField
from django.utils.translation import  gettext_lazy as _
from .models import *

class Signup(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm_password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'})}
        

class Loginform(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
        password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current password', 'class':'form-control'}))


class AddJobform(forms.ModelForm):
     class Meta:
          model=Job
          fields=['title','company','description']
          widgets={
               'title':forms.TextInput(attrs={'placeholder':'Title of the job...','class':'form-control'}),
               'company':forms.TextInput(attrs={'placeholder':'Company name...',"class":"form-control"}),
               'description':forms.Textarea(attrs={'rows':'5','cols':'40','placeholder':'Description of the Job...',"class":"form-control"})
          }
    

class ApplicationJobform(forms.ModelForm):
     class Meta:
          model=Application
          fields=['content','experience']
          widgets={
               'content':forms.Textarea(attrs={'rows':'5','cols':'40','placeholder':'Your application content here...','class':'form-control'}),
               'experience':forms.Select(choices=[('0-1 year','0-1 years'), ('1-3 years','1-3 years'),('3+ years','3+ years')]),
          }