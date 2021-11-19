"""StudentTrackingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from StudentTrackingSystemApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirectLogin),
    path('login/', views.loginPage, name ='loginPage'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registerPage, name ='registerPage'),
    path('settings/', views.settings, name='settings'),
    path('student_data/', views.student_data, name ='student_data'),
    path('course_data/', views.course_data, name ='course_data'),
    path('enrolment_data/', views.enrolment_data, name ='enrolment_data'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('api/student_data/', views.get_student_data_api, name ='get_student_data_api'),
    path('api/counts_semester/<path:semester>/', views.get_counts_by_semester, name ='get_counts_by_semester_api'),
    path('api/counts_cohort/<str:cohort>/', views.get_counts_by_cohort, name ='get_counts_by_cohort_api'),
    path('api/count_parameters', views.get_count_parameters_api, name ='get_count_parameters_api'),
    path('get_transcript/<int:student_num>', views.get_transcript, name = 'get_transcript'),
]
