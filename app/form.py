from django.forms import ModelForm
from .models import *
from django import forms

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields=['name','dob','gender','mobile','resume','email','company']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.Select(attrs={'class':'form-control'}),
        }