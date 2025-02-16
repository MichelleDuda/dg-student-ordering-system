from django.shortcuts import render
from django.http import HttpResponse

# Views

def index(request):
    return HttpResponse("You did it! Welcome to DG Student Ordering System")