from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic  import TemplateView,FormView
from .models import *
from .forms import MasterEmployeesForm



class HomeView(TemplateView):
    template_name = 'index.html'

class AddUserView(FormView):
    template_name = 'form.html'
    form_class = MasterEmployeesForm
    success_url = '.'

    def form_valid(self, form):
        form.save()
        return super(AddUserView, self).form_valid(form)

class EmployeeProfileView(TemplateView):
    template_name = 'profile.html'

