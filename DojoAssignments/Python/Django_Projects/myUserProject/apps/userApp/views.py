# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    user = User.objects.all()
    context = {
        'all_users': user
    }
    return render(request,'userApp/index.html', context)

def new(request):
    return render(request, 'userApp/new.html')

def add(request):
    User.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'],email=request.POST['email'])
    return redirect('/users')

def show(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=int(user_id))
        print(request.POST)
        user.first_name = request.POST["firstname"]
        user.last_name = request.POST["lastname"]
        user.email = request.POST["email"]
        user.save()
        return redirect("/users/{}".format(user_id))
    else:
        user = User.objects.get(id=int(user_id))
        context = {
            'user': user
            }
        return render(request, 'userApp/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id=int(user_id))
    context = {
        'user': user
    }
    return render(request, 'userApp/edit.html', context)

def process(request, user_id):
    user = User.objects.get(id=int(user_id))
    return redirect("/users")

def destroy(request, user_id):
    user = User.objects.get(id=int(user_id)).delete()
    return redirect("/users")
