from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic  import TemplateView,FormView,UpdateView,View,DeleteView
from django.views.generic.detail import SingleObjectMixin
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


class EmployeeProfileEditView(UpdateView):
    template_name = 'form_update.html'
    model = MasterEmployees
    form_class = MasterEmployeesForm
    success_url = '/training/home/'
    
    def form_valid(self, form):
        form.save()
        return super(EmployeeProfileEditView, self).form_valid(form)


class EmployeeProfileView(TemplateView):
    def get(self, request, **kwargs):
        pk = self.kwargs.get('pk')
        employee_object = MasterEmployees.objects.get(pk = pk)
        return render(request,'profile.html',{'employee_object':employee_object})



class EmployeeProfileDeleteView(View):

    def get(self, *args, **kwargs):
        id = self.kwargs.get('pk')
        MasterEmployees.objects.get(employee_code = id).delete()
        return HttpResponseRedirect('/training/home/')


