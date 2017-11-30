# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, postData):
        
        pass


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name="posted_by")
    favorited_by = models.ManyToManyField(User, related_name="favslist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
