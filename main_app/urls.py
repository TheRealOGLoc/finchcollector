# main_app/urls.py

from django.urls import path
from . import views
from .views import FinchDetailView, ToyCreateView
urlpatterns = [
    path('', views.FinchListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('finches/<int:pk>/', views.FinchDetailView.as_view(), name='finch_detail'),
    path('finches/create/', views.FinchCreateView.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdateView.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDeleteView.as_view(), name='finch_delete'),
    path('finches/<int:pk>/add_toy/', ToyCreateView.as_view(), name='toy_create'),
]
