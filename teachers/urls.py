from django.urls import path
from teachers import views


urlpatterns = [
    path('teacher-register/',views.teacher_register_view,name="teacher_register"),
    path('dashboard/',views.dashboard,name="dashboard_teacher"),
]
