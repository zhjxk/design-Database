from django.shortcuts import render

# Create your views here.
# request
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    return HttpResponse("ok")