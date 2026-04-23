from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donor/register/', views.donor_register, name='donor_register'),
    path('donors/', views.donor_list, name='donor_list'),
    path('donor/<int:donor_id>/', views.donor_detail, name='donor_detail'),
    path('request-blood/', views.request_blood, name='request_blood'),
    path('requests/', views.request_list, name='request_list'),
]