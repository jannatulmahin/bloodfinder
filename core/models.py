from django.db import models



BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

URGENCY_CHOICES = [
    ('Normal', 'Normal'),
    ('Urgent', 'Urgent'),
    ('Critical', 'Critical'),
]

REQUEST_STATUS = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ('Completed', 'Completed'),
]

class Donor(models.Model):
    full_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    address = models.TextField()
    last_donation_date = models.DateField(blank=True, null=True)
    available = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.blood_group}"


class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=150)
    blood_group_needed = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    units_needed = models.PositiveIntegerField(default=1)
    hospital_name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    hospital_address = models.TextField()
    required_date = models.DateField()
    required_time = models.TimeField()
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    contact_person = models.CharField(max_length=150)
    contact_phone = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} needs {self.blood_group_needed}"
