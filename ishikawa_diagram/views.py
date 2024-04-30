""""
from django.shortcuts import render
from rest_framework import generics
from .models import IshikawaDiagram
from .serializers import IshikawaDiagramSerializer

class IshikawaDiagramList(generics.ListCreateAPIView):
    queryset = IshikawaDiagram.objects.all()
    serializer_class = IshikawaDiagramSerializer

class IshikawaDiagramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IshikawaDiagram.objects.all()
    serializer_class = IshikawaDiagramSerializer
"""
from rest_framework import generics
from .models import IshikawaDiagram, Category, Cause
from .serializers import IshikawaDiagramSerializer, CategorySerializer, CauseSerializer

class IshikawaDiagramList(generics.ListCreateAPIView):
    queryset = IshikawaDiagram.objects.all()
    serializer_class = IshikawaDiagramSerializer

class IshikawaDiagramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IshikawaDiagram.objects.all()
    serializer_class = IshikawaDiagramSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CauseList(generics.ListCreateAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer

class CauseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
