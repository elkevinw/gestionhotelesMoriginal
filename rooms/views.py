from django.shortcuts import render

# Create your views here.

from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def payment(request):
    return render(request, 'payment.html')

def pricing(request):
    return render(request, 'pricing.html')

def register(request):
    return render(request, 'register.html')