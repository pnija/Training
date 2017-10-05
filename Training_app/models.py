from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DepartmentGroups(models.Model):
    group_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.group_name

class MasterDesignations(models.Model):
    designation_name = models.CharField(max_length=255)
    department_group = models.ForeignKey(DepartmentGroups)

    def __unicode__(self):
        return self.designation_name

class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.department_name

class EmployeeCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category_name

class MasterEmployees(models.Model):
    employee_code = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    category = models.ForeignKey(EmployeeCategory)
    department = models.ForeignKey(Department)
    designation = models.ForeignKey(MasterDesignations)

    def __unicode__(self):
        return self.employee_name

class SkillGroups(models.Model):
    group_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.group_name

class SkillTrainingTypes(models.Model):
    training_type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.training_type

class MasterSkills(models.Model):
    skill = models.CharField(max_length=255)
    training_type = models.ForeignKey(SkillTrainingTypes)
    group = models.ForeignKey(SkillGroups)
    required_level = models.FloatField(default=None, null=True, blank=True)

    def __unicode__(self):
        return self.skill

class SkillDesignationMapping(models.Model):
    designation = models.ForeignKey(MasterDesignations)
    skills = models.ForeignKey(MasterSkills)
    required_competance = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    reporting_to = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)

    def __unicode__(self):
        return self.required_compatance



class EmployeeSkillMapping(models.Model):
    skill = models.ForeignKey(SkillDesignationMapping)
    competence = models.FloatField(default=None)
    qc_inspector = models.ForeignKey(MasterEmployees)
    current_level = models.FloatField(default=None)
    skill_gap = models.FloatField(default=None)

class TrainingSkillTracking(models.Model):
    designation = models.ForeignKey(MasterDesignations)
    skill = models.ForeignKey(SkillDesignationMapping)
    required_level = models.FloatField(default=None)
    skill_needed = models.FloatField(default=None)

class SkillTrainingShedule(models.Model):
    skill = models.ForeignKey(MasterSkills)
    trainer_designation = models.ForeignKey(MasterDesignations)
    trainer_name = models.CharField(max_length=255)
    plan_date = models.DateField()
    actual_date = models.DateField()

class TrainingAttendance(models.Model):
    skill = models.ForeignKey(MasterSkills)
    trained_date = models.DateField()
    trainee = models.ForeignKey(MasterEmployees)

class TrainingSkillRequired(models.Model):
    skill = models.ForeignKey(SkillDesignationMapping)
    required_level = models.FloatField(default=None)
