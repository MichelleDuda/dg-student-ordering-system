from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CustomUserChangeForm(UserChangeForm):
    """ This form is used to update user profile information. """
    """ Use of widgets from Django documentation """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        label="New Password",
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        label="Confirm New Password",
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user


class ContactForm(forms.Form):
    """ This form is used to collect information for users to send feeback. """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                 'placeholder': 'Your Email'
            }
        )
    )
    subject = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4, 'placeholder': 'Your Message'
            }
        )
    )
