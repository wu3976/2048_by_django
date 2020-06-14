from django.contrib import admin
from django.urls import path
from .views import mainPage, login, login_check, message, signup, signup_check, logout
urlpatterns = [
    path("", mainPage, name="mainPage"),
    path("login/", login, name="login"),
    path("login_check/", login_check, name="login_check"),
    path("message/<str:title>/<str:body>", message, name="message"),
    path("signup/", signup, name="signup"),
    path("signup_check/", signup_check, name="signup_check"),
    path("logout/", logout, name="logout")
]
