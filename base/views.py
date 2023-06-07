from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#template inheritance

def home(request):
    return render(request, 'index.html')

def room(request):
    return render(request, 'room.html')

