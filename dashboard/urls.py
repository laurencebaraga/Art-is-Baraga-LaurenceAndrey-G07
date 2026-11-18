from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_redirect, name='dashboard'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('artist/', views.artist_dashboard, name='artist_dashboard'),
]