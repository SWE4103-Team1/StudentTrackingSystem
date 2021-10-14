from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('homepage/', views.homePage, name='homepage'),
     path('view_data/', views.view_data, name = 'view_data')
]
