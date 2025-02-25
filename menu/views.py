from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Views

def index(request):
   return render(request, 'menu/index.html')

@login_required  # Ensures users can only access if logged in
def dashboard(request):
    return render(request, 'menu/student_dashboard.html', {'user': request.user})