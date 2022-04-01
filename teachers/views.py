from django.shortcuts import render,redirect

'''
    custom class and functions 
'''
from teachers.forms import TeacherCreactionForm
from sendemailverification.send_email import send_custom_mail
import random
from accounts.models import OtpEmail

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
def teacher_register_view(request):
    if request.method == "POST":
        form = TeacherCreactionForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            request.session['uid'] = user.pk
            token = default_token_generator.make_token(user)
            otp = random.randint(100000, 500000)
            otp_create = OtpEmail.objects.create(otp=otp,user=user)
            otp_create.save()
            text = "Please verify your teacher account !"
            send_custom_mail(request, user, otp,text)
            return redirect('validate-email',token)

    form = TeacherCreactionForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/teacher_register.html',context)




def dashboard(request):
    return render(request, 'teacher/dashboard.html')
