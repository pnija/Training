"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,static
from .views import HomeView,AddEmployeeView,EmployeeProfileEditView,EmployeeProfileView,EmployeeProfileDeleteView,\
    MasterSkillsAddView,MasterSkillListView


urlpatterns = [
    url(r'^home/', HomeView.as_view(),name='home'),
    url(r'^add-employee/(?P<pk>\d+)/$', EmployeeProfileEditView.as_view(),name='edit_profile'),
    url(r'^add-employee/', AddEmployeeView.as_view(),name='add-employee'),
    url(r'^delete_profile/(?P<pk>\d+)/$', EmployeeProfileDeleteView.as_view(),name='delete_profile'),
    url(r'^user-profile/(?P<pk>\d+)/', EmployeeProfileView.as_view(),name='profile'),
    url(r'^master-skills/', MasterSkillsAddView.as_view(), name='master_skills'),
    url(r'^skill_list/', MasterSkillListView.as_view(), name='master_skill_list'),

]
