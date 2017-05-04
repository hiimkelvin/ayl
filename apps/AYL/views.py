# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import User, Content, Comment, Like
from .forms import DocumentForm
from django.contrib import messages

def index(request):
    documents = Content.objects.all()
    return render(request, 'AYL/index.html', { 'documents': documents })

def addcontentpage(request):
    return render(request, "AYL/addcontent.html")

def addcontent(request):
    try:
        context = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'document': request.FILES['document'],
            'userID': 1
        }
        Content.objects.addcontent(context)
        return redirect('/')
    except:
        messages.add_message(request, messages.ERROR, 'Upload a picture!')
        return redirect('/addcontentpage')
