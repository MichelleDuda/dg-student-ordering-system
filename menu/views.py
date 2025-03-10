from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserChangeForm

# Views


# Homepage View
def index(request):
    return render(request, 'menu/index.html')


# Student Dashboard View
@login_required
def dashboard(request):
    return render(
        request,
        'menu/student_dashboard.html',
        {'user': request.user}
    )


# Uesr Information Update View
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()

            new_password = form.cleaned_data.get("password")
            if new_password:
                user.set_password(new_password)

            user.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                'Your information has been updated successfully!'
            )
            return redirect('student_dashboard')
        else:
            messages.warning(
                request,
                'There was an error processing your request. Try again'
            )

    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form': form})


# Custom Error Pages
def handler404(request, exception):
    return render(request, "errors/404.html", status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)
