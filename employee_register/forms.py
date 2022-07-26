from django.forms import forms,ModelForm
from .models import *

class RegistrationForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = (
            ('full_name' , 'Full Name'),
            ('emp_code' , 'Emp_Code')

        )