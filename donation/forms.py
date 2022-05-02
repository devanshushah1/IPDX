from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import transaction

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class': 'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }


class NgoRegForm(forms.ModelForm):
    class Meta():
        model = Ngos
        fields = ['name','phone']
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                }


class DonorRegForm(forms.ModelForm):
    class Meta():
        model = Donors
        fields = ['name','phone']
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                }

class ReqForm(forms.ModelForm):
    class Meta():
        model = Requirements
        fields = ['ngo','name','category','quantity']
# 'donated_quantity'

class DonatedForm(forms.ModelForm):
    class Meta():
        model = Donated
        fields = ['requirements','ngo','donor','count']