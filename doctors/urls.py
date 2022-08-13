from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_home, name='doctor_home'),
    path('signup', views.doctor_signup, name='doctor_signup'),
    path('login', views.doctor_login, name='doctor_login'),
    path('logout', views.doctor_logout, name='doctor_logout'),
    path('profile/<int:id>', views.doctor_profile, name='doctor_profile'),
]