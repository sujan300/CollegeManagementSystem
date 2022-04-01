from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from teachers.models import TeacherAccount






'''
    this is for teacher registration form
'''

class TeacherCreactionForm(UserCreationForm):
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
        label = "Password",
        widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password',
            'class':'form-control',
        }))


    password2 = forms.CharField(
        label = "Password Confirm",
        widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password(again)',
        'class':'form-control',
    }))


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
        user.is_teacher = True
        user.save()
        teacher = TeacherAccount.objects.create(user=user)
        teacher.gender = self.cleaned_data.get('gender')
        teacher.save()
        return user