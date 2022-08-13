from django.db import models
from doctors.models import Doctor_Detail

# Create your models here.
class Speciality(models.Model):
    speciality  = models.CharField(max_length=255)
    discription = models.TextField()
    # doctor      = models.ForeignKey(Doctor_Detail, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.speciality
    

    class Meta:
        verbose_name_plural = 'Speciality'