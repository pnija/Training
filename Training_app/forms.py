from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import MasterEmployees


class MasterEmployeesForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    date_of_joining = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    class Meta:
        model = MasterEmployees
        fields = ('employee_name','gender','employee_code',
                  'profile_pic','address','date_of_birth',
                  'email','date_of_joining','location','department','designation')
