from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic  import TemplateView,FormView,UpdateView,View,DeleteView,CreateView,ListView
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
    template_name = 'profile.html'



class EmployeeProfileDeleteView(View):

    def delete(self, request,**kwargs):
        # delete an object and send a confirmation response
        MasterEmployees.objects.get(employee_code=self.kwargs.get['pk']).delete()
        return HttpResponse()



class MasterSkillsAddView(CreateView):
    template_name = 'skill.html'
    model = MasterSkills
    fields = ('skill',)
    success_url ='/training/skill_list/'

class MasterSkillListView(ListView):
    template_name = 'skill_list.html'
    model = MasterSkills
    success_url = '/training/skill_list/'
