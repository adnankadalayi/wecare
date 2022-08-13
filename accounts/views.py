from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import Accounts
from django.contrib.auth.decorators import login_required
import random
from twilio.rest import Client

# Create your views here.
def home(request):
    # if request.user.is_authenticated:
    #     if request.user.is_patient:
            return render(request, 'home.html')
    # return redirect('login')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name  = form.cleaned_data.get('first_name')
            last_name   = form.cleaned_data.get('last_name')
            phone_number    = form.cleaned_data.get('phone_number')
            email       = form.cleaned_data.get('email')
            password    = form.cleaned_data.get('password')
            
            user = Accounts.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, password=password)
            user.phone_number = phone_number
            user.username = email.split('@')[0]
            user.is_patient = True
            user.save()

        # otp account verification
            request.session["mobile"] = phone_number
            user = Accounts.objects.filter(phone_number=phone_number)

            for m in user:
                if m.phone_number == phone_number:
                    user_mobile = phone_number
                    user_mobile
                    

                    account_sid = 'ACe3f88ce90341561def57fbb8b601e699'
                    auth_token = 'fa8af45db1c1850d405c685a0787ee49'
                    # client = Client(settings.ACCOUNT_SIF, settings.AUTH_TOKEN)
                    client = Client(account_sid, auth_token)

                    generated_otp = random.randrange(1000,9999)
                    print(generated_otp)

                    message = client.messages.create(
                                                body='Your OTP code is ' + str(generated_otp),
                                                from_='+19097265332',
                                                to='+91'+(user_mobile)
                                            )
                    print(message.body)
                    print(message.sid)
                    request.session['phone_number'] = phone_number   
                    return redirect('verify_otp')
           
    else:
       
        form = RegistrationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def verify_otp(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        generated_otp = request.session.get('backend_otp')
        print(generated_otp)
        user_otp = request.POST.get('otp')
        print(user_otp)
        if int(user_otp) == int(generated_otp):
            # messages.success(request, "OTP verified successfully.")
            phone_number = request.session.get('phone_number')
            print(phone_number)
            user = Accounts.objects.get(phone_number=phone_number)
            print(user)
            user.is_active = True
            user.save()
            print('saved')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print('login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('verify_otp')
    else:
        print('incorrect method')
        return render(request, 'accounts/otp_form.html')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_patient:
                print(user)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # messages.success(request, "Your account has been successfully logged in.")
                return redirect('home')
        messages.error(request, "Invalid Credentials")
    return render(request, 'accounts/login.html')

def otp_login(request, **generated_otp):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        user = Accounts.objects.filter(phone_number=phone_number)
        for i in user:
            if i.phone_number == phone_number:
                user_mobile = phone_number
            
                account_sid = 'ACe3f88ce90341561def57fbb8b601e699'
                auth_token = 'fa8af45db1c1850d405c685a0787ee49'
                # client = Client(settings.ACCOUNT_SIF, settings.AUTH_TOKEN)
                client = Client(account_sid, auth_token)
                generated_otp = random.randrange(1000,9999)
                print(generated_otp)
                request.session['backend_otp'] = generated_otp
                message = client.messages.create(
                                            body='Your OTP code is ' + str(generated_otp),
                                            from_='+19097265332',
                                            to='+91'+(user_mobile)
                                        )
                print(message.body)
                print(message.sid)
                request.session['phone_number'] = phone_number   
                return redirect('verify_otp')
        else:
            messages.error(request, 'Enter correct Phone Number')
            return redirect('otp_login')
    return render(request, 'accounts/otp_login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')