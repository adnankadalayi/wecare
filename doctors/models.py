from django.db import models
# from accounts.models import Accounts

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class Doctor_Detail(models.Model):
    user                    = models.ForeignKey('accounts.Accounts', on_delete=models.CASCADE)
    age                     = models.IntegerField()
    gender                  = models.CharField(choices=GENDER, max_length=10)
    medical_speciality      = models.ForeignKey('admin_panel.Speciality', on_delete=models.SET_NULL, null=True)
    degree                  = models.CharField(max_length=255)
    experience              = models.IntegerField()
    registration_no         = models.IntegerField()
    state_medical_council   = models.CharField(max_length=255)
    address                 = models.TextField(max_length=255)

    def __str__(self):
        return self.user.first_name
    