from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,HttpResponse
from django.contrib import messages 
from django.conf import settings
from django.db.models import Q
from dashboard.models import Routine,Faulty,Subject
from dashboard.forms import AddRoutineForm,AddSubjectForm,AddFacultyForm,Add_RoutineForm


from django.contrib.auth.decorators import login_required
from dashboard.decorators import admin_required

from accounts.models import Account

# Create your views here.



@login_required(login_url='login')
@admin_required
def student_admit_view(request,pk):
    student = get_object_or_404(Account,pk=pk)
    student.is_active = True
    student.save()
    return redirect(request.session['url_student'])




@login_required(login_url='login')
@admin_required
def see_student_request(request):
    request.session['url_student'] = request.get_full_path()
    all_student =  Account.objects.filter(is_active=False)
    context={
        "all_student":all_student,
    }
    return render(request, 'dashboard/request_student.html',context)


@login_required(login_url='login')
@admin_required
def see_teacher_request(request):
    request.session['url_teacher'] = request.get_full_path()
    all_teacher =  Account.objects.filter(is_active=False)
    context={
        "all_teacher":all_teacher,
    }
    return render(request, 'dashboard/request_teacher.html',context)



@login_required(login_url='login')
@admin_required
def teacher_admit_view(request,pk):
    student = get_object_or_404(Account,pk=pk)
    student.is_active = True
    student.save()
    return redirect(request.session['url_teacher'])




@login_required(login_url='login')
@admin_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')



@login_required(login_url='login')
@admin_required
def attendanceslist_view(request):
    return render(request, 'dashboard/attendances-list.html')



@login_required(login_url='login')
@admin_required
def attendancesreport_view(request):
    return render(request,'dashboard/attendances-report-blank.html')





'''
    below this completed code !!!!
'''

@login_required(login_url='login')
@admin_required
def routine_management_view(request):
    request.session['url_routine'] =  request.get_full_path()

    if request.GET.get('faulty') and request.GET.get('semister') and request.GET.get('day'):
        faculty = request.GET.get('faulty')
        semister= request.GET.get('semister')
        day     = request.GET.get('day')
        # print("faculty is =====>>>",facult
        Routines = Routine.objects.filter(faulty__faulty=request.GET['faulty']) & Routine.objects.filter(semister=request.GET['semister']) & Routine.objects.filter(day=request.GET['day'])
    else:
        Routines = None
        day      = None
        semister = None
        faculty  = None

    faulty   = Faulty.objects.all()
    context = {
        'routine':Routines,
        'faulties':faulty,
        'day':day,
        'semister':semister,
        'faculty':faculty,
    }
    return render(request,'dashboard/routine-admin.html',context)


'''
    this is add form view 
'''

@login_required(login_url='login')
@admin_required
def add_routine_view(request):
    faulties = Faulty.objects.all()
    request.session['faculty'] = request.GET.get('faulty')
    request.session['semister'] = request.GET.get('semister')

    if request.GET.get('faulty') and request.GET.get('semister'):
        semister = request.GET.get('semister')
        faculty  = request.GET.get('faulty')
        day      = request.GET.get('day')
        request.session['url'] = request.get_full_path()
        routine = Routine.objects.filter(Q(faulty__faulty__exact=faculty) & Q(semister__exact=semister) & Q(day__exact=day))
        form_show = request.GET.get('value')
    else:
        routine = None
        form_show = None
        semister = None
        faculty  = None
        day     = None

    if request.method == "POST":
        form = Add_RoutineForm(request.POST or None,request=request)
        if form.is_valid():
            form.save()
            clean_data = form.cleaned_data
            semister   = clean_data.get('semister')
            faculty    = clean_data.get('faulty')
            subject    =clean_data.get('subject')
            messages.success(request, f'Routine has been added for {semister} of {faculty} of {subject}')
            return redirect(request.session['url'])
        else:
            messages.error(request, 'form is invalid please fill up again !')
            return redirect('add_routine')
    else:
        form = Add_RoutineForm(request=request)
    context = {
        'form_show':form_show,
        'form':form,
        'faulties':faulties,
        'routine':routine,
        'semister':semister,
        'faculty':faculty,
        'day':day,
    }
    return render(request, 'dashboard/add-routine.html',context)





@login_required(login_url='login')
@admin_required
def editroutine_view(request,pk,semister,faculty):
    # routine = get_object_or_404(Routine,pk=pk)
    routine = Routine.objects.get(pk=pk)
    form = Add_RoutineForm(request.POST or None,instance=routine,request=request)
    if form.is_valid():
        form.save()
        messages.success(request, 'Routine has been updated Successfully !')
        return redirect(request.session['url_routine'])
    else:
        print("form.is_valid() value ==>>:",form.is_valid())


    context = {
        'form':form,
        'edit_form':True,
    }
    return render(request,'dashboard/editroutine.html',context)


@login_required(login_url='login')
@admin_required
def routine_delete_view(request,pk):
    routine = Routine.objects.get(pk=pk)
    routine.delete()
    messages.success(request, f'Routine deleted of {routine.faulty} of semister  {routine.semister}')
    return redirect(request.session['url_routine'])
 




@login_required(login_url='login')
@admin_required
def homework_view(request):
    return render(request, 'dashboard/homework.html')






@login_required(login_url='login')
@admin_required
def add_subject_view(request):
    if request.POST.get('save_add') == "Save And Add":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            clean_data = form.cleaned_data
            subject     = clean_data.get('subject')
            faculty  = clean_data.get('faulty')
            semister    = clean_data.get('semister')
            messages.success(request,f"{subject} Subject of {faculty}  semister of {semister} has been added successfully !")
            return redirect('add_subject')


    elif request.method == "POST":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            clean_data = form.cleaned_data
            subject     = clean_data.get('subject')
            faculty  = clean_data.get('faulty')
            semister    = clean_data.get('semister')
            messages.success(request,f"{subject} Subject of {faculty}  semister of {semister} has been added successfully !")
            return redirect('view_all_subject')
    else:
        form = AddSubjectForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/add-subject.html',context)







@login_required(login_url='login')
@admin_required
def view_all_subject_view(request):
    request.session['url_subject'] = request.get_full_path()
    faulty = request.GET.get('faulty')
    semister = request.GET.get('semister')
    if faulty is not None and semister == "all":
        subjects = Subject.objects.filter(faulty__faulty=faulty).order_by('semister')
    elif faulty is not None and semister is not None:
        subjects = Subject.objects.filter(faulty__faulty=faulty) & Subject.objects.filter(semister=semister)
    else:
        subjects = None
    faulties = Faulty.objects.all()
    context = {
        'faulties':faulties,
        'subjects':subjects,
    }
    return render(request,'dashboard/view-all-subjects.html',context)




@login_required(login_url='login')
@admin_required
def subject_edit_view(request,pk):
    subject = get_object_or_404(Subject,pk=pk)
    form = AddSubjectForm(request.POST or None,instance=subject)
    if form.is_valid():
        clean_data = form.cleaned_data
        subject = clean_data.get('subject')
        faulty  = clean_data.get('faulty')
        year_or_semister = clean_data.get('semister')
        form.save()
        messages.success(request, f'subject {subject} of {year_or_semister} faculty {faulty} has been edited successfully !')
        return redirect(request.session['url_subject'])

    context = {
        'form':form,
    }
    return render(request,'dashboard/edit-subject.html',context)


@login_required(login_url='login')
@admin_required
def delete_subject_view(request,pk):
    subject = get_object_or_404(Subject,pk=pk)
    messages.success(request, f"{subject.subject} of {subject.semister}  of {subject.faulty} has been deleted")
    subject.delete()
    return redirect(request.session['url_subject'])



@login_required(login_url='login')
@admin_required
def add_faculty_view(request):
    if request.method == "POST":
        form = AddFacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'faculty has been added successfully !')
            return redirect('view_all_faculty')
    else:
        form = AddFacultyForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add-faculty.html',context)

@login_required(login_url='login')
@admin_required
def view_all_faculty_view(request):
    request.session['url'] = request.get_full_path()
    faculty = Faulty.objects.all()
    context = {
        'faculty':faculty,
    }
    return render(request, 'dashboard/view-all-faculty.html',context)





@login_required(login_url='login')
@admin_required
def edit_faculty_view(request,pk):
    faculty = get_object_or_404(Faulty,pk=pk)
    form = AddFacultyForm(request.POST or None,instance=faculty)
    if form.is_valid():
        form.save()
        messages.success(request, 'updated faculty !!')
        return redirect('view_all_faculty')
    context = {
        'form':form,
    }
    return render(request, 'dashboard/edit-faculty.html',context)



@login_required(login_url='login')
@admin_required
def delete_faculty(request,pk):
    faculty = get_object_or_404(Faulty,pk=pk)
    messages.success(request, f"{faculty.faulty} faculty has been deleted")
    faculty.delete()
    return redirect('view_all_faculty')





