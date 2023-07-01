from django.shortcuts import render
<<<<<<< HEAD
# Create your views here.

#template inheritance

def home(request):
    return render(request, 'index.html')
=======
#from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')
>>>>>>> 3847e08240dd8a04a43a9db3faf6999333926c55

def room(request):
    return render(request, 'room.html')

