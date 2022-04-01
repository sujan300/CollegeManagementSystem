from  django.urls import path
from students import views


urlpatterns = [
    # this is only for student register 
    path('student-register-view/',views.student_register_view,name="student_register"),

    # student dashboard
    path('dashboard/',views.dashboard,name="dashboard_student"),

    # routine for student 
    path('student-routine/',views.student_routine_view,name="student_routine"),

]
