"""from django.urls import path ,include
from .views import show_all

urlpatterns = [
   # path('api/incident/',),
    #path('',include( 'incident.urls')),
    path('', show_all, name='show_all'),
]
"""
from django.urls import path, include
from django.contrib import admin

from .views import  IncidentDetail, IncidentList

urlpatterns = [
    
    path('api/incident/', IncidentList.as_view()),
    path('api/incident/<int:pk>/', IncidentDetail.as_view(), name='incident-detail'),
    
]



