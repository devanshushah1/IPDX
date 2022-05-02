from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *


class NgoSignUpForm(UserCreationForm):

    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                        # 'class': 'bg-white',
                                                                        # 'class': 'border-left-0',
                                                                        # 'class': 'border-md',
                                                                        # 'class': 'pl-3',
                                                                        'placeholder': 'Contact Number'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            # 'class': 'bg-white',
                                                            # 'class': 'border-left-0',
                                                            # 'class': 'border-md',
                                                            'placeholder': 'E-mail     '}))

    ngo_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             #   'class': 'bg-white',
                                                             #   'class': 'border-left-0',
                                                             #   'class': 'border-md',
                                                                      'placeholder': 'Name of NGO'}))

    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          #   'class': 'bg-white',
                                                          #   'class': 'border-left-0',
                                                          #   'class': 'border-md',
                                                          #   'class': 'pl-3',
                                                          'placeholder': 'State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             #   'class': 'bg-white',
                                                             #   'class': 'border-left-0',
                                                             #   'class': 'border-md',
                                                                      'placeholder': 'City'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            # 'class': 'bg-white',
                                                            # 'class': 'border-left-0',
                                                            # 'class': 'border-md',
                                                            # 'class': 'pl-3',
                                                            'placeholder': 'Address'}))
    # logo
    logo = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     #  'class': 'bg-white',
                                                     #  'class': 'border-left-0',
                                                     #  'class': 'border-md',
                                                     'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      #   'class': 'bg-white',
                                                      #   'class': 'border-left-0',
                                                      #   'class': 'border-md',
                                                      'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      #   'class': 'bg-white',
                                                      #   'class': 'border-left-0',
                                                      #   'class': 'border-md',
                                                      'placeholder': 'Re-enter Password'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    @ transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo = True
        user.save()
        ngo = Ngo.objects.create(user=user)
        ngo.email = self.cleaned_data.get('email')
        ngo.contact_number = self.cleaned_data.get('contact_number')
        ngo.ngo_name = self.cleaned_data.get('ngo_name')
        ngo.address = self.cleaned_data.get('address')
        ngo.state = self.cleaned_data.get('state')
        if self.cleaned_data.get('logo') is not None:
            ngo.logo = self.cleaned_data.get('logo')
        else:
            ngo.logo = 'ngo.png'
        ngo.save()
        return user


class DonorSignUpForm(UserCreationForm):
    name_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              #   'class': 'bg-white',
                                                              #   'class': 'border-left-0',
                                                              #   'class': 'border-md',
                                                              #   #   'class': 'pl-3',
                                                              'placeholder': 'Name     '}))
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                        # 'class': 'bg-white',
                                                                        # 'class': 'border-left-0',
                                                                        # 'class': 'border-md',
                                                                        # 'class': 'pl-3',
                                                                        'placeholder': 'Contact Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            # 'class': 'bg-white',
                                                            # 'class': 'border-left-0',
                                                            # 'class': 'border-md',
                                                            'placeholder': 'E-mail     '}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              #   'class': 'bg-white',
                                                              #   'class': 'border-left-0',
                                                              #   'class': 'border-md',
                                                              #   #   'class': 'pl-3',
                                                              'placeholder': 'City'}))
    # state = forms.CharField()
    # address = forms.CharField()
    # logo
    # logo = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     #  'class': 'bg-white',
                                                     #  'class': 'border-left-0',
                                                     #  'class': 'border-md',
                                                     'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      #   'class': 'bg-white',
                                                      #   'class': 'border-left-0',
                                                      #   'class': 'border-md',
                                                      'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      #   'class': 'bg-white',
                                                      #   'class': 'border-left-0',
                                                      #   'class': 'border-md',
                                                      'placeholder': 'Re-enter Password'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    @ transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_donor = True
        user.id_verified = True
        user.save()
        donor = Donor.objects.create(user=user)
        donor.name_user = self.cleaned_data.get('name_user')
        donor.contact_number = self.cleaned_data.get('contact_number')
        donor.email = self.cleaned_data.get('email')
        donor.city = self.cleaned_data.get('city')
        # donor.address = self.cleaned_data.get('address')
        # donor.state = self.cleaned_data.get('state')
        # if self.cleaned_data.get('logo') is not None:
        #     donor.logo = self.cleaned_data.get('logo')
        # else:
        #     donor.logo = 'donor.png'
        donor.save()
        return user
