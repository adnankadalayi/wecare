from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('signup/', views.signup_view, name= 'signup'),
    path('verify_otp/', views.verify_otp, name= 'verify_otp'),
    path('otp_login/', views.otp_login, name= 'otp_login'),
]
