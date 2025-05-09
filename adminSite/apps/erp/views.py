# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# Projects imports

# Python imports

# -------------------------------------------------
def myFirstView(request):
    return HttpResponse('hola')
