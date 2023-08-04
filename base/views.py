from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

rooms = [
       {'id':1, 'name': 'Administrator'}, 
       {'id':2, 'name': 'Management'}, 
       {'id':3, 'name': 'Principal'}, 
    ]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')

