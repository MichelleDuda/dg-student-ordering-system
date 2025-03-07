from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Views

def index(request):
   return render(request, 'menu/index.html')

@login_required  # Ensures users can only access if logged in
def dashboard(request):
    return render(request, 'menu/student_dashboard.html', {'user': request.user})

def handler404(request, exception):
    return render(request, "errors/404.html", status=404)

def handler500(request):
    return render(request, "errors/500.html", status=500)