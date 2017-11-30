# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'QuoteApp/index.html')

def register(request):
    result = User.objects.validate(request.POST)
    return redirect('/')

def quotes(request):
    pass
def login(request):
    pass
