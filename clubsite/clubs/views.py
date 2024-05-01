from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Club

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def clubs(request):
    myclubs = Club.objects.all().values()
    template = loader.get_template('clubs.html')
    context = {
        "myclubs": myclubs
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  myclub = Club.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myclub': myclub,
  }
  return HttpResponse(template.render(context, request))