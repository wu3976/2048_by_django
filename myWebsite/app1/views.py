from django.shortcuts import render
from .forms import LoginForm, SignupForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import UserDataModel, SessionModel
from .utils import *
from django.contrib import sessions


# Create your views here.
def mainPage(request):
    return render(request, 'index.html')


def login(request):
    if 'username' in request.COOKIES.keys():
        username = request.COOKIES['username']
        access_key = request.COOKIES['access_key']
        record = SessionModel.objects.filter(user_name=username)
        if len(record) == 1 and record[0].access_key == access_key:
            return render(request, "already_logged_in.html", {
                'name': request.COOKIES['username']
            })
        else:
            return render(request, "message.html", {
                "msg_title": "Error",
                "msg_body": "Unexpected Error!"
            })

    login_form = LoginForm()

    return render(request, "login.html", {'form': login_form})


def login_check(request):
    login_form = LoginForm(request.POST)
    print("here")
    if login_form.is_valid():
        user_name = login_form.cleaned_data['userName']
        obj = UserDataModel.objects.filter(user_name=user_name)
        if len(obj) == 0:
            return redirect("/message/fail/Login_fail")
        else:
            if obj[0].password == login_form.cleaned_data['passWord']:
                response = redirect("/message/success/Login_success")
                # set cookie-session
                response.set_cookie("username", obj[0].user_name)
                access_key = generateAccessKey(32, db_compatible=True)
                response.set_cookie("access_key", access_key)
                # save the cookie session into model
                session = SessionModel(user_name=obj[0].user_name, access_key=access_key)
                session.save()

                return response
            else:
                return redirect("/message/fail/Password_incorrect")

    else:
        return redirect("/message/invalid/form")


def message(request, title, body):
    text = parse_URL_param(body)

    context = {
        "msg_title": title,
        "msg_body": text
    }

    return render(request, "message.html", context)


def signup(request):
    signupForm = SignupForm()

    context = {
        'form': signupForm
    }

    return render(request, "signup.html", context)


def signup_check(request):
    signupForm = SignupForm(request.POST)
    if signupForm.is_valid():
        newLine = UserDataModel(user_name=signupForm.cleaned_data['userName'],
                                password=signupForm.cleaned_data['passWord'],
                                email=signupForm.cleaned_data['email'], game_counts=0, personal_best=0)
        newLine.save()
        return redirect("/message/success/Signup_success")


def logout(request):
    context = {
        'message': "You have logged out!"
    }
    res = render(request, "logout.html", context)
    if 'username' in request.COOKIES.keys():
        username = request.COOKIES['username']
        res.delete_cookie('username')
        access_key = request.COOKIES['access_key']
        res.delete_cookie('access_key')
        row = SessionModel.objects.filter(user_name=username)
        if row[0].access_key == access_key:
            row.delete()
            return res
        else:
            return render(request, "logout.html", {
                "message": "Unexpected error"
            })
    else:
        return render(request, "logout.html", {
            "message": "You have already logged out!"
        })
