from django.contrib import admin
from teachers.models import TeacherAccount

# Register your models here.
class AdminTeacher(admin.ModelAdmin):
    list_display = ['id','user','gender']
admin.site.register(TeacherAccount,AdminTeacher)