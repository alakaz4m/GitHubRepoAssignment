# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):






class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Course(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Desc(models.Model):
    description = models.OneToOneField(Course)

class Comment(models.Model):
    comments = models.CharField(max_length = 255)
    posted_by = models.ForeignKey(User, related_name = 'user_posted')
    posted_at = models.DateTimeField(auto_now_add = True)
