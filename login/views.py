
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_auth
from django.views.generic import CreateView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):
    context = {}
    return render(request, 'login/index.html', context)


class NgoSignUpView(CreateView):
    model = User
    form_class = NgoSignUpForm
    template_name = 'login/ngo_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login_auth(self.request, user)
        return redirect('login')


class DonorSignUpView(CreateView):
    model = User
    form_class = DonorSignUpForm
    template_name = 'login/donor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login_auth(self.request, user)
        return redirect('login')


def index(request):
    return render(request, 'login/index.html')


# @unauthenticated_user
def login(request):
    if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            if user.is_ngo:
                login_auth(request, user)
                return redirect('main:admin', user.id)
            else:
                messages.info(request, 'Ngo is not registered')
            if user.is_donor:
                login_auth(request, user)
                return redirect('main:user', user.id)
            else:
                messages.info(request, 'User is not registered')

        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


# def ngo(request):
#     context = {}
#     return render(request, 'login/ngo.html', context)


# def donor(request):
#     context = {}
#     return render(request, 'login/donor.html', context)

def create_user(n):
    user = User()
    user.username = n
    user.is_ngo = True
    user.save()


# import pandas as pd
# df = pd.read_csv("ngo1.csv", sep=',')
# #
# def ngos(df):
#     cnt = 1
#     for i in User.objects.all():
#         ngo = Ngo()
#         ngo.user = i
#         ngo.ngo_name = df['ngo_name'][cnt]
#         # ngo.contact_number = df['contact_number'][cnt]
#         ngo.email = df['email'][cnt]
#         ngo.address = df['address'][cnt]
#         ngo.state = df['state'][cnt]
#         ngo.aim = df['']
#         ngo.save()
#         cnt+=1

def ngos(df):
    for i in range(1, 430):
        username = 'username{}'.format(i)
        x = User.objects.get_or_create(username=username)
        x = x[0]
        x.set_password('Password@123')
        x.is_ngo=True
        x.save()
        print(x.id)
        ngo = Ngo.objects.create(user=x)
        ngo.ngo_name = df['Name'][i]
        # ngo.contact_number = df['contact_number'][cnt]
        ngo.email = df['Email'][i]
        ngo.address = df['Address'][i]
        ngo.state = 'Maharashtra'
        ngo.aim = df['Aim/Objective'][i]
        ngo.save()

# ngos(df)
#
# for i in Ngo.objects.all():
#     print(i.user)

# for ind in df.index:
# print(df['ngo_name'][0])

import random

def assign_randomCIty(city_list):
    Ngos = Ngo.objects.all()
    for ngo in Ngos:
        ngo.city = random.choice(city_list)
        ngo.save()

