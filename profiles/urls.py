from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('api/profiles/', ProfileList.as_view()),
    path('api/profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    #path('',showAll)
]
