# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "unique_id": get_random_string(length=14)
    }
    try:
        request.session["my_session"] += 1
    except:
        request.session["my_session"] = 1

    return render(request, 'wordGenerator/index.html', context)
