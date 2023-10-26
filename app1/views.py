from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def htmlexample(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def htmlexample1(request) :
    template = loader.get_template('index1.html')
    return HttpResponse(template.render())
def htmlexample2(request) :
    template = loader.get_template('index2.html')
    return HttpResponse(template.render())
def htmlexample3(request) :
    template = loader.get_template('index3.html')
    return HttpResponse(template.render())
def htmlexample4(request) :
    template = loader.get_template('index4.html')
    return HttpResponse(template.render())