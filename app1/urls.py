from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.Registerpage,name="registerpage"),
    path("loginpage/",views.Loginpage,name='loginpage'),
    path("registerpage/",views.RegisterUser,name="ragisterer"),
    path("login-page/",views.loginuser,name="loginuser"),
]