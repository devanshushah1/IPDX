from django import forms
from .models import *
from django.forms import ModelForm


class RequirementsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter Product'})
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Choose Category'})
        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter Quantity'})

    class Meta:
        model = Requirements
        fields = ['name', 'category', 'quantity']


class Count(ModelForm):
    class Meta:
        model = Requirements
        fields = ['quantity']


class DonationForm(ModelForm):
    class Meta:
        model = Donate
        fields = ['count']
