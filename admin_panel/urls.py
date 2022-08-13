from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name= 'dashboard'),
    path('doctors', views.doctors, name= 'doctors'),
    path('patients', views.patients, name= 'patients'),
    path('specialities', views.specialities, name= 'specialities'),
    path('add_speciality', views.add_speciality, name= 'add_speciality'),
    path('delete_speciality/<int:id>', views.delete_speciality, name= 'delete_speciality'),
    path('edit_speciality/<int:id>', views.edit_speciality, name= 'edit_speciality'),
    path('login', views.admin_login, name= 'admin_login'),
    path('logout', views.admin_logout, name= 'admin_logout'),
    path('activate/<int:id>', views.activate, name= 'activate'),
    path('deactivate/<int:id>', views.deactivate, name= 'deactivate'),
]