from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('Hello Django and Docker')

def page2(request):
    return render(request, 'page2.html')
