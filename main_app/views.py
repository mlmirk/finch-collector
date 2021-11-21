from django.shortcuts import render
from django.http import HttpResponse
from django.utils.regex_helper import flatten_result
# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello finchees</h1>')

def about(request):
  return HttpResponse('<h1>About Finches</ht>')