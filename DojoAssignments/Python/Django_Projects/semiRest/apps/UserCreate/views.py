# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
            'users':User.objects.all()
    }
    return render(request, 'UserCreate/index.html', context)

def addUser(request):
    return render(request, 'UserCreate/new.html')

def process(request):
    User.objects.create(name=request.POST['name'], email=request.POST['email'])
    return redirect('/')

def show(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id = user_id)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
        return redirect('/%s' % str(user_id))
    context = {
            'user':User.objects.get(id=user_id)
    }
    return render(request, 'UserCreate/show.html', context)

def edit(request, user_id):
    context = {
            'user':User.objects.get(id=user_id)
    }
    return render(request, 'UserCreate/edit.html', context)

def destroy(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    return redirect('/')
