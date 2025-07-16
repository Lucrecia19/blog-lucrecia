from django.urls import path 
from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/eliminar/', PageDeleteView.as_view(), name='page_delete'),
]
