from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('doctor/', include('doctors.urls')),
    path('', include('patients.urls')),
    path('superuser/', include('admin_panel.urls')),
    path('accounts/', include('allauth.urls')),
    
]
