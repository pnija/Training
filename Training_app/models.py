from django.db import models

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

class MasterEmployes(models.Model):
    category = models.ForeignKey(EmployeCategory)
    employe_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department)
    designation = models.ForeignKey(MasterDesignations)
