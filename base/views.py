from django.shortcuts import render
from .models import Room
#from django.http import HttpResponse


# Create your views here.

# rooms = [
#        {'id':1, 'name': 'Administrator'}, 
#        {'id':2, 'name': 'Management'}, 
#        {'id':3, 'name': 'Principal'}, 
#     ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk) #returns a single item 
    # room = None 
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room' : room}
    return render(request, 'base/room.html', context)

