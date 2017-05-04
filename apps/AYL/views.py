# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import User, Content, Comment, Like
from .forms import DocumentForm
from django.contrib import messages

def index(request):
    # Content.objects.all().delete()
    documents = Content.objects.all()
    return render(request, 'AYL/index.html', { 'documents': documents })

def addcontentpage(request):
    return render(request, "AYL/addcontent.html")

def addcontent(request):
    if 'user_id' not in request.session:
        messages.add_message(request, messages.ERROR, 'You have to login to upload pictures!')
        return redirect('/addcontentpage')
    else:
        try:
            context = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'document': request.FILES['document'],
            'userID': request.session['user_id']
            }
            Content.objects.addcontent(context)
            return redirect('/')
        except:
            messages.add_message(request, messages.ERROR, 'Upload a picture!')
            return redirect('/addcontentpage')
def index(request):
    context ={
        'all_content': Content.objects.all(),
    }
    return render(request, 'AYL/index.html', context)

def loginpage(request):
    return render(request, 'AYL/login.html')

def register(request):
	context = {
		'name': request.POST['name'],
        'username': request.POST['username'],
        'email': request.POST['email'],
		'password': request.POST['password'],
		'c_pass': request.POST['c_pass'],
	}
	reg_results = User.objects.reg(context)
	if reg_results['new'] != None:

		request.session['user_id'] = reg_results['new'].id
		request.session['user_name'] = reg_results['new'].name
		return redirect('/')
	else:
		for error_str in reg_results['error_list']:
			messages.add_message(request, messages.ERROR, error_str)
		return redirect('/login_registration')

def login(request):
    context = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    results = User.objects.log(context)
    if results['list_errors'] != None:
        for error in results['list_errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/login_registration')
    else:
        request.session['user_id'] = results['logged_user'].id
        request.session['user_name'] = results['logged_user'].name
        return redirect('/')

def content(request, content_id):
    context = {
        'content': Content.objects.get(id=content_id)
    }
    return render(request, "AYL/content.html", context)
