# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
import bcrypt, re, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg(self, data):
    	errors = []

    	if len(data['name']) < 3:
    		errors.append("Name must be at least three characters long.")
    	if len(data['username']) < 3:
    		errors.append("Username must be at least three characters long.")
		if data['email'] == '':
			errors.append("Email may not be blank")
		if not EMAIL_REGEX.match(data['email']):
			errors.append("Please enter a valid email address.")
		try:
			User.objects.get(email=data['email'])
			errors.append("Email is already registered")
		except:
			pass
    	if len(data['password']) < 8:
    		errors.append("Password must be at least eight characters long.")
    	if data['password'] != data['c_pass']:
    		errors.append("Password does not match.")

    	if len(errors) == 0:
    		data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    		new_user = User.objects.create(name=data['name'], username=data['username'], email=data['email'], pw=data['password'])
    		return {
    			'new': new_user,
    			'error_list': None
    		}
    	else:
    		return {
    			'new': None,
    			'error_list': errors
    		}

    def log(self, data):
        errors = []
        try:
        	user = User.objects.get(email=data['email'])
        	if bcrypt.hashpw(data['password'].encode('utf-8'), user.pw.encode('utf-8')) != user.pw.encode('utf-8'):
        		errors.append("Incorrect password.")
        except:
        	errors.append("Email not registered.")
        if len(errors) == 0:
        	return {
        		'logged_user': user,
        		'list_errors': None
        	}
        else:
            return {
                'logged_user': None,
                'list_errors': errors
            }

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class ContentManager(models.Manager):
    def addcontent(self, data):
        title = data['title']
        description = data['description']
        document = data['document']
        userID = data['userID']
        errors = []

        if title == '':
            errors.append('Give your picture a title!')
        if description == '':
            errors.append('You need a description!')

        if len(errors) == 0:
            user = User.objects.get(id=userID)
            newimage = Content(user_table=user, title=title, description=description, document=document)
            newimage.save()
        else:
            pass

class Content(models.Model):
    user_table = models.ForeignKey(User, related_name='user_content')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContentManager()

class CommentManager(models.Manager):
    def add_comment(self, data):
        userID = data['userID']
        contentID = data['contentID']
        comments = data['comments']
        errors = []

        if data['comments'] == '':
            errors.append('Comments may not be empty!')

        if len(errors) == 0:
            user = User.objects.get(id=userID)
            content = Content.objects.get(id=contentID)
            Comment.objects.create(user_table=user, content_table=content, comment=comments)
            print 'added user'
        else:
            pass

class Comment(models.Model):
    user_table = models.ForeignKey(User, related_name='user_comment')
    content_table = models.ForeignKey(Content, related_name='content_comment')
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

class Like(models.Model):
    user_table = models.ForeignKey(User, related_name='user_like')
    content_table = models.ForeignKey(Content, related_name='content_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
