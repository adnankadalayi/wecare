from django import forms
from .models import Speciality

class SpecialityForm(forms.ModelForm):
    
    class Meta:
        model = Speciality
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpecialityForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
