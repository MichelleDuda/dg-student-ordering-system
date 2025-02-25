from django.shortcuts import render
from django.http import HttpResponse

# Views

def about(request):
   return render(request, 'about/about.html')

def sample_menu(request):
   return render(request, 'about/sample_menu.html')