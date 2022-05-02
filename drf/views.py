from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets


# Create your views here.


@api_view(['GET'])
def ngo(request):
    ngo = Ngo.objects.all()
    context = NgoSerializer(ngo, many=True)
    return Response(context.data)


@api_view(['GET'])
def donor(request):
    donor = Donor.objects.all()
    context = DonorSerializer(donor, many=True)
    return Response(context.data)


@api_view(['GET'])
def user(request):
    user = User.objects.all()
    context = UserSerializer(user, many=True)
    return Response(context.data)


# for hyperlinked
class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer


class DonateViewSet(viewsets.ModelViewSet):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
