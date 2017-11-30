# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        print request.session['logics']
    except KeyError as e:
        request.session['logics'] = 0
    return render(reqeust, 'addCourse/index.html')

def register(request):
    pass

def login(request):
    pass

def process(request, logics):
    pass
