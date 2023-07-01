from django.shortcuts import render
# Create your views here.

#template inheritance

def home(request):
    return render(request, 'index.html')

def room(request):
    return render(request, 'room.html')

