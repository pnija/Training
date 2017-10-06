from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import MasterEmployees,MasterSkills,SkillGroups


class MasterEmployeesForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    date_of_joining = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    profile_pic = forms.ImageField(required=True)

    class Meta:
        model = MasterEmployees
        fields = ('employee_name','gender','employee_code',
                  'profile_pic','address','date_of_birth',
                  'email','date_of_joining','location','phone_number','department','designation')




class MasterSkillsForm(forms.ModelForm):
    class Meta:
        model = MasterSkills
        fields = '__all__'

class SkillGroupsForm(forms.ModelForm):
    class Meta:
        model = SkillGroups
        fields = '__all__'