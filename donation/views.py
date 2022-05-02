from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import *
from .forms import *
from .decoraters import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def NgoSignUp(request):
    user_type = 'ngo'
    user_form = UserForm()
    ngo_reg_form = NgoRegForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        ngo_reg_form = NgoRegForm(request.POST)
        if user_form.is_valid() and ngo_reg_form.is_valid():
            user = user_form.save()
            user.is_ngo = True
            user.save()
            profile = ngo_reg_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account was created! ')
            return redirect('login')
    context = {'user_form':user_form,'ngo_reg_form':ngo_reg_form,'user_type':user_type}
    return render(request,'donation/ngo_reg.html', context)

def DonorSignUp(request):
    user_type = 'donor'
    user_form = UserForm()
    donor_reg_form = DonorRegForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        donor_reg_form = DonorRegForm(request.POST)
        if user_form.is_valid() and donor_reg_form.is_valid():
            user = user_form.save()
            user.is_donor = True
            user.save()
            profile = donor_reg_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account was created! ')
            return redirect('login')
    context = {'user_form':user_form,'donor_reg_form': donor_reg_form,'user_type':user_type}
    return render(request,'donation/donor_reg.html', context)

def SignUp(request):
    return render(request,'donation/signup.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_ngo:
               login(request, user)
               return HttpResponseRedirect(reverse('ngo'))
            if user.is_donor:
               login(request, user)
               return HttpResponseRedirect(reverse('donor'))
            else:
             messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request,'donation/login.html', context)

@login_required()
def user_logout(request):
    logout(request)
    return redirect('login')

def NgoPage(request):
    return render(request, 'donation/ngo.html')

def DonorPage(request):
    return render(request, 'donation/donor.html')


class DonorView(LoginRequiredMixin,DetailView):
    context_object_name = "donor"
    model = Donors
    template_name = 'donation/donor_index.html'


class NgoView(LoginRequiredMixin,DetailView):
    context_object_name = "ngo"
    model = Ngos
    template_name = 'donation/ngo_index.html'

@login_required()
def upload_requirement(request,id):
    req_uploaded = False
    ngo = Ngos.objects.get(user_id=id)
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            # product = Requirements()
            # product.seller = Ngos.objects.filter(user=ngo).first()
            # product.name=form.cleaned_data['name']
            # product.category=form.cleaned_data['category']
            # product.quantity=form.cleaned_data['quantity']
            upload = form.save(commit=False)
            upload.ngos = ngo
            upload.save()
            # product.save()
            req_uploaded = True
    else:
        form = ReqForm()
    context = {'form':form,'req_uploaded':req_uploaded}
    return render(request,'donation/upload_req.html', context)

@login_required()
def req_list(request,id):
    ngo = Ngos.objects.get(user_id=id)
    reqs = Requirements.objects.filter(ngo=ngo)
    return render(request,'donation/req_list.html',{'ngo':ngo,'reqs':reqs})

@login_required()
def req_list_backup(request,id):
    ngo = Ngos.objects.get(user_id=id)
    reqs = Requirements.objects.filter(ngo=ngo)
    return render(request,'donation/req_list_backup.html',{'ngo':ngo,'reqs':reqs})

@login_required()
def edit(request, id):
    reqs = Requirements.objects.get(id=id)
    form = ReqForm(instance=reqs)
    if request.method == 'POST':
        form = ReqForm(request.POST, instance=reqs)
        if form.is_valid():
            form.save()
            return redirect("ngo")
    context = {'form': form }
    return render(request, 'donation/edit.html', context)

@login_required()
def done(request, id):
    reqs = Requirements.objects.get(id=id)
    reqs.completed = True
    reqs.save()
    return redirect('ngo')

@login_required()
def undone(request, id):
    reqs = Requirements.objects.get(id=id)
    reqs.completed = False
    reqs.save()
    return redirect('ngo')

@login_required()
def delete(request, id):
    Requirements.objects.get(id=id).delete()
    return redirect('ngo')

@login_required()
def req_list_donors(request):
    reqs = Requirements.objects.order_by('-ngo')
    context = {'reqs': reqs}
    return render(request, 'donation/req_list_donor.html', context)

@login_required()
def donate(request,id):
    donate_upload = False
    donors = Donors.objects.get(user_id=id)
    if request.method == 'POST':
        form = DonatedForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.donors = donors
            upload.save()
            donate_upload = True
    else:
        form = DonatedForm()
    context = {'form':form,'donate_upload':donate_upload}
    return render(request, 'donation/donate.html', context)

@login_required()
def donated_list(request,id):
    ngo = Ngos.objects.get(user_id=id)
    donates = Donated.objects.filter(ngo=ngo)
    return render(request, 'donation/donated.html', {'ngo':ngo, 'donates':donates})

@login_required()
def donated_list_donor(request,id):
    donor = Donors.objects.get(user_id=id)
    donates = Donated.objects.filter(donor=donor)
    return render(request, 'donation/donated_list.html', {'donor':donor, 'donates':donates})


# #drf
# from .models import *
# from .serializers import *
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
#
# #ngos
# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = NgoSerializer
#     queryset = Ngos.objects.all()
#     lookup_field = 'user_id'
#     #authentication_classes = [SessionAuthentication, BasicAuthentication]
#     #authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, user_id=None):
#         if user_id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#     def post(self, request,user_id=None):
#         return self.create(request, user_id)
#     def put(self, request, user_id=None):
#         return self.update(request,user_id)
#     def delete(self, request, user_id):
#         return self.destroy(request, user_id)
#
# class NgoAPIView(APIView):
#     def get(self, request):
#         ngos = Ngos.objects.all()
#         serializer = NgoSerializer(ngos, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = NgoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class NgoDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Ngos.objects.get(user_id=id)
#         except Ngos.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, id):
#         ngo = self.get_object(id)
#         serializer = NgoSerializer(ngo)
#         return Response(serializer.data)
#     def put(self, request, id):
#         ngo = self.get_object(id)
#         serializer = NgoSerializer(ngo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id):
#         ngo = self.get_object(id)
#         ngo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# #donors
# class DonorAPIView(APIView):
#     def get(self, request):
#         donors = Donors.objects.all()
#         serializer = DonorSerializer(donors, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = DonorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class DonorDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Donors.objects.get(user_id=id)
#         except Donors.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, id):
#         donor = self.get_object(id)
#         serializer = DonorSerializer(donor)
#         return Response(serializer.data)
#     def put(self, request, id):
#         donor = self.get_object(id)
#         serializer = DonorSerializer(donor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id):
#         donor = self.get_object(id)
#         donor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# #reqs
# class ReqAPIView(APIView):
#     def get(self, request):
#         reqs = Requirements.objects.all()
#         serializer = ReqSerializer(reqs, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ReqSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
