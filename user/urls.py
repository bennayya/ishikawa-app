# userapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.user_list),
    path('api/user/<int:id>/', views.user_detail),
]
