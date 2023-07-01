from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('room/', views.room, name = "room")

]
=======
from . import views 

urlpatterns = [
    path('', views.home, name = "home"),
    path('room/', views.room, name = "home"),
]
>>>>>>> 3847e08240dd8a04a43a9db3faf6999333926c55
