from django.contrib import admin
from accounts.models import Account,OtpEmail

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','is_admin','is_staff','is_active','is_superadmin','is_emailverified','is_student','is_teacher']
admin.site.register(Account,AccountAdmin)


class OtpEmailAdmin(admin.ModelAdmin):
    list_display = ["id",'otp','user']

admin.site.register(OtpEmail,OtpEmailAdmin)