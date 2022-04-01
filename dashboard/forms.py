
from django import forms
from django.forms import ModelChoiceField
from dashboard.models import Routine,Subject,Faulty
from django.db.models import Q
from django.db.models import CharField
from django.db.models.functions import Lower
from django.forms import modelformset_factory



class AddRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['subject','semister','day','time','faulty']

        
    query_subject = None
    subject = forms.ModelChoiceField(label='Share with groups', queryset=query_subject)

    def __init__(self,*args,**kwargs):
        instance = kwargs.pop('instance', None)
        super(AddRoutineForm, self).__init__(*args,**kwargs)
        # self.query_subject = Subject.objects.filter(faulty__faulty=instance.faulty) & Subject.objects.filter(semister=instance.semister)
        self.fields['subject'].queryset = instance
        # self.fields['faulty'].queryset  = Faulty.objects.filter(faulty=faculty)







class Add_RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = "__all__"

    def __init__(self,*args,request=None,**kwargs):
        super(Add_RoutineForm,self).__init__(*args,**kwargs)

        semister = request.session['semister']
        faculty  = request.session['faculty']

        if faculty is not None and semister is not None:
            self.fields['subject'].queryset =  Subject.objects.filter(faulty__faulty=faculty) & Subject.objects.filter(semister=semister)
            self.fields['faulty'].queryset =  Faulty.objects.filter(faulty=faculty)

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model  = Subject
        fields = "__all__"




class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faulty
        fields= "__all__"

