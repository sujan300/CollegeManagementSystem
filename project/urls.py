




from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('students/',include('students.urls')),
    path('teachers/',include('teachers.urls')),
    path('test-view/',views.test_view,name="test-view")
]
