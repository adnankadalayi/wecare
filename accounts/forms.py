from . models import Accounts
from django import forms


class RegistrationForm(forms.ModelForm):
    password = forms.CharField( widget=forms.PasswordInput())
    confirm_password = forms.CharField( widget=forms.PasswordInput())
    class Meta:
        model = Accounts
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ' Password'
        self.fields['confirm_password'].label = 'Confirm Password'
      
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

            

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError('Password do not match')
