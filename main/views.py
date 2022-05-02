from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from drf.views import donor
from .models import Requirements, Donate
from main.models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
# Create your views here.

ngo_required = user_passes_test(lambda user: user.is_ngo, login_url='login')
donor_required = user_passes_test(
    lambda user: user.is_donor, login_url='login')


def ngo_user_required(view_func):
    decorated_view_func = login_required(ngo_required(view_func))
    return decorated_view_func


def donor_user_required(view_func):
    decorated_view_func = login_required(donor_required(view_func))
    return decorated_view_func


def admin(request, pk):
    id = pk

    context = {'id': id}
    return render(request, 'main/admin.html', context)

#  college = College.objects.get(id=pk)
#     form = UpdateStream(instance=college)
#     if request.method == "POST":
#         form = UpdateStream(request.POST, instance=college)
#         if form.is_valid:
#             form.save()
#             return redirect('homePage')

#     context = {'form': form, 'college': college}


def requirementform(request, pk):
    id = pk
    ngo = Ngo.objects.get(user_id=id)
    form = RequirementsForm()
    if request.method == "POST":
        form = RequirementsForm(request.POST)
        if form.is_valid():
            r = form.save()
            r.ngo = ngo
            r.save()
            return redirect('main:tabular', id)
    else:
        form = RequirementsForm()
    context = {'id': id, 'form': form}
    return render(request, 'main/requirementform.html', context)


# def add_student(request, pk):
#     StudentFormSet = inlineformset_factory(
#         College, Student, fields=('name', 'stream_name', 'college_name'), extra=10)
#     colleges = College.objects.get(id=pk)
#     # print(colleges)
#     formset = StudentFormSet(
#         queryset=Student.objects.none(), instance=colleges)
#     if request.method == 'POST':
#         formset = StudentFormSet(request.POST, instance=colleges)
#         # if paranthesis missing then error = studentform doesnot have the attribute cleaned_data
#         if formset.is_valid():
#             formset.save()
#             return redirect('homePage')
#     context = {'formset': formset}
#     return render(request, 'college/add_student.html', context)


def summary(request, pk):
    id = pk
    ngos = Ngo.objects.get(user_id=id)
    requirements = Requirements.objects.filter(ngo=ngos)
    print(requirements)
    donated = Donate.objects.all()
    context = {'id': id, 'donated': donated}
    return render(request, 'main/summary.html', context)


@ ngo_user_required
def tabular(request, pk):
    id = pk
    ngos = Ngo.objects.get(user_id=id)
    requirements = Requirements.objects.filter(ngo=ngos)

    # @register.filter(name='subtract')
    # def subtract(value, arg):
    #     return value - arg
    # print(requirements)
    context = {'id': id, 'requirements': requirements}
    return render(request, 'main/tabular.html', context)


@ donor_user_required
def user_requirements(request, pk):
    donor = request.user.donor
    object_list = Requirements.objects.filter(ngo__city = donor.city)
    categories = ['Medicine', 'Food', 'Clothing', 'Stationary']
    # paginator = Paginator(object_list, 6)
    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    context = {'object_list':object_list, 'categories':categories, 'user_id':pk}
    return render(request, 'main/user.html', context)

def user_requirements_category(request, pk, cat):
    donor = request.user.donor
    print(donor, donor.city,"=======================")
    print(cat)
    object_list = Requirements.objects.filter(ngo__city = donor.city).filter(category=cat)
    print(object_list)
    context = {'object_list':object_list}
    return render(request, 'main/user_requirements.html', context=context)


# def ngo_summary(request, pk):
#     context = {}
#     return render(request, 'main/summary.html', context)


# def ngo_tabular(request, pk):
#     context = {}
#     return render(request, 'main/tabular.html', context)


# @ngo_user_required
# def ngo_requirementform(request, pk):
#


def donation(request, pk):
    req = Requirements.objects.get(id=pk)
    donor = Donor.objects.get(user_id=request.user.id)
    form = DonationForm()
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            r = form.save()
            r.ngo = req.ngo
            r.user = donor
            r.requirements_name = req
            if r.count <= req.initial_count:
                req.donation_count = r.count
                req.save()
                r.save()
                return redirect('main:user', pk)
            else:
                return HttpResponse("Donation count exceeded Donation count")
    context = {'req': req, 'form': form}
    return render(request, 'main/donation.html', context)


def ngo_list(request):        
    ngos = Ngo.objects.all()
    user = request.user.id
    paginator = Paginator(ngos, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts, 'page':page, 'user_id':user}
    return render(request, 'main/ngo.html', context)

def ngo_search(request, pk):
        user = request.user.id
        ngo_list = Ngo.objects.filter(ngo_name__contains=pk)
        context = {'posts':ngo_list, 'user_id':user}
        return render(request, 'main/ngo_search.html', context)


def chat(request):
    
    return render(request, 'main/chat.html')
