from django.contrib import admin
from .models import Donor, BloodRequest

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'blood_group', 'phone', 'district', 'area', 'available', 'verified']
    list_filter = ['blood_group', 'district', 'available', 'verified']
    search_fields = ['full_name', 'phone', 'district', 'area']


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'blood_group_needed', 'hospital_name', 'district', 'urgency', 'status', 'required_date']
    list_filter = ['blood_group_needed', 'urgency', 'status', 'district']
    search_fields = ['patient_name', 'contact_person', 'contact_phone', 'hospital_name']