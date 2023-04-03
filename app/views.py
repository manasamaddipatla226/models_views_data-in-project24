from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insertion_topic(request):
    topic_name=input('enter topic name here: ')
    TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    return HttpResponse('topic inserted successfully')


def insertion_Webpage(request):
    tn=input('enter tn here: ')
    n=input('enter name here: ')
    url=input('enter url here: ')
    email=input('enter email: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url,email=email)[0]
    WO.save()
    return HttpResponse('webpage topic is inserted successfully')

def insertion_AccessRecord(request):
    topic_name=input('enter topic here: ')
    n=input('enter name here: ')
    url=input('enter url here: ')
    au=input('enter author name here: ')
    d=input('enter date here: ')
    TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=d)[0]
    AO.save()
    return HttpResponse('Access record data inserted successfully')


