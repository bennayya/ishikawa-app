# urls.py
from django.urls import path
from .views import IshikawaDiagramList, IshikawaDiagramDetail

from django.urls import path
from .views import IshikawaDiagramList, IshikawaDiagramDetail, CategoryList, CategoryDetail, CauseList, CauseDetail

urlpatterns = [
    path('api/ishikawa_diagrams/', IshikawaDiagramList.as_view(), name='ishikawa-diagram-list'),
    path('api/ishikawa_diagrams/<int:pk>/', IshikawaDiagramDetail.as_view(), name='ishikawa-diagram-detail'),
    path('api/categories/', CategoryList.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/causes/', CauseList.as_view(), name='cause-list'),
    path('api/causes/<int:pk>/', CauseDetail.as_view(), name='cause-detail'),
]
