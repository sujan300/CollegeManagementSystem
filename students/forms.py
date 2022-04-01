from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from students.models import StudentAccount


import datetime

'''
    this is teacher registration form 
'''

class StudentCreationForm(UserCreationForm):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )

    gender = forms.ChoiceField(
            choices=GENDER,
            widget=forms.Select(attrs={
                'class':'form-control'
        }))


    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password',
            'class':'form-control',
        }))


    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password(again)',
        'class':'form-control',
    }))


    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder':'yyy/mmm/ddd',
            'class':'form-control',
            'type':'date'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['first_name','last_name','phone_number','email']


        widgets     = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
        }


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.is_active  = False
        user.save()
        student = StudentAccount.objects.create(user=user)
        student.gender = self.cleaned_data.get('gender')
        student.date_of_birth = self.cleaned_data.get('date_of_birth')
        student.semister =1
        # student.date_joined = str(datetime.datetime.now().year)
        # print("the date is : ",datetime.datetime.now().year)
        # print(type(datetime.datetime.now().year))
        student.save()
        return user

