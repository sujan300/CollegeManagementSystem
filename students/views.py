from django.shortcuts import render,HttpResponse,redirect
from students.forms import StudentCreationForm

'''
    for security purpose 
'''
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from accounts.decorators import student_required
from django.contrib.auth.decorators import login_required


'''
    custom functions
'''
from sendemailverification.send_email import send_custom_mail
import random
from accounts.models import OtpEmail

# Create your views here.



'''
    this part only for authenticate for students 
'''
def student_register_view(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            user.is_emailverified = False
            user.save()
            request.session['uid'] = user.pk
            token = default_token_generator.make_token(user)
            otp = random.randint(100000, 500000)
            otp_create = OtpEmail.objects.create(otp=otp,user=user)
            otp_create.save()
            text = "please verify your student account !"
            send_custom_mail(request, user, otp,text)
            return redirect('validate-email',token)
    else:
        form = StudentCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/student_register.html',context)




'''
    below this only for student dashboard
'''


@login_required(login_url='login')
@student_required(login_url='login')
def dashboard(request):
    print("students required")
    return render(request, 'students/dashboard.html')


@login_required(login_url='login')
@student_required(login_url='login')
def student_routine_view(request):
    print("yes this is student routine view !!!")
    return render(request, 'students/routine_student.html')