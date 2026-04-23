from django import forms
from .models import Donor, BloodRequest

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'full_name',
            'age',
            'gender',
            'blood_group',
            'phone',
            'email',
            'district',
            'area',
            'address',
            'last_donation_date',
            'available',
        ]
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = [
            'patient_name',
            'blood_group_needed',
            'units_needed',
            'hospital_name',
            'district',
            'area',
            'hospital_address',
            'required_date',
            'required_time',
            'urgency',
            'contact_person',
            'contact_phone',
            'note',
        ]
        widgets = {
            'required_date': forms.DateInput(attrs={'type': 'date'}),
            'required_time': forms.TimeInput(attrs={'type': 'time'}),
        }