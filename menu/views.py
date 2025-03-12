from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserChangeForm, ContactForm

# Views


# Home View
def index(request):
    """Render and return the Home page. """
    return render(request, 'menu/index.html')


# Student Dashboard View
@login_required
def dashboard(request):
    """
    Render and return the Student Dashboard page.
    Only accessible to authenticated users.
    """
    return render(
        request,
        'menu/student_dashboard.html',
        {'user': request.user}
    )


# Uesr Information Update View
@login_required
def update_profile(request):
    """
    Handles update of user profile information
    Only accessible to authenticated users.
    """
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
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(
                        request,
                        f"Error Occurred: {error}. Please try again"
                    )

    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form': form})


# Contact View
def contact_us(request):
    """ Handles contact form submission """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(
                f"New contact message from {name} ({email}):\n"
                f"Subject: {subject}\n"
                f"Message:{message}"
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )
            return redirect("student_dashboard")

        else:
            messages.error(
                request,
                "There was an error submitting the form. Please try again."
            )

    else:
        form = ContactForm()

    return render(request, "menu/contact.html", {"form": form})


# Custom Error Pages
def handler404(request, exception):
    return render(request, "errors/404.html", status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)
