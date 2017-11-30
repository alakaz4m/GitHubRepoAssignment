# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'Survey/index.html')

def results(request):
    try:
        request.session['num'] += 1
    except:
        request.session['num'] = 1

    context = {
        "name":request.POST['name'],
        "location":request.POST['location'],
        "language":request.POST['favlanguage'],
        "comment":request.POST['comment'],
        "attemps":request.session['num'],
    }
    return render(request, 'Survey/results.html', context)
