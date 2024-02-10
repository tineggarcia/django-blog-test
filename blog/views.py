from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def my_blog(request):
    return HttpResponse(os.environ.get("SECRET_KEY"))