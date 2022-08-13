from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import Accounts
from django.contrib.auth.decorators import login_required
from .forms import SpecialityForm
from admin_panel.models import Speciality

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                print(user)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # messages.success(request, "Your account has been successfully logged in.")
                return redirect('dashboard')
        messages.error(request, "Invalid Credentials")
    return render(request, 'admin_panel/login.html')

@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url='admin_login')
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

@login_required(login_url='admin_login')
def doctors(request):
    doctors = Accounts.objects.filter(is_doctor=True)

    context = {
        'doctors': doctors,
        }
    return render(request, 'admin_panel/doctors.html', context)

@login_required(login_url='admin_login')
def patients(request):
    patients = Accounts.objects.filter(is_patient=True)

    context = {
        'patients': patients,
        }
    return render(request, 'admin_panel/patients.html', context)

def activate(request, id):
    doctor = Accounts.objects.get(id=id)
    print(doctor)
    doctor.is_activated = True
    doctor.save()
    return redirect('doctors')

def deactivate(request, id):
    doctor = Accounts.objects.get(id=id)
    print(doctor)
    doctor.is_activated = False
    doctor.save()
    return redirect('doctors')

def specialities(request):
    specialities = Speciality.objects.all()
    context = {
        'specialities': specialities,
        }
    return render(request, 'admin_panel/specialities.html', context)

def add_speciality(request):
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialities')
    else:
        form = SpecialityForm()
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/add_specialities.html', context)

def edit_speciality(request, id):
    speciality = Speciality.objects.get(id=id)
    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=speciality)
        if form.is_valid():
            form.save()
            return redirect('specialities')
    else:
        form = SpecialityForm(instance=speciality)
    context = { 
        'form': form,
    }
    return render(request, 'admin_panel/edit_specialities.html', context)

def delete_speciality(request, id):
    speciality = Speciality.objects.get(id=id)
    speciality.delete()
    return redirect('specialities')