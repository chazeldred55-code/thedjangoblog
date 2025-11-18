# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return HttpResponse("Hello, Django! Your blog is working.")
