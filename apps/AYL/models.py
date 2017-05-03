# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
import bcrypt, re, datetime

# Create your views here.

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Content(models.Model):
    user_table = models.ForeignKey(User, related_name='user_content')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user_table = models.ForeignKey(User, related_name='user_comment')
    content_table = models.ForeignKey(Content, related_name='content_comment')
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user_table = models.ForeignKey(User, related_name='user_like')
    content_table = models.ForeignKey(Content, related_name='content_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
