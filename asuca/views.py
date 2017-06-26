# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import IntegrityError
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from asuca.models import userinfo

# Create your views here.
def home(request):
    username = request.session.get('username')
    msg = request.session.get('msg')
    print username
    return render(request, 'asuca/home.html', {'uname':username, 'msg':msg})

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd']
            user = authenticate(request, username=uname, password=passwd)
            if user is not None:
                login(request, user)
                msg = "Logged in successfully!!"
                request.session['username'] = uname
                request.session['msg'] = msg
                return HttpResponseRedirect(reverse('home'))

            else:
                form = LoginForm()
                form2 = SignupForm()
                return render(request, 'asuca/login.html', {'login_form': form, 'signup_form': form2, "Error":"Username or Password is not correct!! Try again!!"})
        else:
            messages.error(request, "Error")
    else:
        form = LoginForm()
    return render(request, 'asuca/login.html', {'login_form': form})

def signupUser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            passwd1 = form.cleaned_data['passwd1']
            passwd2 = form.cleaned_data['passwd2']
            pnum = form.cleaned_data['pnum']

            if passwd1 != passwd2:
                msg = "Both passwords didn't match"
                return render(request, 'asuca/signup.html', {'signup_form': form, "Error":msg})
            try:
                User.objects.create_user(uname, email, passwd1)
            except IntegrityError:
                msg = "User already exist!!"
                return render(request, 'asuca/signup.html', {'signup_form': form, "Error": msg})

            userinfo.objects.create(username = uname, emailid = email, phone = pnum)
            user = authenticate(request, username=uname, password=passwd1)
            login(request, user)
            msg = "User created and logged in successfully!!"
            request.session['username'] = uname
            request.session['msg'] = msg
            return HttpResponseRedirect(reverse('home'))

    else:
        form = SignupForm()
    return render(request, 'asuca/signup.html', {'signup_form': form})





