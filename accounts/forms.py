from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.db import transaction
from students.models import StudentAccount
from teachers.models import TeacherAccount




class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)

    username = UsernameField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'name':'email',
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'name':'password',
        }))