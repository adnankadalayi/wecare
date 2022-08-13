from django.forms import ModelForm
from .models import Doctor_Detail

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor_Detail
        exclude = ['user']
        # exclude = ['user', 'age', 'gender', 'registration_no', 'state_medical_council']

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
      
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["age", "gender", "registration_no"]
        else:
            return []