from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from accounts.models import Accounts
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from doctors.forms import DoctorForm
from .models import Doctor_Detail

def doctor_home(request):
    if request.user.is_authenticated:
        return render(request,'doctors/home.html')
    return redirect('doctor_login')

def doctor_signup(request):
    if request.user.is_authenticated:
        return redirect('doctor_home')
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('form valid')
            first_name  = form.cleaned_data.get('first_name')
            last_name   = form.cleaned_data.get('last_name')
            phone_number    = form.cleaned_data.get('phone_number')
            email       = form.cleaned_data.get('email')
            password    = form.cleaned_data.get('password')
            
            user = Accounts.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, password=password)
            user.phone_number = phone_number
            user.username = email.split('@')[0]
            print(user)
            print(user.is_active)
            user.is_active = True
            user.is_doctor = True
            print(user.is_active)
            user.save()
            print('user saved')
            print(user)
            return redirect('doctor_login')
    else:
       
        form = RegistrationForm()

    context = {
        'form' : form,
    }
    return render(request,'doctors/signup.html', context)

def doctor_login(request):
    if request.user.is_authenticated:
        return redirect('doctor_home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print('user', user)
        if user is not None:
            print('not none')
            print(user)
            login(request, user)
            return redirect('doctor_home')
        messages.error(request, "Invalid Credentials")
    return render(request,'doctors/login.html')

def doctor_logout(request):
    logout(request)
    return redirect('doctor_login')

def doctor_profile(request, id):
    try:
        user = Doctor_Detail.objects.get(user_id=id)
    except :
        user = None
    print(user)
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=user)
        register_form = RegistrationForm(request.POST, instance=request.user)
        print('edit')
        if doctor_form.is_valid() and register_form.is_valid():
            doctor_form.save()
            register_form.save()
            print('edit and saved')

    else:
        doctor_form = DoctorForm(instance=user)
        register_form = RegistrationForm(instance=request.user)

    if request.method == 'POST':
        add_doctor_form = DoctorForm(request.POST)
        add_register_form = RegistrationForm(request.POST)
        print('add')
        if doctor_form.is_valid() and register_form.is_valid():
            doctor_form.save()
            register_form.save()
            print('added and saved')

    else:
        add_doctor_form = DoctorForm()
        add_register_form = RegistrationForm()
        
    context = {
        'doctor': user,
        'doctor_form': doctor_form,
        'register_form': register_form,
        'add_doctor_form': add_doctor_form,
        'add_register_form': add_register_form,
    }
    return render(request,'doctors/doctor_profile.html', context)