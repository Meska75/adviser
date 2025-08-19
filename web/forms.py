from web.models import Contact
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']