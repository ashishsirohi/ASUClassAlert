# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import IntegrityError
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import LoginForm, SignupForm, SearchForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from asuca.models import userinfo, courses
from searchcourse import check_status

import json

# Create your views here.
def home(request):
    username = request.session.get('username')
    msg = request.session.get('msg')
    form = SearchForm()
    return render(request, 'asuca/home.html', {'uname':username, 'msg':msg, 'form' : form})

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd']
            user = authenticate(request, username=uname, password=passwd)
            if user is not None:
                login(request, user)
                msg = "true"
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

            userinfo.objects.create(username = uname, emailid = email, phone = pnum, courses=[])
            user = authenticate(request, username=uname, password=passwd1)
            login(request, user)
            msg = "true"
            request.session['username'] = uname
            request.session['msg'] = msg
            return HttpResponseRedirect(reverse('home'))

    else:
        form = SignupForm()
    return render(request, 'asuca/signup.html', {'signup_form': form})

def logoutUser(request):
    logout(request)
    msg = "false"
    request.session['msg'] = msg
    return HttpResponseRedirect(reverse('home'))

def searchcourse(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cid = form.cleaned_data['courseid']
            sub = form.cleaned_data['subject']
            sub_id = form.cleaned_data['subj_num']
            term = '2177'
            status = check_status(cid, term)
            course_name = str(sub)+str(sub_id)
            #print "Hello"
            print status
            if len(status)>0:
                request.session['prof'] = status[0]
                request.session['course'] = status[1]
                request.session['seats'] = status[2]
                request.session['cid'] = cid
                request.session['av'] = 1
            else:
                request.session['cid'] = cid
                request.session['av'] = 0
                request.session['course'] = course_name


    return HttpResponseRedirect(reverse('searchresult'))

def searchResult(request):
    return render(request, 'asuca/result.html', {'av': request.session.get('av'), 'cid': request.session.get('cid'),'name': request.session.get('username'), 'course': request.session.get('course'), 'prof': request.session.get('prof'), 'seats': request.session.get('seats')})

def notifyUser(request):
    cid =request.session.get('cid')
    uname = request.session.get('username')
    record = userinfo.objects.get(username=uname)
    print cid
    print record.courses
    if int(cid) in record.courses:
        print "Already have course in notification list"
    else:
        print "Added"
        record.courses.append(cid)
        record.save()

    record = courses.objects.filter(courseid=cid).exists()
    if(record):
        record = courses.objects.get(courseid=cid)
        if uname in record.users:
            print "Already in the notification list"
        else:
            print "Hello"
            record.users.append(uname)
            record.save()
    else:
        courses.objects.create(courseid=cid, term=2177, users=[uname])

    return HttpResponseRedirect(reverse('myCourses'))

def myCourses(request):
    uname = request.session.get('username')
    record = userinfo.objects.get(username=uname)
    mylist = record.courses
    return render(request, 'asuca/mycourses.html', {'mylist': mylist})

def removeNotification(request):
    if request.method == 'GET':
        cid = request.GET.get('id', '')
        uname = request.session.get('username')
        print cid
        print uname
    return HttpResponseRedirect(reverse('myCourses'))





