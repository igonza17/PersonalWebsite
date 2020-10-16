from django.contrib import admin
from .models import Courses, PreRequisite
# Register your models here.
class coursesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'department', 'course_number', 'course_name', 'semester', 'sem_year', 'grade')
    def info(self,obj):
        return obj.description
    info.short_description = 'info'
admin.site.register(Courses,coursesAdmin)

class preReqAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'prereq1', 'prereq2')
    def info(self,obj):
        return obj.description
    info.short_description = 'info'
admin.site.register(PreRequisite, preReqAdmin)