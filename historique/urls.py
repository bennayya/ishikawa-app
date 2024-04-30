from django.urls import path, include
from django.contrib import admin

from .views import  HistoriqueDetail, HistoriqueList

urlpatterns = [
    
    path('api/historique/', HistoriqueDetail.as_view()),
    path('api/historique/<int:pk>/', HistoriqueList.as_view(), name='historique-detail'),
    
]