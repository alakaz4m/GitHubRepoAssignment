# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *

def index(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request, 'CreateUser/index.html', context)

def add(request):
    return render(request, 'CreateUser/add.html')

def new(request):
    User.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'],email=request.POST['email'])
    return redirect('/users')
