from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    # path('student-register/',views.student_register_view,name="student_register"),
    # path('teacher-register/',views.teacher_register_view,name="teacher_register"),
    path('forgotpassword/',views.forgotpassword_view,name='forgotpassword'),
    path('resetpassword/',views.resetpassword_view,name='resetpassword'),
    #dont forget token ==>> here line 12
    path('profile/<int:pk>/',views.profile_view, name='profile'),
    path('profile-edit/', views.editprofile_view, name='profile_edit'),

    # ''' validate any types of user'''
    path('validate-email/<token>/',views.validate_email,name="validate-email"),

    # for forgotpassword validate 
    path("forgotpassword-validate/<token>/",views.forotpassword_validate,name="forgotpassword_validate"),
]