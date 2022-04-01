from django.contrib import admin
from dashboard.models import Subject,Routine,Faulty

# Register your models here.

class AdminSubject(admin.ModelAdmin):
    list_display = ['id','subject','semister','faulty']
admin.site.register(Subject,AdminSubject)


class AdminFaulty(admin.ModelAdmin):
    list_display = ['id','faulty']
admin.site.register(Faulty,AdminFaulty)

class AdminRoutine(admin.ModelAdmin):
    list_display = ['id','semister','subject','faulty','time','day','teacher']
admin.site.register(Routine,AdminRoutine)
