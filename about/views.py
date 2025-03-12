from django.shortcuts import render
from django.http import HttpResponse
from .menu_data import menu_data

# Views


def about(request):
    """Render and return the About page."""
    return render(request, 'about/about.html')


def sample_menu(request):
    """Render and return the Sample Menu page with menu data."""
    return render(request, 'about/sample_menu.html', {"menu_data": menu_data})
