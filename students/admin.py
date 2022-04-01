from django.contrib import admin
from students.models import StudentAccount

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','user','gender','date_of_birth',"semister"]
admin.site.register(StudentAccount,AdminStudent)