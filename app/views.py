from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

def topic_name(request):
    tn=input('enter topic name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Data inserted Successfully')


def webpage(request):
    tn=input('Enter topic name: ')
    n=input('Enter name : ')
    url=input('Enter URL : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    wo.save()
    return HttpResponse('Data inserted Successfully')
    

def access_record(request):
    tn=input('enter topic name :')
    n=input('enter name:')
    url=input('Enter URL : ')
    date=input('enter date : ')
    author=input('enter author:')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    wo.save()
    Ao=Accessrecord.objects.get_or_create(name=wo,date=date,author=author)[0]
    Ao.save()
    return HttpResponse('Data inserted Successfully')