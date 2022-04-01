from django.urls import path
from dashboard import views


urlpatterns = [
    # dashboard
    path('dashboard/',views.dashboard_view,name='dashboard'),

    # attendances
    path('attendances-list/',views.attendanceslist_view,name="attendances_list"),
    path('attendances-report-bank/',views.attendancesreport_view,name="attendances_report_bank"),

    # routine
    path('routine/',views.routine_management_view,name="routine"),
    path('add-routine/',views.add_routine_view,name='add_routine'),
    path('routine-delete/<int:pk>/',views.routine_delete_view,name='routine_delete'),
    path('edit-routine/<int:pk>/<semister>/<faculty>/',views.editroutine_view,name="editroutine"),

    # homework
    path('homework/',views.homework_view,name="homework"),

    # subject
    path('add-subject/',views.add_subject_view,name='add_subject'),
    path('view-all-subjects/',views.view_all_subject_view,name="view_all_subject"),
    path('edit-subject/<int:pk>/',views.subject_edit_view,name="edit_subject"),
    path('delete-subject/<int:pk>/',views.delete_subject_view,name='delete_subject'),

    # faculty
    path('add-faculty/',views.add_faculty_view,name="add_faculty"),
    path('view-all-faculty/',views.view_all_faculty_view,name="view_all_faculty"),
    path('delete-faculty/<int:pk>/',views.delete_faculty,name="delete_faculty"),
    path('edit-faculty/<int:pk>/',views.edit_faculty_view,name='edit_faculty'),



    # student request for adminsion 
    path('request-student/',views.see_student_request,name="student_request"),
    path('admit-student/<int:pk>/',views.student_admit_view,name="student_admit"),

    # teacher request for admission 
    path('request-teacher/',views.see_teacher_request,name="teacher_request"),
    path('admit-teacher/<int:pk>/',views.teacher_admit_view,name="teacher_admit"),

]


