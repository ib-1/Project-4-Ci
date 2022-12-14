from django.shortcuts import render
from django.views.generic import ListView
from .models import room, book
# Create your views here.

class rooms(ListView):
    model = room

class books(ListView):
    model = book
