from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True, label="First Name")
    last_name = forms.CharField(max_length=200, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
# to recognize user email is verified or not
User = get_user_model()
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Your Email",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError(
                "This email is not registered in the system. Please enter another email."
            )
        return email