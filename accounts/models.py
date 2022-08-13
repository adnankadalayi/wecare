from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from doctors.models import Doctor_Detail

class MyAccountManager(BaseUserManager):
    
    #create user with f.name, l.name, username set password and save user 
    def create_user(self, first_name, last_name, phone_number, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name  = last_name,
            phone_number   = phone_number,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
     
     # superuser
    def create_superuser(self, first_name, email, last_name, password):
        user = self.model(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
            username    = email.split('@')[0],
            password    = password,

        )

        user.is_staff       = True
        user.is_admin       = True
        user.is_superadmin  = True
        user.is_active      = True
        user.is_doctor      = True
        user.is_patient      = True

        user.set_password(password)
        user.save(using=self.db)
        return user
     
#account model 
class Accounts(AbstractBaseUser):
    first_name      = models.CharField( max_length=50)
    last_name       = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    username        = models.CharField(max_length=50,unique=True)
    phone_number    = models.CharField( max_length=10, unique=True)
    is_active       = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_doctor       = models.BooleanField(default=False)
    is_patient      = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    is_activated    = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    details         = models.ForeignKey(Doctor_Detail, on_delete=models.SET_NULL, null=True)

    #email field in username
    # changed to username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    #telling its objects on MyAccountManager
    objects = MyAccountManager()

    #str form of model
    def __str__(self):  
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def full_name(self):                                                       
        return f'{self.first_name} {self.last_name}' 
   



    #changing name
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'