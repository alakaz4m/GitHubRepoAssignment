# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
        first_name = CharField(maxlength=255)
        last_name = CharField(maxlength=255)
        email_address = CharField(maxlength=255)
        age = DecimalField(max_digits=3,decimal_places=0)
        created_at = DateTimeField(auto_now_add=True)
        updated_at = DateTimeField(auto_now=True)
