from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our projects!')

def project(request, pk):
    return HttpResponse('Here are our project! with {}'.format(pk))