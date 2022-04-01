from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from accounts.models import Account,OtpEmail
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from accounts.forms import LoginForm
from django.contrib.auth.decorators import login_required
from students.models import StudentAccount




from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


import random

# custom email OtpEmail
from accounts.models import OtpEmail







def validate_email(request,token):
    if request.method == "POST":
        uid = request.session['uid']
        otp_submit = request.POST.get('otp')
        try:
            user = Account.objects.get(pk=uid)
            otp  = str(OtpEmail.objects.get(user=user))
            user_delete= OtpEmail.objects.get(user=user)
        except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
            user = None
            otp  = None
        if user is not None and default_token_generator.check_token(user,token) and otp is not None:
            request.session['pk_user']=user.pk
            if otp_submit ==str(otp):
                user.is_active = False
                user.is_emailverified = True
                user.save()
                user_delete.delete()
                return redirect('login')
            else:
                messages.error(request, "Opt does not match !")
                return redirect("validate-email",token)
    else:
        return render(request, "accounts/otp_verification.html")













# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        email = request.POST.get('username')
        password = request.POST.get('password')

        if Account.objects.filter(email__exact=email).exists():
            user =authenticate(username=email,password=password)
            print(user)
            if user:
                if user.is_emailverified:
                    login(request, user)
                    if user.is_active and user.is_authenticated and user.is_student and user.is_emailverified:
                        return redirect('dashboard_student')
                    elif user.is_active and user.is_authenticated and user.is_teacher and user.is_emailverified:
                        return redirect('dashboard_teacher')
                    elif user.is_active and user.is_authenticated and user.is_admin and user.is_emailverified:
                        return redirect('dashboard')
                else:
                    messages.error(request, "your account not verified by  please call teacher")
                    return redirect('login')
            else:
                messages.error(request, "incorrect password")
                return redirect('login')
        else:
            messages.error(request, "Please register first !")
            return redirect('login')
    form = LoginForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')



def forgotpassword_view(request):
    if request.method =="POST":
        email = request.POST.get("email")
        user=Account.objects.filter(email__exact=email).exists()
        if user:
            from sendemailverification.send_email import send_custom_mail
            validate_email_id = Account.objects.get(email=email)
            request.session["forgotpassword_user_id"] = validate_email_id.pk
            token   = default_token_generator.make_token(validate_email_id)
            otp = random.randint(100000, 500000)
            otp_create = OtpEmail.objects.create(otp=otp,user=validate_email_id)
            text    = "enter your otp in forgot email"
            otp_create.save()
            is_email_send=send_custom_mail(request,validate_email_id, otp, text)
            if is_email_send:
                return redirect("forgotpassword_validate",token)
        else:
            messages.error(request, "account does not exists please sign up first ")
    return render(request,'accounts/forgotpassword.html')


def forotpassword_validate(request,token):
    if request.method == "POST":
        otp_submit = request.POST.get('otp').strip(" ")
        print("your otp_submit otp is:",otp_submit)
        try:
            user = Account.objects.get(id=request.session["forgotpassword_user_id"])
            otp = OtpEmail.objects.filter(user=user).last()
        except(TypeError,OverflowError,ValueError,Account.DoesNotExist,OtpEmail.DoesNotExist,KeyError):
            user = None
            otp = None

        if otp_submit == str(otp) and default_token_generator.check_token(user,token):
            request.session["forgot_validate_user_id"] = user.pk
            return redirect("resetpassword")
        else:
            messages.error(request, "code does not match !")
            return redirect("forgotpassword_validate",token)

    return render(request, "accounts/otp_verification.html")



def resetpassword_view(request):
    if request.method == "POST":
        password = request.POST.get("password").strip(' ')
        confirm_password = request.POST.get('confirm_password').strip(' ')
        if password !=confirm_password:
            messages.error(request, "both passwords does not match !")
            return redirect("resetpassword")
        else:
            user_id = request.session['forgot_validate_user_id']
            user    = Account.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request, "your password has been changed successfully !")
            return redirect('login')
    return render(request, 'accounts/resetpassword.html')



'''
    from this line below code is for user profile
'''

@login_required(login_url='login')
def profile_view(request,pk):
    user = get_object_or_404(Account,pk=pk)
    if user.is_student:
        user_date = get_object_or_404(StudentAccount,user=user)
    else:
        user_date = None
    context={
        'user_date':user_date,
    }
    return render(request,'accounts/profile/my-profile.html',context)

@login_required(login_url='login')
def editprofile_view(request):
    return render(request, 'accounts/profile/edit-my-profile.html')