# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        authors = self.authors.all()
        temp = ''
        for a in authors:
            temp += a.first_name
            temp += ' '
            temp += a.last_name
            temp += ', '
        return 'Title:' , self.name , 'Author:', temp


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'Name:' , self.first_name , self.last_name , 'Books:', self.books
