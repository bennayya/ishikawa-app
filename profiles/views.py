from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


#def showAll(request):
    #profiles = Profile.objects.all()
   # return HttpResponse(profiles)
