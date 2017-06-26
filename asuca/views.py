# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from psycopg2._psycopg import IntegrityError

from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request, username='',msg=''):
    return render(request, 'asuca/home.html', {'uname':username, 'msg':msg})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd']
            user = authenticate(username=uname, password=passwd)
            if user is not None:
                home(request=request,username=uname)
            else:
                form = LoginForm()
                form2 = SignupForm()
                return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2, "Error":"Username or Password is not correct!! Try again!!"})
        else:
            messages.error(request, "Error")
    else:
        form = LoginForm()
        form2 = SignupForm()
    return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2})

def signup(request):
    if request.method == 'POST':
        print "Hello"
        form = SignupForm(request.POST)
        if form.is_valid():
            print "Hello from validation!!!"
            uname = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd1']
            pnum = form.cleaned_data['pnum']
            try:
                user = User.objects.create_user(uname, email, passwd)
            except IntegrityError:
                msg = "User already exist!!"
                form = LoginForm()
                form2 = SignupForm()
                return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2,
                                                            "Error": msg})
            else:
                home(request= request,username=uname,msg="User created successfully!!")
        else:
            form = LoginForm()
            form2 = SignupForm()
            print "Error : "+str(form.errors)
        return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2, "Error": form.errors})
    else:
        form = LoginForm()
        form2 = SignupForm()
    return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2})





