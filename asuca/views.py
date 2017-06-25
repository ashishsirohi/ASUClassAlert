# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'asuca/home.html')

def login(request):
    return render(request, 'asuca/login.html')

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        pass