from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor, BloodRequest
from .forms import DonorForm, BloodRequestForm

def home(request):
    donor_count = Donor.objects.count()
    available_donor_count = Donor.objects.filter(available=True).count()
    request_count = BloodRequest.objects.count()

    context = {
        'donor_count': donor_count,
        'available_donor_count': available_donor_count,
        'request_count': request_count,
    }
    return render(request, 'core/home.html', context)


def donor_register(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'core/donor_register.html', {'form': form})


def donor_list(request):
    donors = Donor.objects.all().order_by('-id')

    blood_group = request.GET.get('blood_group')
    district = request.GET.get('district')
    area = request.GET.get('area')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if district:
        donors = donors.filter(district__icontains=district)

    if area:
        donors = donors.filter(area__icontains=area)

    return render(request, 'core/donor_list.html', {'donors': donors})


def donor_detail(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    return render(request, 'core/donor_detail.html', {'donor': donor})


def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = BloodRequestForm()

    return render(request, 'core/request_blood.html', {'form': form})


def request_list(request):
    requests = BloodRequest.objects.all().order_by('-created_at')
    return render(request, 'core/request_list.html', {'requests': requests})