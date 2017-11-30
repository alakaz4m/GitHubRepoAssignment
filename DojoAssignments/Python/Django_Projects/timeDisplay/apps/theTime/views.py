# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime

def index(request):
    context = {
    "date": strftime("%b %d, 20%y", gmtime()),
    "time": strftime( "%I:%M %p", localtime())
    }
    return render(request, 'theTime/index.html', context)
