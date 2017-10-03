from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DepartmentGroups(models.Model):
    group_name = models.CharField(max_length=255)

class MasterDesignations(models.Model):
    designation_name = models.CharField(max_length=255)
    department_group = models.ForeignKey(DepartmentGroups)

class Department(models.Model):
    department_name = models.CharField(max_length=255)

class EmployeCategory(models.Model):
    category_name = models.CharField(max_length=255)

class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

class MasterEmployes(models.Model):
    category = models.ForeignKey(EmployeCategory)
    employee = models.ForeignKey(Employee)
    department = models.ForeignKey(Department)
    designation = models.ForeignKey(MasterDesignations)

class SkillGroups(models.Model):
    group_name = models.CharField(max_length=255)

class SkillTrainingTypes(models.Model):
    training_type = models.CharField(max_length=255)

class MasterSkills(models.Model):
    skill = models.CharField(max_length=255)
    training_type = models.ForeignKey(SkillTrainingTypes)
    group = models.ForeignKey(SkillGroups)

class SkillDesignationMapping(models.Model):
    designation = models.ForeignKey(MasterDesignations)
    skills = models.ForeignKey(MasterSkills)
    required_compatance = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    reporting_to = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)
