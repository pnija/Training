from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DepartmentGroups)
admin.site.register(MasterDesignations)
admin.site.register(Department)
admin.site.register(EmployeeCategory)
admin.site.register(MasterEmployees)
admin.site.register(SkillGroups)
admin.site.register(SkillTrainingTypes)
admin.site.register(MasterSkills)
admin.site.register(SkillDesignationMapping)
admin.site.register(EmployeeSkillMapping)
admin.site.register(TrainingSkillTracking)
admin.site.register(SkillTrainingShedule)
admin.site.register(TrainingAttendance)


