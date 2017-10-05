from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic  import TemplateView,FormView
from .models import *
from .forms import MasterEmployeesForm



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['employees'] = MasterEmployees.objects.all
        return context

class AddEmployeeView(FormView):
    template_name = 'form.html'
    form_class = MasterEmployeesForm
    success_url = '.'

    def form_valid(self, form):
        form.save()
        return super(AddEmployeeView, self).form_valid(form)

