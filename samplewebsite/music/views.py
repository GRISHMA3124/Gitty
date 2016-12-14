from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Albums

def index(request):
    all_abums=Albums.object.all()
    template=loader.get_template('')
    return HttpResponse('')
# Create your views here.

def detail(request,album_id):
    return HttpResponse("<h1>this is my album page</h1>")