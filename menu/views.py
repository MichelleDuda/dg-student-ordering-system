from django.shortcuts import render
from django.http import HttpResponse

# Views

def index(request):
   return render(request, 'menu/index.html')