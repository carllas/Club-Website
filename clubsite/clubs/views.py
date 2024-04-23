from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def clubs(request):
    template = loader.get_template('clubs.html')
    return HttpResponse(template.render({}, request))