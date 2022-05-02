from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Ngo(models.Model):
    ngo_name = models.CharField(max_length=200, null=True)
    # user = ngo name
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True)
    # owner_name = models.CharField(max_length=200, null=True)
    contact_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
    # location details
    address = models.CharField(max_length=500, null=True)
    # usi api for states
    state = models.CharField(max_length=200, null=True)
    aim = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    # logo
    logo = models.ImageField(null=True, blank=True, default='ngo.jpg')


    def __str__(self):
        return str(self.ngo_name)


class Donor(models.Model):
    name_user = models.CharField(max_length=200, null=True)
    # user is unique
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True)
    contact_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    # location details
    # address = models.CharField(max_length=500, null=True)
    # usi api for states
    # state = models.CharField(max_length=200, null=True)
    # logo
    # profile_pic = models.ImageField(null=True, blank=True, default='donor.png')

    def __str__(self):
        return str(self.user)


# from django.http import HttpResponse
# from django.shortcuts import redirect


# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('home')
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper_func


# def allowed_users(allowed_roles=[]):
#     def decorater(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse("You are an un-authorised user")

#         return wrapper_func
#     return decorater

# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'admin':
#             return view_func(request, *args, **kwargs)
#         if group == "customer":
#             return redirect('user')
#     return wrapper_func
