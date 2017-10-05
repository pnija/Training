from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class DepartmentGroups(models.Model):
    group_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.group_name

class MasterDesignations(models.Model):
    designation_name = models.CharField(max_length=255)
    department_group = models.ForeignKey(DepartmentGroups, related_name='get_designations_by_group')

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
    category = models.ForeignKey(EmployeeCategory, related_name='get_employess_in_category',null=True,blank=True)
    department = models.ForeignKey(Department, related_name='get_employess_in_department',null=True,blank=True)
    designation = models.ForeignKey(MasterDesignations, related_name='get_employess_by_designation',null=True,blank=True)
    employee_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True,blank=True)
    address  = models.TextField(max_length=255)
    date_of_birth = models.DateField(null=True,blank=True)
    email = models.EmailField(max_length=40,null=True,blank=True)
    date_of_joining = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=25,null=True,blank=True)
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
    training_type = models.ForeignKey(SkillTrainingTypes, related_name='get_skills_by_training_type')
    group = models.ForeignKey(SkillGroups, related_name='get_skills_by_groups')

    def __unicode__(self):
        return self.skill

class SkillDesignationMapping(models.Model):
    designation = models.ForeignKey(MasterDesignations, related_name='get_mapping_skill_designation_by_designation')
    skills = models.ForeignKey(MasterSkills, related_name='get_mapping_skill_designation_by_skills')
    required_competance = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    reporting_to = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)

    def __unicode__(self):
        return self.required_compatance



class EmployeeSkillMapping(models.Model):
    designation_skill = models.ForeignKey(SkillDesignationMapping, related_name='get_employee_skill_mapping_by_designation_skills')
    qc_inspector = models.ForeignKey(MasterEmployees, related_name='get_employee_skill_mapping_by_employee')
    current_level = models.FloatField(default=None)
    skill_gap = models.FloatField(default=None)

    def __unicode__(self):
        return self.skill.designation.designation_name +'-'+self.qc_inspector.employee_name


class TrainingSkillTracking(models.Model):
    designation_skill = models.ForeignKey(SkillDesignationMapping, related_name='get_skill_training_tracking_by_designation_skills')
    training_needed = models.FloatField(default=None)
    updated_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.skill.designation.designation_name

class SkillTrainingShedule(models.Model):
    training_id = models.IntegerField(primary_key=True)
    skill = models.ForeignKey(SkillDesignationMapping, related_name='get_training_schedule_by_designation_skills')
    trainer_name = models.CharField(max_length=255)
    plan_date = models.DateField()
    actual_date = models.DateField()

    def __unicode__(self):
        return self.skill.skills.skill

class TrainingAttendance(models.Model):
    skill = models.ForeignKey(MasterSkills, related_name='get_training_attendance_by_skill')
    trained_date = models.DateField()
    trainee = models.ForeignKey(MasterEmployees, related_name='get_training_attendance_by_employee')

    def __unicode__(self):
        return self.skill.skill

class TotalTrainingRequirement(models.Model):
    skill = models.ForeignKey(MasterSkills,related_name='get_required_training_in_skills')
    training_required = models.FloatField(default=None, null=True, blank=True)

