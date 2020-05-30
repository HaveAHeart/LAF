from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def newItem(request):
    return HttpResponse("Hello, world. NEWITEM will be here")
