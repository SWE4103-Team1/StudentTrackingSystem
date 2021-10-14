from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('homepage/', views.homePage, name='homepage'),
    path('student_data/', views.student_data, name = 'student_data'),
    path('course_data/', views.course_data, name = 'course_data'),
    path('enrolment_data/', views.enrolment_data, name = 'enrolment_data')
]